import pyautogui
import keyboard
import time
from time import sleep
import sys

REGION_BATTLE = (1746, 362, 172, 164)
REGION_MANA = (1840, 161, 24, 18)
REGION_ARROW = (1592, 654)

slimes_counter = -1
loop_ativo = False  # Inittialy, the loop is off

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

def iniciar_loop():
    global loop_ativo
    loop_ativo = True

def pausar_loop():
    global loop_ativo
    loop_ativo = False

# Register keys to turn on/off the auto fishing
keyboard.add_hotkey('page up', iniciar_loop)
keyboard.add_hotkey('page down', pausar_loop)

# Conjure rune (cast spell saved on F1 hotkey)
def conjure_rune():
  mana = pyautogui.locateOnScreen('cavebot-fiesta/nostalther/images/mana.PNG', confidence=0.8, region=REGION_MANA)
  if mana != None:
    pyautogui.moveTo(REGION_ARROW)
    pyautogui.click(REGION_ARROW, button='left')
    keyboard.press_and_release('F1')

def eat_food():
   pyautogui.moveTo(REGION_ARROW)
   for i in range(5):
    pyautogui.click(REGION_ARROW, button='right')

def attack_next_slime():
  global slimes_counter
  
  t = time.localtime()
  current_time = time.strftime("%H:%M:%S", t)
  
  targeting_slime = pyautogui.locateOnScreen('cavebot-fiesta/nostalther/images/targeting_slime.PNG', confidence=0.9, region=REGION_BATTLE)
  full_hp_slime = pyautogui.locateOnScreen('cavebot-fiesta/nostalther/images/full_hp_slime.PNG', confidence=0.9, region=REGION_BATTLE)
  
  if full_hp_slime and not targeting_slime:
    sleep(2)
    pyautogui.moveTo(1754, 408)
    pyautogui.click(button="left")
    sleep(0.5)
    eat_food() 
    slimes_counter += 1
    print(current_time, ':', 'Slimes killed: {}'.format(slimes_counter))
   
print(current_time, ':', 'Starting trainer!')

while True:
  if loop_ativo:
    attack_next_slime()
    conjure_rune()
    battle = pyautogui.locateOnScreen('cavebot-fiesta/nostalther/images/battle_name.PNG', confidence=0.9, region=(1744,361,65,17))
    if not battle:
       t = time.localtime()
       current_time = time.strftime("%H:%M:%S", t)
       
       print(current_time, ':', "Battle don't found ...")
       print(current_time, ':', "Exiting trainer.")
       sys.exit()