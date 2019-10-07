RESOLUTION      = (1366, 768)#(1366 // 2, 768 // 2)#(1366, 768)
HALF_RES        = (RESOLUTION[0] // 2, RESOLUTION[1] // 2)
FPS_CAP         = 31
TILE_WIDTH      = 15
TILE_HEIGHT     = 15

WHITE           = (255, 255, 255)
WHITEA          = (255, 255, 255, 100)
BLACK           = (  0,   0,   0)
BLACKA          = (  0,   0,   0, 100)
GREY            = (151, 160, 175)
BROWN           = (188, 113, 113)
ORANGE          = (255, 150, 150)
ORANGEA         = (255, 150, 150, 100)
RED             = (200,  50,  50)
BLUE            = (100, 100, 255)
BLUEA           = (100, 100, 255, 100)
GREEN           = ( 50, 200,  50)
GREENA          = ( 50, 200,  50, 100)
PURPLE          = (128,   0, 128)
PURPLEA         = (128,   0, 128, 100)

RARITIES        = [WHITEA, GREENA, BLUEA, PURPLEA, ORANGEA]
RARITY_SCALING  = [1.1,   1.2,   1.3,  1.4,    1.5]

DISPLAY_KEY     = [(0,              0),
                   (HALF_RES[0],    0),
                   (0,              HALF_RES[1]),
                   (HALF_RES[0],    HALF_RES[1])]

DIRECTION_KEY   = { "UP"    :(0,-1) ,
                    "DOWN"  :(0, 1) ,
                    "LEFT"  :(-1,0) ,
                    "RIGHT" :(1 ,0) }

TRIG_ACCURACY   = 90

maps = []

for n in range(0, 5):
    file = open("resources\maps\{}.txt".format(str(n + 1)), "r")
    contents    = file.readlines()
    file.close()

    currentMap  = []
##    for i in contents:
##        if "@" in i:    maps[n].append(currentMap); currentMap = []
##        i = i.translate({ord("\n"): None})
##        i = i.translate({ord("@") : None})
##        currentMap.append(list(i))

print(maps)
