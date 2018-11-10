from kaiengine.event import customEvent
from kaiengine.objectinterface import EventInterface
from kaiengine.uidgen import IdentifiedObject

from .interfaceElementKeys import *


class ListenerInitializerInterface(EventInterface):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._input_locks = set()
        self._input_listeners = []

    def _initListener(self, event_key, func, priority, lock, sleep_when_unfocused):
        def instantiated(*args, **kwargs):
            if (not lock) or (not self._input_locks):
                return func(self, *args, **kwargs)
        self.addCustomListener(event_key, instantiated, priority)
        if sleep_when_unfocused:
            self._input_listeners.append((event_key, instantiated, priority))

    def _initChildListener(self, child_key, event_key, func, priority, lock):
        child = getattr(self, child_key)
        event_key = child.id + event_key
        self._initListener(event_key, func, priority, lock, False)

class EventIDInterface(IdentifiedObject, ListenerInitializerInterface):

    def event(self, event_key, **kwargs):
        customEvent(self.id + event_key, origin_id=self.id, **kwargs)

def _event_response(event_key, priority=None, lock=False, sleep_when_unfocused=False):
    def decorator(func):
        func._listener_init_data = (event_key, priority, lock, sleep_when_unfocused)
        return func
    return decorator

def on_event(event_key, priority=None, lock=False):
    return _event_response(event_key, priority, lock)

def on_input(input_key, priority=None, lock=True):
    return _event_response(input_key, priority, lock, sleep_when_unfocused=True)

def _child_event_response(event_append, event_key, *args, **kwargs):
    if kwargs:
        try:
            priority = kwargs["priority"]
        except:
            priority = None
        try:
            lock = kwargs["lock"]
        except:
            lock = None
        def decorator(func):
            func._special_key_append = event_append
            func._child_listener_init_data = (event_key, priority, lock)
            return func
        return decorator
    else:
        func = args[0]
        func._special_key_append = event_append
        func._child_listener_init_data = (event_key, None, True) #TODO: consider whether we can make a better guess on lock value
    return func

def on_activate(*args, **kwargs):
    return _child_event_response(ACTIVATE_APPEND, EVENT_INTERFACE_ACTIVATED, *args, **kwargs)
