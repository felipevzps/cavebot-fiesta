# global variables - referencing x and y axis coords
WAYPOINT_RANGE = range(0,29)                            # waypoint (icons) range
REGION_BATTLE = (1744, 406, 176, 166)                   # battle region (below equipment set and skill bar)
REGION_MINIMAP = (1753, 32, 109, 111)                   # northeast minimap
REGION_MANA = (1836, 162, 24, 18)                       # region when mana is ~95% full
REGION_ARROW = (1841, 289)                              # arrow region
MONSTER_IN_BATTLE = (1765, 444)                         # first monster on battle
REGION_PLAYER = (1212, 405, 112, 115)                   # region 8x8 sqm near player (to loot dead copses)
POS_LIST = [(1224, 410), (1263, 411),                   # region 8x8 sqm to right-clicks to open corpses
            (1307, 416), (1298, 451), 
            (1303, 499), (1261, 498), 
            (1226, 492), (1222, 456)]
PLAYER_SQM = (1248, 440)                                # sqm under player foot (to drop items from lootbag)
REGION_LOOT = (1743, 704, 177, 330)                     # region to find items from corpse (below battle)

# directory to images (change this to play other ots) 
img_dir =  "cavebot-fiesta/antiga/images/"
icons_dir = "cavebot-fiesta/antiga/icons/"

# items to collect from corpse
items = []                                              # loot this items
coins = ["goldcoin1", "goldcoin2"]                      # gold coins from loot (1-4 and 5-100 stacks)
food = ["ham", "meat"]                                  # food to eat from dead corpse
drop_items = ["mace", "sword", "ham"]                   # items to drop on the floor
bpname = img_dir + "yellow_backpack" + ".PNG"           # backpack to store gold
bags = ["bagloot"]                                      # bagloot from monster

# hunting monsters (change this for other hunts)
target_list = ["rotworm"]
dead_monster = ["dead_rotworm"]