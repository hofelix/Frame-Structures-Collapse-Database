import pyautogui
import time

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 2

pyautogui.click(168,1064)
pyautogui.click(398,220)

for i in range(0,1000):
    pyautogui.press('F2')
    pyautogui.typewrite(str(i))
    pyautogui.press('enter')
    pyautogui.press('down')

#print(pyautogui.position())
