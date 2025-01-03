import pyautogui as pag
import time as t
import keyboard


i = 420
d = 0.2

t.sleep(2)

while i > 0:

    t.sleep(1)

    locMenu = pag.locateOnScreen('menu.png')
    poinMenu = pag.center(locMenu)
    pag.click(poinMenu[0], poinMenu[1], 1, 1, 'left')

    #t.sleep(d)

    locDow = pag.locateOnScreen('download.png')
    poinDow = pag.center(locDow)
    pag.click(poinDow[0], poinDow[1], 1, 1, 'left')
    pag.click(poinDow[0], poinDow[1], 1, 1, 'left')


    #t.sleep(d)

    locList = pag.locateOnScreen('list.png')
    poinList = pag.center(locList)
    pag.click(poinList[0], poinList[1], 1, 1, 'left')

    #t.sleep(d)

    keyboard.press("ctrl+f")

    i = i - 1