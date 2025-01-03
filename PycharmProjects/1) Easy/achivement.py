import keyboard
import time

i = 200

time.sleep(5)

while i > 1:
    time.sleep(0.01)
    keyboard.press("space")
    time.sleep(0.01)
    keyboard.press('down')
    i = i - 1