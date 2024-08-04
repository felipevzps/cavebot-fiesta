import pyautogui
import keyboard
#import config_nostalther as config       # import nostalther config
import config_antiga as config            # import antiga config
import threading
from collections import defaultdict
from time import sleep

loop_status = False

def start_loop():
    """
    Start the loop by setting the global loop_status to True.
    """
    global loop_status
    loop_status = True

def stop_loop():
    """
    Stop the loop by setting the global loop_status to False.
    """
    global loop_status
    loop_status = False

# register start/stop keys
keyboard.add_hotkey('page up', start_loop)
keyboard.add_hotkey('page down', stop_loop)

def conjure_rune():
    """
    Conjure a rune if mana is available. It locates the mana on the screen
    and uses the F1 hotkey to cast the spell.
    """
    mana = pyautogui.locateOnScreen(config.img_dir + "mana" + ".PNG", confidence=0.7, region=config.REGION_MANA)
    if mana is not None:
        keyboard.press_and_release('F1')

def eat_food():
    """
    Eat food from the REGION_ARROW slot by right-clicking it twice.
    """
    pyautogui.moveTo(config.REGION_ARROW)
    for i in range(2):
        pyautogui.click(config.REGION_ARROW, button='right')

def attack_next_monster():
    """
    Search for a monster and attack it if it is found in the battle region.
    If the battle is clean and a monster was attacked, it will open the dead corpses.
    """
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

def open_corpse():
    """
    Open the dead corpses in the REGION_PLAYER (8x8 sqm). It moves the mouse to pre-defined
    positions and right-clicks to open corpses.
    """
    for pos in config.POS_LIST:
        pyautogui.moveTo(pos[0], pos[1])
        pyautogui.click(button="right")


'''
# TODO: The corpses of some creatures are not being found. 
# find a more effective method to locate them.
def open_corpse(target_monster):
  # find and open dead corpse in REGION_PLAYER (8x8 sqm)
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

def eat_food_from_corpse(fooditems):
    """
    Eat food from the corpse loot by right-clicking on identified food items in the REGION_LOOT.
    
    Parameters:
    fooditems (list): List of food item image names to locate and eat.
    """
    count = len(fooditems)
    for item in range(count):
        food = pyautogui.locateAllOnScreen(config.img_dir + fooditems[item] + ".PNG", confidence=0.9, region=config.REGION_LOOT)
        for item in food:
            center_x, center_y = pyautogui.center(item)
            pyautogui.moveTo(center_x, center_y)
            sleep(0.5)
            pyautogui.click(button="right") 

def loot_corpse(lootitems):
    """
    Loot items from a corpse by dragging them to the backpack.
    
    Parameters:
    lootitems (list): List of loot item image names to locate and loot.
    """
    backpack = pyautogui.locateOnScreen(config.bpname)
    count = len(lootitems)
    for item in range(count):
        gold = pyautogui.locateAllOnScreen(config.img_dir + lootitems[item] + ".PNG", confidence=0.9, region=config.REGION_LOOT)
        for item in gold:
            center_x, center_y = pyautogui.center(item)
            pyautogui.moveTo(center_x, center_y)
            sleep(0.5)
            pyautogui.dragTo(backpack.left, backpack.top + 20, duration=0.2)
            sleep(0.5)
            pyautogui.press('enter')
            sleep(1)

def find_coin_positions(coin_image, region):
    """
    Find gold coin positions (clusters) on the screen within a specified region.
    
    Parameters:
    coin_image (str): The image file name of the coin.
    region (tuple): The region of the screen to search for coins.
    
    Returns:
    dict: A dictionary of coin positions grouped by their proximity.
    """
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

def loot_goldcoin(coins):
    """
    Loot gold coins from a corpse by dragging them to the backpack.
    
    Parameters:
    coins (list): List of coin image names to locate and loot.
    """
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
                    pyautogui.dragTo(backpack.left, backpack.top + 20, duration=0.3)
                    sleep(0.1)
                    pyautogui.press('enter')
                    sleep(0.3) 
                    looted = True
                    break  # break after looting the first coin in the group

            if not looted:
                break  # exit if no coin was looted in this iteration

def drop_loot_on_floor(dropitems, bags):
    """
    Drop loot on the floor by dragging items from bags to the player's location.
    
    Parameters:
    dropitems (list): List of items to drop.
    bags (list): List of bag image names to locate and open.
    """
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

def move(location):
    """
    Move the mouse to the center of the specified location.
    
    Parameters:
    location (tuple): The location to move the mouse to.
    """
    x, y = pyautogui.center(location)
    pyautogui.moveTo(x, y)

def move_and_click(location):
    """
    Move the mouse to the center of the specified location and click.
    
    Parameters:
    location (tuple): The location to move the mouse to and click.
    """
    move(location)
    pyautogui.click()
    sleep(0.5)

def thread_attack_monster():
    """
    Open a thread to continuously attack monsters while loop_status is True.
    """
    while True:  # infinite loop to continuos attack monsters
        if loop_status:
            attack_next_monster()
   
# creates an attack thread outside principal loop
threadKillMonster = threading.Thread(target=thread_attack_monster)
threadKillMonster.daemon = True  # defining thread as daemon to stop it when the principal program ends
#threadKillMonster.start()