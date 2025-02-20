import pyautogui
import keyboard
import time
from time import sleep
import sys
import numpy as np

REGION_BATTLE = (1746, 362, 172, 164)
REGION_HEALTH = (1774, 156, 81, 5)
REGION_UH = (1592, 350)
REGION_PLAYER = (1255, 246)
REGION_MANA = (1773, 171, 82, 3)
REGION_FOOD = (1592, 654)

slimes_counter = -1
loop_status = False  # inittialy, the loop is off

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

def start_loop():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    global loop_status
    loop_status = True
    print(current_time, ':', 'STARTED!')

def end_loop():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    global loop_status
    loop_status = False
    print(current_time, ':', 'PAUSED!')
    print(current_time, ':', 'PRESS PAGE UP TO RESUME')

# register keys to turn on/off the trainer
keyboard.add_hotkey('page up', start_loop)
keyboard.add_hotkey('page down', end_loop)

def get_bar_percentage(region, threshold=0.45):
    screenshot = pyautogui.screenshot(region=region).convert("L")  # gray scale
    arr = np.array(screenshot)
    bw = arr >= int(threshold * 255)
    height, width = bw.shape
    fill_width = 0
    
    for col in range(width):
        col_data = bw[:, col]
        col_mean = np.mean(col_data)
        
        if col_mean > 0.5:
            fill_width += 1
        else:
            break
    
    percentage = (fill_width / width) * 100
    return percentage

# healing (use uh)
def use_uh():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    health_percentage = get_bar_percentage(REGION_HEALTH, threshold=0.45)

    if health_percentage > 60:
        return

    print(f"Vida atual: {health_percentage:.1f}%")
    pyautogui.moveTo(REGION_UH)
    pyautogui.click(REGION_UH, button='right')
    pyautogui.moveTo(REGION_PLAYER)
    pyautogui.click(REGION_PLAYER, button='left')
    print(current_time, ':', 'Using one Ultimate Healing Rune...')  

# ml training (cast spell saved on F1 hotkey)
def cast_spell():
  mana_percentage = get_bar_percentage(REGION_MANA, threshold=0.45)
  if mana_percentage < 70:
    return
  
  print(f"Mana atual: {mana_percentage:.1f}%")
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