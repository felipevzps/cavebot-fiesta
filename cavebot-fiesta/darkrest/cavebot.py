import pyautogui
import keyboard
import random
import time
from time import sleep
import threading

#ZOOM = 4x

REGION_BATTLE = (1650, 500, 500, 250)
REGION_MANA = (1852, 237, 59, 21)
REGION_ARROW = (1830, 359)
MINIMAP = (1728, 31, 183, 182)
PICKAXE = (1579, 545)

right = (1258,393,50,50)
left = (1192,396,50,50)
top = (1225,363,50,50)
bot = (1225,428,50,50)

list_positions = [top, bot, right, left]

loop_status = False

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

def start_loop():
    global loop_status
    loop_status = True

def stop_loop():
    global loop_status
    loop_status = False

# Register start/stop keys
keyboard.add_hotkey('page up', start_loop)
keyboard.add_hotkey('page down', stop_loop)

# Conjure rune (cast spell saved on F12 hotkey)
def conjure_rune():
  mana = pyautogui.locateOnScreen('fibula_rotworms/images/mana2.PNG', confidence=0.6, region=REGION_MANA)
  if mana != None:
    pyautogui.moveTo(REGION_ARROW)
    pyautogui.click(REGION_ARROW, button='left')
    keyboard.press_and_release('F12')

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
    pyautogui.press("numlock")

  if halloween_skeleton_on_battle and not targeting:
    sleep(0.5)
    pyautogui.press("numlock")

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

# Use pickaxe on ore -> gather silver and steel
def get_ore(location):
  if location != None:
    sleep(0.5)
    pyautogui.moveTo(PICKAXE)
    pyautogui.click(PICKAXE, button='right')
    sleep(0.5)
    move(location)
    pyautogui.click(button='left')
    sleep(1)
   
# Creates a attack thread outside principal loop
threadKillRotworm = threading.Thread(target=thread_attack_rotworm)
threadKillRotworm.daemon = True  # Defining thread as daemon to stop it when the principal program ends
threadKillRotworm.start()

ore_names = {
   0: 'Silver',
   1: 'Steel',
   2: 'Iron',
   3: 'Iron'
}

ore_positions = [8, 9, 10, 15, 31, 45]

print(current_time, ':', 'Starting cavebot ...')
print('---')

while True:
    if loop_status:
        for waypoint in range(46):

            position_in_map = pyautogui.locateOnScreen('fibula_rotworms/icons/icon_{}.png'.format(waypoint), confidence=0.9, region=MINIMAP)

            if position_in_map:
                
                t = time.localtime()
                current_time = time.strftime("%H:%M:%S", t)

                move_and_click(position_in_map)
                print(current_time, ':', 'Going to waypoint: {}'.format(waypoint))
                conjure_rune()
                eat_food()

                # Calculate a random wait time between 5 and 7 seconds
                wait_time = random.uniform(6, 7)
                sleep(wait_time)

                check_position = pyautogui.locateOnScreen('fibula_rotworms/icons/icon_{}.png'.format(waypoint), confidence=0.9, region=MINIMAP)
                
                if not check_position:
                    
                    t = time.localtime()
                    current_time = time.strftime("%H:%M:%S", t)

                    print(current_time, ':', 'Already on waypoint: {}'.format(waypoint))
                    conjure_rune()

                    while True:
                        
                        conjure_rune()

                        battle_monk = pyautogui.locateOnScreen('fibula_rotworms/images/region_battle_monk.PNG', confidence=0.9, region=REGION_BATTLE)
                        battle_berserker = pyautogui.locateOnScreen('fibula_rotworms/images/region_battle_berserker.PNG', confidence=0.9, region=REGION_BATTLE)
                        
                        if battle_monk or battle_berserker:
                            
                            t = time.localtime()
                            current_time = time.strftime("%H:%M:%S", t)

                            print(current_time, ':', 'Clean battle')
                            print('---')
                            break
                
                # Gathering steel, silver and iron
                if not check_position and waypoint in ore_positions:
                    
                    t = time.localtime()
                    current_time = time.strftime("%H:%M:%S", t)

                    print(current_time, ':', 'Already on position: {}'.format(waypoint))
                    print(current_time, ':', 'Starting mining ...')
                    sleep(3)

                    while True:
                        found_ore = False # Track if ore was found
                        for position in list_positions:
                              for index in range(4):
                                  
                                  ore = pyautogui.locateOnScreen('fibula_rotworms/ores/ore_{}.PNG'.format(index), confidence=0.7, region=position)
                                  
                                  if ore:
                                      
                                      t = time.localtime()
                                      current_time = time.strftime("%H:%M:%S", t)

                                      print(current_time, ':', 'Found ore: {}'.format(ore_names[index]))
                                      get_ore(ore)
                                      found_ore = True
                           
                        t = time.localtime()
                        current_time = time.strftime("%H:%M:%S", t)
                        
                        if found_ore:
                           print(current_time, ':', "Didn't find any more ores")

                        else:
                           print(current_time, ':', "No ores found")
                        
                        print('---')
                        break
