import pyautogui
import keyboard
import time
from time import sleep
import sys

REGION_BATTLE = (1746, 362, 172, 164)
REGION_HEALTH = (1747, 149, 116, 14)
REGION_UH = (1592, 350)
REGION_PLAYER = (1255, 246)
REGION_MANA = (1840, 161, 24, 18)
REGION_FOOD = (1592, 654)

slimes_counter = -1
loop_status = False  # inittialy, the loop is off

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

def start_loop():
    global loop_status
    loop_status = True

def end_loop():
    global loop_status
    loop_status = False

# register keys to turn on/off the trainer
keyboard.add_hotkey('page up', start_loop)
keyboard.add_hotkey('page down', end_loop)

# healing (use uh)
def use_uh():
  health = pyautogui.locateOnScreen('cavebot-fiesta/nostalther/images/health.PNG', confidence=0.8)
  if health != None:
    pyautogui.moveTo(REGION_UH)
    pyautogui.click(REGION_UH, button='right')
    pyautogui.moveTo(REGION_PLAYER)
    pyautogui.click(REGION_PLAYER, button='left')
    print(current_time, ':', 'Using one Ultimate Healing Rune...')

# ml training (cast spell saved on F1 hotkey)
def cast_spell():
  mana = pyautogui.locateOnScreen('cavebot-fiesta/nostalther/images/mana.PNG', confidence=0.8, region=REGION_MANA)
  if mana != None:
    pyautogui.moveTo(REGION_FOOD)
    pyautogui.click(REGION_FOOD, button='left')
    keyboard.press_and_release('F1')

def eat_food():
   pyautogui.moveTo(REGION_FOOD)
   for i in range(3):
     pyautogui.click(REGION_FOOD, button='right')

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
   
print(current_time, ':', 'PRESS PAGE UP TO START THE TRAINER')

while True:
  if loop_status:
    attack_next_slime()
    use_uh()
    cast_spell()
    battle = pyautogui.locateOnScreen('cavebot-fiesta/nostalther/images/battle_name.PNG', confidence=0.9, region=(1744,361,65,17))
    if not battle:
       t = time.localtime()
       current_time = time.strftime("%H:%M:%S", t)
       
       print(current_time, ':', "Battle don't found ...")
       print(current_time, ':', "Exiting trainer.")
       sys.exit()