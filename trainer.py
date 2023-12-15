import pyautogui
import keyboard
import time
from time import sleep
import sys

REGION_BATTLE = (1726, 582, 194, 113)
REGION_MANA = (1852, 237, 59, 21)
REGION_CHAR = (1240, 404)
REGION_ARROW = (1835, 363)

slimes_counter = -1
loop_ativo = False  # Inicialmente, o loop está pausado

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

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
  mana = pyautogui.locateOnScreen('images/mana_2.PNG', confidence=0.8, region=REGION_MANA)
  if mana != None:
    pyautogui.moveTo(REGION_ARROW)
    pyautogui.click(REGION_ARROW, button='left')
    keyboard.press_and_release('F3')

def eat_food():
   pyautogui.moveTo(REGION_ARROW)
   for i in range(5):
    pyautogui.click(REGION_ARROW, button='right')

def attack_next_slime():
  global slimes_counter
  
  t = time.localtime()
  current_time = time.strftime("%H:%M:%S", t)
  
  targeting_slime = pyautogui.locateOnScreen('trainer/targeting_slime.PNG', confidence=0.9, region=REGION_BATTLE)
  full_hp_slime = pyautogui.locateOnScreen('trainer/full_hp_slime.PNG', confidence=0.9, region=REGION_BATTLE)
  
  if full_hp_slime and not targeting_slime:
    sleep(2)
    eat_food()
    pyautogui.press('numlock')
    slimes_counter += 1
    print(current_time, ':', 'Slimes killed: {}'.format(slimes_counter))
   
print(current_time, ':', 'Starting trainer!')

while True:
  if loop_ativo:
    attack_next_slime()
    conjure_rune()
    battle = pyautogui.locateOnScreen('trainer/battle.PNG', confidence=0.9, region=REGION_BATTLE)
    if not battle:
       t = time.localtime()
       current_time = time.strftime("%H:%M:%S", t)
       
       print(current_time, ':', "Battle don't found ...")
       print(current_time, ':', "Exiting trainer.")
       sys.exit()