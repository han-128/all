import mouse
import time
import keyboard

click = False

time.sleep(3)

def set_clicker():
    global click
    if click:
        click = False
        print('кликер  отключен')
    else:
        click = True
        print('кликер включен')

while True:
    keyboard.press('w')
    time.sleep(1)
    keyboard.release('w')

    time.sleep(5)
    keyboard.press('a')
    time.sleep(1)
    keyboard.release('a')

    time.sleep(5)
    keyboard.press('s')
    time.sleep(1)
    keyboard.release('s')

    time.sleep(5)
    keyboard.press('d')
    time.sleep(1)
    keyboard.release('d')
    time.sleep(5)

keyboard.add_hotkey('z', set_clicker)

while True:
    mouse.click(button = 'left')
    time.sleep(0.1)

    keyboard.press('w')
    time.sleep(1)
    keyboard.release('w')

    time.sleep(5)
    keyboard.press('a')
    time.sleep(1)
    keyboard.release('a')

    time.sleep(5)
    keyboard.press('s')
    time.sleep(1)
    keyboard.release('s')

    time.sleep(5)
    keyboard.press('d')
    time.sleep(1)
    keyboard.release('d')
    time.sleep(5)

