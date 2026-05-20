import pyautogui
import time

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 2

pyautogui.click(437,54)
for i in range(0,2):
    pyautogui.doubleClick(912,272)
    pyautogui.typewrite(str(i))
    pyautogui.scroll(-5000)
    pyautogui.doubleClick(719,948)
    pyautogui.typewrite(str(i))
    pyautogui.press('F5')
    time.sleep(2)
    pyautogui.press('enter')
    pyautogui.scroll(5000)

#1print(pyautogui.position())
