

from .paths import *
from .datakeys import *

DYNAMIC_SETTINGS_FPS_ON = "FPS_VISIBLE"
DYNAMIC_SETTINGS_FPS_SIZE = "FPS_SIZE"
DYNAMIC_SETTINGS_SOUND_VOLUME = "SOUND_VOLUME"
DYNAMIC_SETTINGS_MUSIC_VOLUME = "MUSIC_VOLUME"
DYNAMIC_SETTINGS_SOUND_ON = "SOUND_ON"
DYNAMIC_SETTINGS_MUSIC_ON = "MUSIC_ON"
DYNAMIC_SETTINGS_GLOBAL_SCALING = "GLOBAL_SCALING"
DYNAMIC_SETTINGS_WINDOW_DIMENSIONS = "WINDOW_DIMENSIONS"
DYNAMIC_SETTINGS_DEBUG_ON = "DEBUG_ON"
DYNAMIC_SETTINGS_LOOSE_WARNING = "LOOSE_FILE_WARNING"
DYNAMIC_SETTINGS_MISSING_FILE_WARNING = "MISSING_FILE_WARNING"
DYNAMIC_SETTINGS_USE_GZIP = "USE_GZIP"
DYNAMIC_SETTINGS_PRINT_UNKNOWN_KEYS = "PRINT_UNKNOWN_KEYS"
DYNAMIC_SETTINGS_SKIP_UNDERSCORE_KEYS = "SKIP_UNDERSCORE_KEYS"
DYNAMIC_SETTINGS_LOAD_ARCHIVE_IN_MEMORY = "LOAD_ARCHIVE_IN_MEMORY"
DYNAMIC_SETTINGS_FRAMES_PER_SECOND = "GAME_FPS"
DYNAMIC_SETTINGS_FPS_CLAMP = "MAX_FPS"
DYNAMIC_SETTINGS_MAX_LAG_TIME = "MAX_LAG_TIME"
DYNAMIC_SETTINGS_FULLSCREEN = "FULLSCREEN"
DYNAMIC_SETTINGS_FAKE_FULLSCREEN = "FAKEFULLSCREEN"
DYNAMIC_SETTINGS_GAME_CAPTION = "GAME_CAPTION"
DYNAMIC_SETTINGS_VSYNC = "VSYNC"
DYNAMIC_SETTINGS_KEY_BINDS = "KEYBINDS"
DYNAMIC_SETTINGS_DEFAULT_SAVE_PATH = "DEFAULT_SAVE_PATH"
DYNAMIC_SETTINGS_SAVE_PATH = "REGULAR_SAVE_PATH"
DYNAMIC_SETTINGS_DEFAULT_SAVE_FILENAME = "DEFAULT_SAVE_FILENAME"
DYNAMIC_SETTINGS_LOCALE = "LOCALE"



#can be overrided by passing a dict to settings' initialize
DEFAULT_DYNAMIC_SETTINGS = {DYNAMIC_SETTINGS_FPS_ON: True,
                DYNAMIC_SETTINGS_FPS_SIZE: 45,
                DYNAMIC_SETTINGS_SOUND_VOLUME:0.5,
                DYNAMIC_SETTINGS_MUSIC_VOLUME:0.5,
                DYNAMIC_SETTINGS_SOUND_ON:True,
                DYNAMIC_SETTINGS_MUSIC_ON:True,
                DYNAMIC_SETTINGS_GLOBAL_SCALING:1.0,
                DYNAMIC_SETTINGS_WINDOW_DIMENSIONS: [800,600],
                DYNAMIC_SETTINGS_DEBUG_ON: True,
                DYNAMIC_SETTINGS_LOOSE_WARNING: False,
                DYNAMIC_SETTINGS_MISSING_FILE_WARNING: False,
                DYNAMIC_SETTINGS_USE_GZIP: False,
                DYNAMIC_SETTINGS_PRINT_UNKNOWN_KEYS: True, #keys without defaults set in the class
                DYNAMIC_SETTINGS_SKIP_UNDERSCORE_KEYS: True, #set to false if you want to print unknown keys that start with underscores too
                DYNAMIC_SETTINGS_LOAD_ARCHIVE_IN_MEMORY: True, #set to false for archives too big to fit comfortably in RAM, at the cost of hitting the harddrive frequently
                DYNAMIC_SETTINGS_FRAMES_PER_SECOND: 60.0,
                DYNAMIC_SETTINGS_FPS_CLAMP: 1000000.0, #for dynamically changing the fps; the fps setting will be used for most calculations regarding in-game timing, though
                DYNAMIC_SETTINGS_MAX_LAG_TIME: 1.0,
                DYNAMIC_SETTINGS_FULLSCREEN: False,
                DYNAMIC_SETTINGS_GAME_CAPTION: "Needs a caption",
                DYNAMIC_SETTINGS_VSYNC: False,
                DYNAMIC_SETTINGS_KEY_BINDS: {},
                DYNAMIC_SETTINGS_DEFAULT_SAVE_PATH: [RESOURCE_PATH,MISC_DIR], #for the default save that the game starts with
                DYNAMIC_SETTINGS_SAVE_PATH: [SAVES_PATH], #for player saves
                DYNAMIC_SETTINGS_DEFAULT_SAVE_FILENAME: "default",
                DYNAMIC_SETTINGS_FAKE_FULLSCREEN: False,
                DYNAMIC_SETTINGS_LOCALE: LOCALE_ENGLISH
                }