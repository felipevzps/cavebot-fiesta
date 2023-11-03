import pyautogui
import keyboard
from time import sleep
import threading

REGION_BATTLE = (1730, 581, 190, 200)
REGION_MANA = (1880, 235, 35, 22)
REGION_CHAR = (1240, 404)
REGION_ARROW = (1835, 363)
MINIMAP = (1728, 31, 183, 182)

loop_ativo = False

def iniciar_loop():
    global loop_ativo
    loop_ativo = True

def pausar_loop():
    global loop_ativo
    loop_ativo = False

# Registre as teclas de ativação e pausa
keyboard.add_hotkey('page up', iniciar_loop)
keyboard.add_hotkey('page down', pausar_loop)

# Conjure rune (cast spell saved on F3 hotkey)
def conjure_rune():
  mana = pyautogui.locateOnScreen('fibula_rotworms/images/mana.PNG', confidence=0.6, region=REGION_MANA)
  if mana != None:
    pyautogui.moveTo(REGION_ARROW)
    pyautogui.click(REGION_ARROW, button='left')
    keyboard.press_and_release('F4')

def eat_food():
   pyautogui.moveTo(REGION_ARROW)
   for i in range(5):
    pyautogui.click(REGION_ARROW, button='right')

def attack_next_rotworm():
  
  targeting = pyautogui.locateOnScreen('fibula_rotworms/images/targeting_rotworm.PNG', confidence=0.9, region=REGION_BATTLE)
  full_hp = pyautogui.locateOnScreen('fibula_rotworms/images/full_hp_rotworm.PNG', confidence=0.9, region=REGION_BATTLE)
  
  if full_hp and not targeting:
    sleep(0.5)
    eat_food()
    pyautogui.press('space')

# Move mouse to center of the image
def move(location):
  x,y = pyautogui.center(location)
  pyautogui.moveTo(x, y)

# Click on minimap
def move_and_click(location):
  move(location)
  pyautogui.click()

threadKillRotworm = threading.Thread(target=attack_next_rotworm)

while True:
    if loop_ativo:
      for waypoint in range(25):

        position_in_map = pyautogui.locateOnScreen('fibula_rotworms/icons/icon_{}.png'.format(waypoint), confidence=0.7, region=MINIMAP)

        if position_in_map:
            move_and_click(position_in_map)
            print('going to waypoint: {}'.format(waypoint))
            conjure_rune()
            eat_food()

            if not threadKillRotworm.is_alive():
              threadKillRotworm = threading.Thread(target=attack_next_rotworm)
              threadKillRotworm.start()
            
            threadKillRotworm.join()

            sleep(13)

            check_position = pyautogui.locateOnScreen('fibula_rotworms/icons/icon_{}.png'.format(waypoint), confidence=0.7, region=MINIMAP)
            if not check_position:
                print('already on waypoint: {}'.format(waypoint))
                conjure_rune()

                while True:
                    conjure_rune()
                    if not threadKillRotworm.is_alive():
                      threadKillRotworm = threading.Thread(target=attack_next_rotworm)
                      threadKillRotworm.start()

                    threadKillRotworm.join()
                    
                    battle = pyautogui.locateOnScreen('fibula_rotworms/images/region_battle.PNG', confidence=0.9, region=REGION_BATTLE)
                    if battle:
                      print('battle limpo')
                      print('---')
                      break