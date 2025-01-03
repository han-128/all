import keyboard
import time

i = 10
d = 1

time.sleep(5)

while i > 1:
    time.sleep(d)
    keyboard.press("ctrl+f")

    time.sleep(d)
    keyboard.press("left")
    time.sleep(d)
    keyboard.press("left")
    time.sleep(d)
    keyboard.press("enter")
    time.sleep(d)
    keyboard.press("down")
    time.sleep(d)
    keyboard.press("down")
    time.sleep(d)
    keyboard.press("enter")
    time.sleep(d)
    keyboard.press("tab")
    time.sleep(d)
    keyboard.press("down")
    time.sleep(d)
    keyboard.press("enter")
    i = i - 1