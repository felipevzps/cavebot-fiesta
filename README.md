# cavebot-fiesta

Automated cavebot in [Darkrest Online](https://darkrest.online/?news).

Features include: `cavebot`, `mana trainer` and `mining`.

This repository also includes [autofishing](https://github.com/felipevzps/cavebot-fiesta/blob/main/autofishing.py) and an [auto trainer](https://github.com/felipevzps/cavebot-fiesta/blob/main/trainer.py) (exclusive for knights, allowing for complete AFK training).

> **Note:** [Mining](https://darkrest-online.gitbook.io/darkrest.online-wiki/gathering-and-crafting/gathering) is a lucrative gathering profession centered around extracting valuable ores from mineral deposits found scattered across the game world.

![](https://github.com/felipevzps/cavebot-fiesta/blob/main/images/cavebot-fiesta.png)

## Requirements

```
pip install pyautogui
pip install keyboard
pip install Pillow
pip install opencv-python
```

## Usage

```python
REGION_BATTLE = (1650, 500, 500, 250)
REGION_MANA = (1852, 237, 59, 21)
REGION_ARROW = (1830, 359)
MINIMAP = (1728, 31, 183, 182)
PICKAXE = (1579, 545)

# Positions of the ores based on character position
right = (1258,393,50,50)
left = (1192,396,50,50)
top = (1225,363,50,50)
bot = (1225,428,50,50)
```

>**Note:** Execute [locateOnScreen.py](https://github.com/felipevzps/cavebot-fiesta/blob/main/locateOnScreen.py) in VSCode to capture coordinates. Hover your mouse over desired locations while the script runs, like Pick position in backpack for `PICKAXE`.
>
>You also have to set the waypoints route in your MINIMAP using [screenshot.py](https://github.com/felipevzps/cavebot-fiesta/blob/main/screenshot.py).

After adding coordinates to [cavebot.py](https://github.com/felipevzps/cavebot-fiesta/blob/main/fibula_rotworms/cavebot.py), run the bot in VSCode, minimize it, and press `p` in-game to start fishing.

![](https://github.com/felipevzps/cavebot-fiesta/blob/main/images/positions.PNG)

## Ingame hotkeys

```
Mana trainer (adori vis // adura vita) = F12
```

## Extra

[cavebot.py](https://github.com/felipevzps/cavebot-fiesta/blob/main/fibula_rotworms/cavebot.py) optimizes performance with advanced multithreading capabilities.

The `threadKillRotworm` manages the `thread_attack_rotworm` function. This parallel approach optimizes the bot's performance, especially when searching for images or executing actions simultaneously, ensuring a more responsive and streamlined experience.

[fibula_rotworms](https://github.com/felipevzps/cavebot-fiesta/tree/main/fibula_rotworms) include complete and free waypoints for fibula rotworms cave and waypoints to collect `silver` and `iron ores`.

## Achievements
> Successfully leveled:
> - Sorcerer [level 50, mlvl 41]
> - Druid [level 50, mlvl 44]
> - Marksman [50, distance 71]
> - Guardian [40, skills 70/70]
>
> - Also collected more than 1700 silver ores and 7000 iron ores
