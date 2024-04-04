import pyautogui
import config
import functions
import time
from time import sleep

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

print(current_time, ':', 'Starting cavebot ...\n')
print(current_time, ':', 'Press PageUp to start')
print(current_time, ':', 'Press PageDown to pause\n')
print('---')

while True:
    if functions.loop_status:
        for waypoint in range(8):
            position_in_map = pyautogui.locateOnScreen(config.icons_dir + "icon_{}.png".format(waypoint), confidence=0.9, region=config.REGION_MINIMAP)
            if position_in_map:
                t = time.localtime()
                current_time = time.strftime("%H:%M:%S", t)
                functions.move_and_click(position_in_map)
                print(current_time, ':', 'Going to waypoint: {}'.format(waypoint))
                functions.conjure_rune()
                #eat_food()
                sleep(10) # sleep while walking to next waypoint 
                check_position = pyautogui.locateOnScreen(config.icons_dir + "icon_{}.png".format(waypoint), confidence=0.9, region=config.REGION_MINIMAP)
                if not check_position:
                    t = time.localtime()
                    current_time = time.strftime("%H:%M:%S", t)
                    print(current_time, ':', 'Already on waypoint: {}'.format(waypoint))
                    functions.conjure_rune()
                    while True:
                      functions.conjure_rune()
                      battle = pyautogui.locateOnScreen(config.img_dir + "battle.PNG", confidence=0.9, region=config.REGION_BATTLE)
                      if battle:
                        t = time.localtime()
                        current_time = time.strftime("%H:%M:%S", t)
                        print(current_time, ':', 'Clean battle')
                        functions.open_corpse(config.dead_monster)
                        functions.eat_food_from_corpse(config.food)
                        functions.loot_corpse(config.items)
                        functions.drop_loot_on_floor(config.drop_items, config.bags)
                        print('---')
                        break