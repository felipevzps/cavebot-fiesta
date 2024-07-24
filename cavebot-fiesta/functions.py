import pyautogui
import keyboard
import config
import threading
from collections import defaultdict
from time import sleep

loop_status = False

def start_loop():
  global loop_status
  loop_status = True

def stop_loop():
  global loop_status
  loop_status = False

# register start/stop keys
keyboard.add_hotkey('page up', start_loop)
keyboard.add_hotkey('page down', stop_loop)

# conjure rune (cast spell saved on F12 hotkey)
def conjure_rune():
  mana = pyautogui.locateOnScreen(config.img_dir + "mana" + ".PNG", confidence=0.7, region=config.REGION_MANA)
  if mana != None:
    keyboard.press_and_release('F1')

# eat food on REGION_ARROW slot
def eat_food():
  pyautogui.moveTo(config.REGION_ARROW)
  for i in range(2):
    pyautogui.click(config.REGION_ARROW, button='right')

'''
# search for monster and attack if it is on battle
def attack_next_monster(): 
  monster_on_battle = True
  monster_attacked = False
  while monster_on_battle != None:
    for target in config.target_list:
      targeting = pyautogui.locateOnScreen(config.img_dir + "targeting_" + target + ".PNG", confidence=0.99, region=config.REGION_BATTLE)
      monster_on_battle = pyautogui.locateOnScreen(config.img_dir + target + ".PNG", confidence=0.9, region=config.REGION_BATTLE)
      if monster_on_battle and not targeting:
        sleep(1)
        pyautogui.moveTo(config.MONSTER_IN_BATTLE)
        sleep(0.5)
        pyautogui.click(button="left")
        monster_attacked = True
        break
    else:
      # If no monster is found in the loop, exit the while loop
      break
  if monster_attacked:
     open_corpse()
'''

# search for monster and attack if it is on battle
def attack_next_monster():
    monster_attacked = False
    while True:
        monster_on_battle = False
        for target in config.target_list:
            targeting = pyautogui.locateOnScreen(config.img_dir + "targeting_" + target + ".PNG", confidence=0.99, region=config.REGION_BATTLE)
            monster_on_battle = pyautogui.locateOnScreen(config.img_dir + target + ".PNG", confidence=0.9, region=config.REGION_BATTLE)
            if monster_on_battle and not targeting:
                sleep(1)
                pyautogui.moveTo(config.MONSTER_IN_BATTLE)
                sleep(0.5)
                pyautogui.click(button="left")
                monster_attacked = True  # set to True when a monster is attacked
                break
        # exit the while loop if no monster is found
        if not monster_on_battle:
            break

    # check if a monster was attacked
    if monster_attacked:
        open_corpse()

# open dead corpse in REGION_PLAYER (8x8 sqm)
def open_corpse():
  pos_list = [(1223, 206), (1263, 208), (1301, 213), (1305, 252), (1302, 289), (1265, 285), (1226, 287), (1220, 251)]
  for pos in pos_list:
    pyautogui.moveTo(pos[0], pos[1])
    pyautogui.click(button="right")
    #sleep(0.3)
    
'''
# open dead corpse in REGION_PLAYER (8x8 sqm)
def open_corpse(target_monster):
  count = len(target_monster)
  for monster in range(0,(count)):
    dead_monster = pyautogui.locateAllOnScreen(config.img_dir + target_monster[monster] + ".PNG", confidence=0.96, region=config.REGION_PLAYER)
    sleep(0.5)
    for corpse in dead_monster:
      center_x, center_y = pyautogui.center(corpse)
      pyautogui.moveTo(center_x, center_y)
      pyautogui.click(button="right")
      sleep(0.8)
'''

# eat food from corpse loot (meat, ham, etc)
def eat_food_from_corpse(fooditems):
   count = len(fooditems)
   for item in range(0,(count)):
      food = pyautogui.locateAllOnScreen(config.img_dir + fooditems[item] + ".PNG", confidence=0.9, region=config.REGION_LOOT)
      for item in food:
         center_x, center_y = pyautogui.center(item)
         pyautogui.moveTo(center_x, center_y)
         sleep(0.5)
         pyautogui.click(button="right") 

# loot items from corpse
def loot_corpse(lootitems):
  backpack = pyautogui.locateOnScreen(config.bpname)
  count = len(lootitems)
  for item in range(0,(count)):
    gold = pyautogui.locateAllOnScreen(config.img_dir + lootitems[item] + ".PNG", confidence=0.9, region=config.REGION_LOOT)
    for item in gold:
      center_x, center_y = pyautogui.center(item)
      pyautogui.moveTo(center_x, center_y)
      sleep(0.5)
      pyautogui.dragTo(backpack.left, backpack.top+20, duration=0.2)
      sleep(0.5)
      pyautogui.press('enter')
      sleep(1)

# find goldcoin group position (cluster)
def find_coin_positions(coin_image, region):
    coin_positions = defaultdict(list)
    find_objects = pyautogui.locateAllOnScreen(coin_image, confidence=0.9, region=region)

    for coin_pos in find_objects:
        added_to_group = False
        for group, positions in coin_positions.items():
            for pos in positions:
                if abs(coin_pos.left - pos[0]) < 20 and abs(coin_pos.top - pos[1]) < 20:
                    coin_positions[group].append((coin_pos.left, coin_pos.top, coin_pos.width, coin_pos.height))
                    added_to_group = True
                    break
            if added_to_group:
                break

        if not added_to_group:
            coin_positions[len(coin_positions) + 1].append((coin_pos.left, coin_pos.top, coin_pos.width, coin_pos.height))

    return coin_positions

# loot goldcoins from corpse
def loot_goldcoin(coins):
    backpack = pyautogui.locateOnScreen(config.bpname)
    if not backpack:
        print("Backpack not found")
        return

    for coin in coins:
        while True:
            coin_positions = find_coin_positions(config.img_dir + coin + ".PNG", config.REGION_LOOT)
            if not coin_positions:
                break  # exit if no more coins are found

            # flag to check if any coin was looted in this iteration
            looted = False

            for group, positions in coin_positions.items():
                if positions:
                    position = positions[0]  # get the first coin position in the group
                    center_x = position[0] + position[2] // 2
                    center_y = position[1] + position[3] // 2
                    pyautogui.moveTo(center_x, center_y)
                    sleep(0.5)
                    pyautogui.dragTo(backpack.left, backpack.top + 20, duration=0.2)
                    sleep(0.1)
                    pyautogui.press('enter')
                    sleep(0.3) # 1
                    looted = True
                    break  # break after looting the first coin in the group

            if not looted:
                break  # exit if no coin was looted in this iteration

# drop loot on the floor
def drop_loot_on_floor(dropitems, bags):
    for bag in bags:
        bag_positions = list(pyautogui.locateAllOnScreen(config.img_dir + bag + ".PNG", confidence=0.99, region=config.REGION_LOOT))
        for position in bag_positions:
            center_x, center_y = pyautogui.center(position)
            pyautogui.moveTo(center_x, center_y)
            sleep(0.5)
            pyautogui.click(button="right")
            sleep(0.2)
    
    for dropitem in dropitems:
        item_positions = list(pyautogui.locateAllOnScreen(config.img_dir + dropitem + ".PNG", confidence=0.9, region=config.REGION_LOOT))
        for position in item_positions:
            center_x, center_y = pyautogui.center(position)
            pyautogui.moveTo(center_x, center_y)
            sleep(0.5)
            pyautogui.dragTo(config.PLAYER_SQM, duration=0.8)
            sleep(0.5)

# move mouse to center of the image
def move(location):
  x,y = pyautogui.center(location)
  pyautogui.moveTo(x, y)

# click on minimap
def move_and_click(location):
  move(location)
  pyautogui.click()
  sleep(0.5)

# function that open a thread for attack_next_rotworm()
def thread_attack_monster():
    while True:  # infinite loop to continuos attack rotworms
        if loop_status:
            attack_next_monster()
   
# creates a attack thread outside principal loop
threadKillMonster = threading.Thread(target=thread_attack_monster)
threadKillMonster.daemon = True  # defining thread as daemon to stop it when the principal program ends
#threadKillMonster.start()