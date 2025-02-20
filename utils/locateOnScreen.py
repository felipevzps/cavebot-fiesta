import pyautogui
from time import sleep

REGION_HEALTH = (1747, 149, 116, 14)

health_img = 'cavebot-fiesta/nostalther/images/health.PNG'

# Function to locate the (left, top) position of each image
while True:
    health = pyautogui.locateOnScreen(health_img, confidence=0.8)  
    # Mouse position
    print(pyautogui.position())
    print(health)