import time

import pyautogui as pag

time.sleep(3)
pag.PAUSE = 0

while True:
    time.sleep(0.1)
    if pag.locateOnScreen('blue.png') != None:
        pag.leftClick(619, 697)
    elif pag.locateOnScreen('black.png') != None:
        pag.leftClick(1419, 697)
    else:
        pag.leftClick(1019, 697)
