import pyautogui
import keyboard
from time import sleep

loop_ativo = False  # Inicialmente, o loop está pausado

def iniciar_loop():
    global loop_ativo
    loop_ativo = True

def pausar_loop():
    global loop_ativo
    loop_ativo = False

# Registre as teclas de ativação e pausa
keyboard.add_hotkey('p', iniciar_loop)
keyboard.add_hotkey('k', pausar_loop)

while True:
    if loop_ativo:
        pyautogui.moveTo(1542, 549)
        pyautogui.click(button='right')
        sleep(0.2)
        pyautogui.moveTo(1274, 471)
        pyautogui.click(button='left')