# File for constant info such as RGB colours and 
import ctypes
user32 = ctypes.windll.user32
RESOLUTION = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
# The screen's width and height
#RESOLUTION      = (1366, 768)
# The screen's width / 2 and height / 2
HALF_RES        = (RESOLUTION[0] // 2, RESOLUTION[1] // 2)
# Maximum framerate for the game
FPS_CAP         = 31
# Tile widths and heights
TILE_WIDTH      = 16
TILE_HEIGHT     = 16
HALF_WIDTH      = 8
HALF_HEIGHT     = 8

BOSS_ALIVE      = True

# Various colours to use
WHITE           = (255, 255, 255)
BLACK           = (  0,   0,   0)
GREY            = (151, 160, 175)
BROWN           = (188, 113, 113)
ORANGE          = (255, 150, 150)
RED             = (200,  50,  50)
BLUE            = (100, 100, 255)
GREEN           = ( 50, 200,  50)
PURPLE          = (128,   0, 128)
# Various colours with alpha values for transparency
WHITEA          = (255, 255, 255, 100)
BLACKA          = (  0,   0,   0, 100)
VOIDA           = (  0,   0,   0, 200)
BROWNA          = (188, 113, 113, 100)
ORANGEA         = (255, 150, 150, 100)
REDA            = (200,  50,  50, 100)
YELLOWA         = (248, 222, 126, 100)
BLUEA           = (100, 100, 255, 100)
GREENA          = (249, 166,   2, 100)
PURPLEA         = (128,   0, 128, 100)

RARITIES        = [WHITEA, GREENA, BLUEA, PURPLEA, ORANGEA]
RARITY_SCALING  = [1.1,   1.2,   1.3,  1.4,    1.5]

# Positions for each player's screen
DISPLAY_KEY     = [ (0,              0),
                    (HALF_RES[0],    0),
                    (0,              HALF_RES[1]) ,
                    (HALF_RES[0],    HALF_RES[1]) ]

DIRECTION_KEY   = { "UP"    : (0,-1) ,
                    "DOWN"  : (0, 1) ,
                    "LEFT"  : (-1,0) ,
                    "RIGHT" : (1 ,0) ,
                    "NONE"  : (0 ,0) }

DIRECTIONS      = { 0       : "RIGHT" ,
                    90      : "DOWN"  ,
                    180     : "LEFT"  ,
                    270     : "UP"    ,
                    360     : "RIGHT" }

# Offset for drawing the players when their image isn't a 32x32 resolution
WEAPON_OFFSET   = { "sword"     : { "LEFT"  : (0, 0) ,
                                    "RIGHT" : (0, 0) ,
                                    "UP"    : (0, 0) ,
                                    "DOWN"  : (0, 0) } ,
                    
                    "spear"     : { "LEFT"  : (0, 0) ,
                                    "RIGHT" : (0, 0) ,
                                    "UP"    : (0, 0) ,
                                    "DOWN"  : (0, 0) } ,
                    
                    "gauntlet"  : { "LEFT"  : (0, 0) ,
                                    "RIGHT" : (0, 0) ,
                                    "UP"    : (0, 0) ,
                                    "DOWN"  : (0, 0) } ,
                    
                    "bow"       : { "LEFT"  : (0, 0) ,
                                    "RIGHT" : (0, 0) ,
                                    "UP"    : (0, 0) ,
                                    "DOWN"  : (0, 0) } ,
                    
                    "gun"       : { "LEFT"  : (0, 0) ,
                                    "RIGHT" : (0, 0) ,
                                    "UP"    : (0, 0) ,
                                    "DOWN"  : (0, 0) } }

DIFFICULTY_KEY  = {0 : 1, 8 : 2, 13 : 3, 17 : 4, 20 : 5}
DIFFICULTY_COLOURS = {1 : WHITEA, 2 : YELLOWA, 3 : REDA, 4 : ORANGEA, 5 : PURPLEA}
ENEMY_NUMBERS   = {1 : 4,  2 : 4,  3 : 4,  4 : 4,  5 : 4}

TRIG_ACCURACY   = 90

# Maps for the boss room
map1 =    [ [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9] ,
            [9,3,3,3,3,0,0,0,0,0,3,3,3,3,0,0,0,0,0,3,3,3,3,9] ,
            [9,3,3,3,3,0,0,0,0,0,3,3,3,3,0,0,0,0,0,3,3,3,3,9] ,
            [9,3,3,3,3,0,0,0,0,0,3,3,3,3,0,0,0,0,0,3,3,3,3,9] ,
            [9,3,3,3,3,0,0,0,0,0,3,3,3,3,0,0,0,0,0,3,3,3,3,9] ,
            [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9] ,
            [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9] ,
            [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9] ,
            [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9] ,
            [9,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,9] ,
            [9,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,9] ,
            [9,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,9] ,
            [9,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,9] ,
            [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9] ,
            [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9] ,
            [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9] ,
            [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9] ,
            [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9] ,
            [9,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,9] ,
            [9,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,9] ,
            [9,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,9] ,
            [9,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,9] ,
            [9,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,9] ,
            [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9] ,
            [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9] ,
            [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9] ,
            [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9] ,
            [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9] ,
            [9,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,9] ,
            [9,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,9] ,
            [9,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,9] ,
            [9,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,9] ,
            [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9] ,
            [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9] ,
            [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9] ,
            [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9] ,
            [9,3,3,3,3,0,0,0,0,0,3,3,3,3,0,0,0,0,0,3,3,3,3,9] ,
            [9,3,3,3,3,0,0,0,0,0,3,3,3,3,0,0,0,0,0,3,3,3,3,9] ,
            [9,3,3,3,3,0,0,0,0,0,3,3,3,3,0,0,0,0,0,3,3,3,3,9] ,
            [9,3,3,3,3,0,0,0,0,0,3,3,3,3,0,0,0,0,0,3,3,3,3,9] ,
            [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9] ]

map1c =   [ [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] ,
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] ]

ROOM_MAP        = [map1]
ROOM_COLLISION  = [map1c]

