# global variables - referencing x and y axis coords
REGION_BATTLE = (1744, 406, 200, 170)                   # battle region (below equipment set and skill bar)
REGION_MINIMAP = (1751, 34, 110, 107)                   # northeast minimap
REGION_MANA = (1840, 161, 24, 18)                       # region when mana is ~95% full
REGION_ARROW = (1841, 289)                              # arrow region
MONSTER_IN_BATTLE = (1765, 443)                         # first monster on battle
REGION_PLAYER = (1201, 393, 126, 126)                   # region 8x8 sqm near player (to loot dead copses)
PLAYER_SQM = (1268, 405)                                # sqm under player foot (to drop items from lootbag)
REGION_LOOT = (1745, 569, 167, 461)                     # region to find items from corpse (below battle)

# directory to images (change this to play other ots) 
img_dir =  "antiga/images/"
icons_dir = "antiga/icons/"

# items to collect from corpse
items = ["goldcoin1", "goldcoin2"]                      # gold coins from loot (5-9 and 10-24 stacks)
food = ["ham", "meat"]                                  # food to eat from dead corpse
drop_items = ["mace", "sword"]                          # items to drop on the floor
bpname = img_dir + "backpack" + ".PNG"                  # backpack to store gold
bags = ["bagloot"]                                      # bagloot from monster

# hunting monsters (change this for other hunts)
target_list = ["rotworm"]
dead_monster = ["dead_rotworm"]