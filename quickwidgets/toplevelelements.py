# -*- coding: utf-8 -*-

from kaiengine.display import getWindowDimensionsScaled
from kaiengine.interface import ScreenElement, pushTopElement, popTopElement
from kaiengine.gconfig import WHITE_PIXEL_FILEPATH, COLOR_BLACK

DEFAULT_FADE_TIME = 20

SCENE_FADE_LOCK = "_SCENE_FADE_LOCK"

class Scene(ScreenElement):
    '''A very basic top level element, with fade ins/outs and convenience functions to switch to different ones.'''

    def __init__(self, *args, fade_in_time = DEFAULT_FADE_TIME, **kwargs):
        super().__init__(*args, **kwargs)
        #fade attributes
        self.fade_total_time = 0
        self.fade_time = 0
        self.done_fading = True

        #setup background
        self.setSpriteFollowCamera(True) #set background to follow camera by default
        self.setSpriteDimensions(*getWindowDimensionsScaled()) # tile the background
        self.tileSprite(True)

        #setup darkener
        darkener = ScreenElement(WHITE_PIXEL_FILEPATH)
        self._darkener_id = self.addChild(darkener, False)
        darkener.setSpriteFollowCamera(True)
        darkener.setSpriteDimensions(*getWindowDimensionsScaled())
        darkener.setSpriteColor(*COLOR_BLACK)
        darkener.setSpriteAlpha(0.0)

        if fade_in_time > 0:
            self.fadeIn(fade_in_time)



    #darkener functions
    def getDarkener(self):
        #convenience function
        return self.getChild(self._darkener_id)

    def fadeIn(self, time = DEFAULT_FADE_TIME):
        self._fadeStart(time)
        self.getDarkener().setSpriteAlpha(1.0)
        self.schedule(self._fadeIn, 0, True)

    def fadeOut(self, time = DEFAULT_FADE_TIME):
        self._fadeStart(time)
        self.getDarkener().setSpriteAlpha(0.0)
        self.schedule(self._fadeOut, 0, True)

    def checkDoneFading(self):
        return self.done_fading

    def _fadeStart(self, time):
        self.lockInput(SCENE_FADE_LOCK)
        self.unschedule(self._fadeIn)
        self.unschedule(self._fadeOut)
        time = max(0.0, float(time))
        self.fade_total_time = time
        self.fade_time = time
        self.done_fading = False

    def _fadeIn(self):
        self.fade_time -= 1
        try:
            self.getDarkener().setSpriteAlpha(max(0.0, self.fade_time) / self.fade_total_time)
        except ZeroDivisionError:
            self.fade_time = 0
        if self.fade_time <= 0:
            self._fadeFinish()

    def _fadeOut(self):
        self.fade_time -= 1
        try:
            self.getDarkener().setSpriteAlpha(1.0 - max(0.0, self.fade_time) / self.fade_total_time)
        except ZeroDivisionError:
            self.fade_time = 0
        if self.fade_time <= 0:
            self._fadeFinish()

    def _fadeFinish(self):
        self.done_fading = True
        self.unschedule(self._fadeOut)
        self.unschedule(self._fadeIn)
        self.unlockInput(SCENE_FADE_LOCK)

    #scene change functions
    def fadeToScene(self, scene_type, time = DEFAULT_FADE_TIME, popself = False, args = [], kwargs = {}):
        self.fadeOut(time)
        self.waitForCondition(self._fadeToScene, self.checkDoneFading, scene_type, popself, args, kwargs)

    def _fadeToScene(self, scene_type, popself, args, kwargs):
        self.sceneTransition(scene_type(*args, **kwargs), popself)

    def sceneTransition(self, scene, popself = False):
        if popself:
            popTopElement()
        pushTopElement(scene)

    def fadeToPreviousScene(self, time = DEFAULT_FADE_TIME):
        self.fadeOut(time)
        self.waitForCondition(self._fadeToPreviousScene, self.checkDoneFading)

    def _fadeToPreviousScene(self):
        popTopElement()


    #overwritten stuff

    def updateChildrenLayers(self, lastlayer = None):
        #should return the highest used layer
        if not lastlayer:
            lastlayer = super().updateChildrenLayers()
        lastlayer += 1
        self.getDarkener().setLayer(lastlayer) #ensure darkener on top
        return lastlayer

    def wakeUp(self, *args, **kwargs):
        awoken = super().wakeUp(*args, **kwargs)
        if awoken:
            self.fadeIn()
        return awoken


class SplashScreen(Scene):
    def __init__(self, *args, hang_time = 120, fade_out_time = DEFAULT_FADE_TIME, next_scenes = [], **kwargs):
        super().__init__(*args, **kwargs)

        self._fade_out_time = fade_out_time
        self._hang_time = hang_time
        self._next_scenes = next_scenes

        self.waitForCondition(self.schedule, self.checkDoneFading, self.endHangTime, self._hang_time)


    def endHangTime(self):
        self.unschedule(self.endHangTime)
        scene_type = None
        args = None
        kwargs = None
        while scene_type is None:
            try:
                data = self._next_scenes.pop(0)
            except IndexError:
                break
            try:
                scene_type, args, kwargs = data
            except ValueError:
                from kaiengine.debug import debugMessage
                debugMessage("Cannot unpack scene data. Requires 3 arguments (scene_type, args, kwargs).")
                debugMessage(data)
        if scene_type is None:
            self.fadeToPreviousScene(self._fade_out_time)
        else:
            kwargs["next_scenes"] = self._next_scenes
            self.fadeToScene(scene_type, self._fade_out_time, True, args, kwargs)

    def addNextScene(self, scene, *args, **kwargs):
        self._next_scenes.append((scene, args, kwargs))

    #input events

    def confirm(self):
        if self.checkDoneFading():
            self.endHangTime()
            return True
