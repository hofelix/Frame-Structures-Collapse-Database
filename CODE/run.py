import pyautogui
import time
import random

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 2


for i in range(0,1000):
    pyautogui.click(270,1067)
    pyautogui.click(278,288)
    pyautogui.typewrite(str(random.uniform(0.5, 1.5)))
    pyautogui.moveTo(138,289,duration=1)
    pyautogui.press('enter')
    pyautogui.click(138,289)
    pyautogui.typewrite(str(random.uniform(0.5, 1.5)))
    pyautogui.moveTo(272,308,duration=1)
    pyautogui.press('enter')
    pyautogui.click(272,308)
    pyautogui.typewrite(str(random.uniform(0, 150)))
    pyautogui.moveTo(205,201,duration=1)
    pyautogui.press('enter')
    pyautogui.click(205,201)
    pyautogui.moveTo(159,420,duration=1)
    pyautogui.click(159,420)
    pyautogui.moveTo(191,876)
    time.sleep(20)
    pyautogui.click(191,876)
    pyautogui.hotkey('winleft','printscreen')
    pyautogui.click(311,1059)
    pyautogui.click(1367,70)
    pyautogui.doubleClick(1608,938)
    pyautogui.typewrite(str(i))
    pyautogui.press('F5')
    time.sleep(2)
    pyautogui.press('enter')


#pyautogui.typewrite(str(random.uniform(2.2, 6)))
#print(pyautogui.position())
#print(random.uniform(2.2, 6))
