
from kaiengine.input.keys import *

INPUT_EVENT_TYPE_PRESS = "__INPUT_EVENT_TYPE_PRESS"
INPUT_EVENT_TYPE_RELEASE = "__INPUT_EVENT_TYPE_RELEASE"
INPUT_EVENT_TYPE_HOLD = "__INPUT_EVENT_TYPE_HOLD"

INPUT_EVENT_CONFIRM = "INPUT_EVENT_CONFIRM"
INPUT_EVENT_CONFIRM_UP = "INPUT_EVENT_CONFIRM_UP"
INPUT_EVENT_CONFIRM_HOLD = "INPUT_EVENT_CONFIRM_HOLD"
INPUT_EVENT_CANCEL = "INPUT_EVENT_CANCEL"
INPUT_EVENT_CANCEL_UP = "INPUT_EVENT_CANCEL_UP"
INPUT_EVENT_CANCEL_HOLD = "INPUT_EVENT_CANCEL_HOLD"
INPUT_EVENT_MOVE_UP = "INPUT_EVENT_MOVE_UP"
INPUT_EVENT_MOVE_UP_UP = "INPUT_EVENT_MOVE_UP_UP"
INPUT_EVENT_MOVE_UP_HOLD = "INPUT_EVENT_MOVE_UP_HOLD"
INPUT_EVENT_MOVE_DOWN = "INPUT_EVENT_MOVE_DOWN"
INPUT_EVENT_MOVE_DOWN_UP = "INPUT_EVENT_MOVE_DOWN_UP"
INPUT_EVENT_MOVE_DOWN_HOLD = "INPUT_EVENT_MOVE_DOWN_HOLD"
INPUT_EVENT_MOVE_LEFT = "INPUT_EVENT_MOVE_LEFT"
INPUT_EVENT_MOVE_LEFT_UP = "INPUT_EVENT_MOVE_LEFT_UP"
INPUT_EVENT_MOVE_LEFT_HOLD = "INPUT_EVENT_MOVE_LEFT_HOLD"
INPUT_EVENT_MOVE_RIGHT = "INPUT_EVENT_MOVE_RIGHT"
INPUT_EVENT_MOVE_RIGHT_UP = "INPUT_EVENT_MOVE_RIGHT_UP"
INPUT_EVENT_MOVE_RIGHT_HOLD = "INPUT_EVENT_MOVE_RIGHT_HOLD"

INPUT_EVENT_MENU = "INPUT_EVENT_MENU"
INPUT_EVENT_PAUSE = "INPUT_EVENT_PAUSE"
INPUT_EVENT_TAKE_SCREENSHOT = "INPUT_EVENT_TAKE_SCREENSHOT"
INPUT_EVENT_CAPTURE_ANIMATION = "INPUT_EVENT_CAPTURE_ANIMATION"
INPUT_EVENT_QUIT = "INPUT_EVENT_QUIT"

# to avoid JSON problems, we have to ensure keys to this dict are strings, not tuples (as would be more natural)

DEFAULT_BINDS = {
             (KAI_KEY_Z + INPUT_EVENT_TYPE_PRESS): INPUT_EVENT_CONFIRM,
             (KAI_KEY_ENTER + INPUT_EVENT_TYPE_PRESS): INPUT_EVENT_CONFIRM,
             (KAI_KEY_RETURN + INPUT_EVENT_TYPE_PRESS): INPUT_EVENT_CONFIRM,
             (KAI_KEY_MOUSE_LEFT + INPUT_EVENT_TYPE_PRESS): INPUT_EVENT_CONFIRM,

             (KAI_KEY_Z + INPUT_EVENT_TYPE_RELEASE): INPUT_EVENT_CONFIRM_UP,
             (KAI_KEY_ENTER + INPUT_EVENT_TYPE_RELEASE): INPUT_EVENT_CONFIRM_UP,
             (KAI_KEY_RETURN + INPUT_EVENT_TYPE_RELEASE): INPUT_EVENT_CONFIRM_UP,
             (KAI_KEY_MOUSE_LEFT + INPUT_EVENT_TYPE_RELEASE): INPUT_EVENT_CONFIRM_UP,

             (KAI_KEY_Z + INPUT_EVENT_TYPE_HOLD): INPUT_EVENT_CONFIRM_HOLD,
             (KAI_KEY_ENTER + INPUT_EVENT_TYPE_HOLD): INPUT_EVENT_CONFIRM_HOLD,
             (KAI_KEY_RETURN + INPUT_EVENT_TYPE_HOLD): INPUT_EVENT_CONFIRM_HOLD,
             (KAI_KEY_MOUSE_LEFT + INPUT_EVENT_TYPE_HOLD): INPUT_EVENT_CONFIRM_HOLD,


             (KAI_KEY_X + INPUT_EVENT_TYPE_PRESS): INPUT_EVENT_CANCEL,
             (KAI_KEY_BACKSPACE + INPUT_EVENT_TYPE_PRESS): INPUT_EVENT_CANCEL,
             (KAI_KEY_SPACE + INPUT_EVENT_TYPE_PRESS): INPUT_EVENT_CANCEL,
             (KAI_KEY_MOUSE_RIGHT + INPUT_EVENT_TYPE_PRESS): INPUT_EVENT_CANCEL,

             (KAI_KEY_X + INPUT_EVENT_TYPE_RELEASE): INPUT_EVENT_CANCEL_UP,
             (KAI_KEY_BACKSPACE + INPUT_EVENT_TYPE_RELEASE): INPUT_EVENT_CANCEL_UP,
             (KAI_KEY_SPACE + INPUT_EVENT_TYPE_RELEASE): INPUT_EVENT_CANCEL_UP,
             (KAI_KEY_MOUSE_RIGHT + INPUT_EVENT_TYPE_RELEASE): INPUT_EVENT_CANCEL_UP,

             (KAI_KEY_X + INPUT_EVENT_TYPE_HOLD): INPUT_EVENT_CANCEL_HOLD,
             (KAI_KEY_BACKSPACE + INPUT_EVENT_TYPE_HOLD): INPUT_EVENT_CANCEL_HOLD,
             (KAI_KEY_SPACE + INPUT_EVENT_TYPE_HOLD): INPUT_EVENT_CANCEL_HOLD,
             (KAI_KEY_MOUSE_RIGHT + INPUT_EVENT_TYPE_HOLD): INPUT_EVENT_CANCEL_HOLD,


             (KAI_KEY_W + INPUT_EVENT_TYPE_PRESS): INPUT_EVENT_MOVE_UP,
             (KAI_KEY_UP + INPUT_EVENT_TYPE_PRESS): INPUT_EVENT_MOVE_UP,
             (KAI_KEY_S + INPUT_EVENT_TYPE_PRESS): INPUT_EVENT_MOVE_DOWN,
             (KAI_KEY_DOWN + INPUT_EVENT_TYPE_PRESS): INPUT_EVENT_MOVE_DOWN,
             (KAI_KEY_A + INPUT_EVENT_TYPE_PRESS): INPUT_EVENT_MOVE_LEFT,
             (KAI_KEY_LEFT + INPUT_EVENT_TYPE_PRESS): INPUT_EVENT_MOVE_LEFT,
             (KAI_KEY_D + INPUT_EVENT_TYPE_PRESS): INPUT_EVENT_MOVE_RIGHT,
             (KAI_KEY_RIGHT + INPUT_EVENT_TYPE_PRESS): INPUT_EVENT_MOVE_RIGHT,

             (KAI_KEY_W + INPUT_EVENT_TYPE_RELEASE): INPUT_EVENT_MOVE_UP_UP,
             (KAI_KEY_UP + INPUT_EVENT_TYPE_RELEASE): INPUT_EVENT_MOVE_UP_UP,
             (KAI_KEY_S + INPUT_EVENT_TYPE_RELEASE): INPUT_EVENT_MOVE_DOWN_UP,
             (KAI_KEY_DOWN + INPUT_EVENT_TYPE_RELEASE): INPUT_EVENT_MOVE_DOWN_UP,
             (KAI_KEY_A + INPUT_EVENT_TYPE_RELEASE): INPUT_EVENT_MOVE_LEFT_UP,
             (KAI_KEY_LEFT + INPUT_EVENT_TYPE_RELEASE): INPUT_EVENT_MOVE_LEFT_UP,
             (KAI_KEY_D + INPUT_EVENT_TYPE_RELEASE): INPUT_EVENT_MOVE_RIGHT_UP,
             (KAI_KEY_RIGHT + INPUT_EVENT_TYPE_RELEASE): INPUT_EVENT_MOVE_RIGHT_UP,

             (KAI_KEY_W + INPUT_EVENT_TYPE_HOLD): INPUT_EVENT_MOVE_UP_HOLD,
             (KAI_KEY_UP + INPUT_EVENT_TYPE_HOLD): INPUT_EVENT_MOVE_UP_HOLD,
             (KAI_KEY_S + INPUT_EVENT_TYPE_HOLD): INPUT_EVENT_MOVE_DOWN_HOLD,
             (KAI_KEY_DOWN + INPUT_EVENT_TYPE_HOLD): INPUT_EVENT_MOVE_DOWN_HOLD,
             (KAI_KEY_A + INPUT_EVENT_TYPE_HOLD): INPUT_EVENT_MOVE_LEFT_HOLD,
             (KAI_KEY_LEFT + INPUT_EVENT_TYPE_HOLD): INPUT_EVENT_MOVE_LEFT_HOLD,
             (KAI_KEY_D + INPUT_EVENT_TYPE_HOLD): INPUT_EVENT_MOVE_RIGHT_HOLD,
             (KAI_KEY_RIGHT + INPUT_EVENT_TYPE_HOLD): INPUT_EVENT_MOVE_RIGHT_HOLD,

             (KAI_KEY_ESCAPE + INPUT_EVENT_TYPE_PRESS): INPUT_EVENT_QUIT,

             (KAI_KEY_P + INPUT_EVENT_TYPE_PRESS): INPUT_EVENT_TAKE_SCREENSHOT
             }
