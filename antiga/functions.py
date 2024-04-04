import pyautogui
import keyboard
import config
import threading
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

# search for monster and attack if it is on battle
def attack_next_monster(): 
  for target in config.target_list:
    targeting = pyautogui.locateOnScreen(config.img_dir + "targeting_" + target + ".PNG", confidence=0.99, region=config.REGION_BATTLE)
    monster_on_battle = pyautogui.locateOnScreen(config.img_dir + target + ".PNG", confidence=0.9, region=config.REGION_BATTLE)
    if monster_on_battle and not targeting:
      sleep(1)
      pyautogui.moveTo(config.MONSTER_IN_BATTLE)
      sleep(0.5)
      pyautogui.click(button="left")

# open dead corpse in REGION_PLAYER (8x8 sqm)
def open_corpse(target_monster):
  count = len(target_monster)
  for monster in range(0,(count)):
    dead_monster = pyautogui.locateAllOnScreen(config.img_dir + target_monster[monster] + ".PNG", confidence=0.94, region=config.REGION_PLAYER)
    sleep(0.5)
    for corpse in dead_monster:
      center_x, center_y = pyautogui.center(corpse)
      pyautogui.moveTo(center_x, center_y)
      pyautogui.click(button="right")
      sleep(0.5)

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

# drop loot on the floor
def drop_loot_on_floor(dropitems, bags):
  count_bags = len(bags)
  count_items = len(dropitems)
  for i in range(0,(count_bags)):
    bagloot = pyautogui.locateAllOnScreen(config.img_dir + bags[i] + ".PNG", confidence=0.9, region=config.REGION_LOOT)
    for bag in bagloot:
      center_x, center_y = pyautogui.center(bag)
      pyautogui.moveTo(center_x, center_y)
      sleep(0.5)
      pyautogui.click(button="right")
      sleep(0.2)
      for item in range(0,(count_items)):
         item_to_drop = pyautogui.locateAllOnScreen(config.img_dir + dropitems[item] + ".PNG", confidence=0.9, region=config.REGION_LOOT)
         for drop_item in item_to_drop:
            center_x, center_y = pyautogui.center(drop_item)
            pyautogui.moveTo(center_x, center_y)
            sleep(0.5)
            pyautogui.dragTo(config.PLAYER_SQM, duration=0.6)
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
threadKillMonster.start()