# global variables - referencing x and y axis coords
REGION_BATTLE = (1746, 360, 173, 178)                   # battle region (below equipment set and skill bar)
REGION_MINIMAP = (1755, 35, 108, 105)                   # northeast minimap
REGION_MANA = (1840, 161, 24, 18)                       # region when mana is ~95% full
REGION_ARROW = (1841, 289)                              # arrow region
MONSTER_IN_BATTLE = (1754, 383)                         # first monster on battle
REGION_PLAYER = (1193, 193, 126, 129)                   # region 8x8 sqm near player (to loot dead copses)
PLAYER_SQM = (1251, 253)                                # sqm under player foot (to drop items from lootbag)
REGION_LOOT = (1748, 677, 169, 360)                     # region to find items from corpse (below battle)

# directory to images (change this to play other ots) 
img_dir =  "cavebot-fiesta/nostalther/images/"
icons_dir = "cavebot-fiesta/nostalther/icons/"

# items to collect from corpse
items = []                                              # loot this items
coins = ["goldcoin1", "goldcoin2"]                      # gold coins from loot (1-4 and 5-100 stacks)
food = ["ham", "meat"]                                  # food to eat from dead corpse
drop_items = ["mace", "sword", "ham"]                   # items to drop on the floor
bpname = img_dir + "purple_backpack" + ".PNG"           # backpack to store gold
bags = ["bagloot"]                                      # bagloot from monster

# hunting monsters (change this for other hunts)
target_list = ["rotworm"]
dead_monster = ["dead_rotworm"]