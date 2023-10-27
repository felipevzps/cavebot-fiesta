from time import sleep
import pyautogui

mana = (1880, 235) 

while True:
    mana = pyautogui.locateOnScreen('images/mana.PNG', confidence=0.7)
    battle = pyautogui.locateOnScreen('images/region_battle.PNG', confidence=0.9)
    attacking = pyautogui.locateOnScreen('images/attacking_troll.PNG', confidence=0.9)
    #print(mana)
    #print(battle)
    #print(attacking)
    print(pyautogui.position())