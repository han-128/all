import keyboard
import pyautogui as gui
from time import sleep

input('Нажмите enter, чтобы начать работу')
sleep(4)
gui.click(700,500)
for i in range(10):
    keyboard.press('d')
    sleep(0.1)
    keyboard.press('a')
    sleep(0.1)

