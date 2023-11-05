import pyautogui
import keyboard
import random
from time import sleep
import threading

REGION_BATTLE = (1650, 500, 300, 250)
REGION_MANA = (1880, 235, 35, 22)
REGION_ARROW = (1830, 359)
MINIMAP = (1728, 31, 183, 182)

loop_status = False

def start_loop():
    global loop_status
    loop_status = True

def stop_loop():
    global loop_status
    loop_status = False

# Register start/stop keys
keyboard.add_hotkey('page up', start_loop)
keyboard.add_hotkey('page down', stop_loop)

# Conjure rune (cast spell saved on F4 hotkey)
def conjure_rune():
  mana = pyautogui.locateOnScreen('fibula_rotworms/images/mana.PNG', confidence=0.6, region=REGION_MANA)
  if mana != None:
    pyautogui.moveTo(REGION_ARROW)
    pyautogui.click(REGION_ARROW, button='left')
    keyboard.press_and_release('F4')

# Eat food on REGION_ARROW slot
def eat_food():
   pyautogui.moveTo(REGION_ARROW)
   for i in range(2):
    pyautogui.click(REGION_ARROW, button='right')

# Search for monster and attack if it is on battle
def attack_next_rotworm(): 
  
  targeting = pyautogui.locateOnScreen('fibula_rotworms/images/targeting_rotworm.PNG', confidence=0.9, region=REGION_BATTLE)
  rotworm_on_battle = pyautogui.locateOnScreen('fibula_rotworms/images/rotworm.PNG', confidence=0.9, region=REGION_BATTLE)
  halloween_skeleton_on_battle = pyautogui.locateOnScreen('fibula_rotworms/images/halloween_skeleton.PNG', confidence=0.9, region=REGION_BATTLE)
  attacking_monk = pyautogui.locateOnScreen('fibula_rotworms/images/attacking_monk.PNG', confidence=0.9, region=REGION_BATTLE)
  
  if rotworm_on_battle and not targeting:
    sleep(0.5)
    pyautogui.press("'")

  if halloween_skeleton_on_battle and not targeting:
    sleep(0.5)
    pyautogui.press("'")

  if attacking_monk:
    sleep(0.5)
    pyautogui.press('1')

# Move mouse to center of the image
def move(location):
  x,y = pyautogui.center(location)
  pyautogui.moveTo(x, y)

# Click on minimap
def move_and_click(location):
  move(location)
  pyautogui.click()

# Function that open a thread for attack_next_rotworm()
def thread_attack_rotworm():
    while True:  # Infinite loop to continuos attack rotworms
        if loop_status:
            attack_next_rotworm()

# Creates a attack thread outside principal loop
threadKillRotworm = threading.Thread(target=thread_attack_rotworm)
threadKillRotworm.daemon = True  # Defining thread as daemon to stop it when the principal program ends
threadKillRotworm.start()

while True:
    if loop_status:
        for waypoint in range(45):

            position_in_map = pyautogui.locateOnScreen('fibula_rotworms/icons/icon_{}.png'.format(waypoint), confidence=0.9, region=MINIMAP)

            if position_in_map:
                move_and_click(position_in_map)
                print('Going to waypoint: {}'.format(waypoint))
                conjure_rune()
                eat_food()

                # Calculate a random wait time between 6 and 8 seconds
                wait_time = random.uniform(6, 8)
                sleep(wait_time)

                check_position = pyautogui.locateOnScreen('fibula_rotworms/icons/icon_{}.png'.format(waypoint), confidence=0.9, region=MINIMAP)
                if not check_position:
                    print('Already on waypoint: {}'.format(waypoint))
                    conjure_rune()

                    while True:
                        conjure_rune()

                        battle_monk = pyautogui.locateOnScreen('fibula_rotworms/images/region_battle_monk.PNG', confidence=0.9, region=REGION_BATTLE)
                        battle_berserker = pyautogui.locateOnScreen('fibula_rotworms/images/region_battle_berserker.PNG', confidence=0.9, region=REGION_BATTLE)
                        if battle_monk or battle_berserker:
                            print('Clean battle')
                            print('---')
                            break
