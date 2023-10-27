from time import sleep
import pyautogui
import keyboard

pyautogui.PAUSE = 0.3

REGION_LOOT = (1726, 853, 189, 184)
REGION_TROLL = (1194, 363, 97, 102)
REGION_BATTLE = (1725, 582, 194, 113)
FIRST_MONSTER_BATTLE = (1738, 636)
MINIMAP = (1728, 31, 183, 182)
KNIFE = (1546, 551)
MANA = (1880, 235, 35, 22)

def collect_gold():
    for i in range(3):
       gold = pyautogui.locateOnScreen('images/goldcoin_{}.png'.format(i), confidence=0.9, region=REGION_LOOT)
       if gold != None: 
        print(gold)
        pyautogui.moveTo(gold)
        pyautogui.dragTo(1739, 760, button='left', duration=0.2)
        keyboard.press_and_release('enter')
        sleep(0.5)

def eat_meat():
    meat = pyautogui.locateOnScreen('images/meat.PNG', confidence=0.8, region=REGION_LOOT)
    if meat != None: 
        print(meat)
        pyautogui.moveTo(meat)
        pyautogui.click(button='right')

def collect_perk():
  perk = pyautogui.locateOnScreen('images/perk.PNG', confidence=0.9, region=REGION_LOOT)
  if perk != None: 
    print(perk)
    pyautogui.moveTo(perk)
    pyautogui.dragTo(1739, 760, button='left', duration=0.2)
    keyboard.press_and_release('enter')
    sleep(0.5)
  
def move(location):
  x,y = pyautogui.center(location)
  pyautogui.moveTo(x, y)

def get_troll(location):
  if location != None:
    sleep(0.5)
    move(location)
    pyautogui.click(button='right')
    sleep(1)
    collect_gold()
    collect_perk()
    eat_meat()

def skin_corpse(location):
    if location != None:
        sleep(0.5)
        pyautogui.moveTo(KNIFE)
        pyautogui.click(KNIFE, button='right')
        sleep(0.5)
        move(location)
        pyautogui.click(button='left')

def attack_monster_on_battle():
   attacking = pyautogui.locateOnScreen('images/attacking_troll.PNG', confidence=0.9)
   if attacking == None:
      pyautogui.moveTo(FIRST_MONSTER_BATTLE)
      sleep(0.2)
      pyautogui.click(button='left')

# Conjure rune (cast spell saved on F3 hotkey)
def conjure_rune():
  mana = pyautogui.locateOnScreen('images/mana.PNG', confidence=0.6, region=MANA)
  if mana != None:
    keyboard.press_and_release('F3')
  
# Click on minimap
def move_and_click(location):
  move(location)
  pyautogui.click()
  
#''' working for taking loot from dead troll corpses (use to test autoloot)
while True:
    attack_monster_on_battle()
    dead_troll = pyautogui.locateOnScreen('images/dead_troll.PNG', confidence=0.7, region=REGION_TROLL)
    if dead_troll != None:
        sleep(2)
        get_troll(dead_troll)
        skin_corpse(dead_troll)
#'''

#keyboard.wait('p')
'''
while True:
    for waypoint in range(9):

      position_in_map = pyautogui.locateOnScreen('icons/icon_{}.png'.format(waypoint), confidence=0.7, region=MINIMAP)
      print('waypoint: {}'.format(waypoint))

      if position_in_map:
          move_and_click(position_in_map)
          sleep(8)
          conjure_rune()
          sleep(0.5)

          check_position = pyautogui.locateOnScreen('icons/icon_{}.png'.format(waypoint), confidence=0.7, region=MINIMAP)
          if not check_position:
              while True:
                  attacking = pyautogui.locateOnScreen('images/attacking_troll.PNG', confidence=0.6)
                  pyautogui.moveTo(1240, 418)
                  if not attacking:
                    attack_monster_on_battle()
                    dead_troll = pyautogui.locateOnScreen('images/dead_troll.PNG', confidence=0.8, region=REGION_TROLL)
                    if dead_troll:
                        sleep(2)
                        get_troll(dead_troll)
                        skin_corpse(dead_troll)
                    else:
                        battle = pyautogui.locateOnScreen('images/region_battle.PNG', confidence=0.9, region=REGION_BATTLE)
                        if battle:
                            break
'''






