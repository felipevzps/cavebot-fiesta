# cavebot-fiesta

Automated cavebot for tibia 7.4

Features include: `cavebot 100% AFK`, `auto looter`, `auto attacker`, `rune maker`, `waypoints maker`, `drop food and items on the floor` and `mining`.

This repository also includes [autofishing](https://github.com/felipevzps/cavebot-fiesta/blob/main/utils/autofishing.py) and an [auto trainer](https://github.com/felipevzps/cavebot-fiesta/blob/main/utils/trainer.py) (exclusive for knights, allowing for 100% AFK training).

> **Note:** [Mining (darkrest only)](https://darkrest-online.gitbook.io/darkrest.online-wiki/gathering-and-crafting/gathering) is a lucrative gathering profession centered around extracting valuable ores from mineral deposits found scattered across the game world.

![](https://github.com/felipevzps/cavebot-fiesta/blob/main/cavebot-fiesta/cavebot-fiesta.gif)

## Requirements

```
pip install pyautogui
pip install keyboard
pip install Pillow
pip install opencv-python
```

## Usage

Before running, set up the [configuration file](https://github.com/felipevzps/cavebot-fiesta/blob/main/cavebot-fiesta/config.py).

>**Note:** Execute [locateOnScreen.py](https://github.com/felipevzps/cavebot-fiesta/blob/main/utils/locateOnScreen.py) to capture coordinates. Hover your mouse over desired locations while the script runs, and save the X,Y coords in the configuration file.
>
>You also have to set the waypoints route in your MINIMAP using [screenshot.py](https://github.com/felipevzps/cavebot-fiesta/blob/main/utils/screenshot.py).

Then, run the bot in VSCode, minimize it, and press `PageUp` in-game to start the cavebot.

![](https://github.com/felipevzps/cavebot-fiesta/blob/main/cavebot-fiesta/darkrest/images/positions.PNG)

## Ingame hotkeys

```
Mana trainer (adori vis // adura vita) = F3
```

## Extra

[functions.py](https://github.com/felipevzps/cavebot-fiesta/blob/main/cavebot-fiesta/functions.py) optimizes performance with multithreading.

The `threadKillMonster` manages the `attack_next_monster` function. This parallel approach optimizes the bot's performance, especially when searching for images or executing actions simultaneously.
