import pyautogui
from time import time
import time

time.sleep(5)
index = 0
while(index<500):
    pyautogui.scroll(-1000)
    time.sleep(0.05)
    index = index + 1
    print(index)    
index = 0
while(index<500):
    pyautogui.scroll(1000)
    time.sleep(0.05)
    index = index + 1
    print(index)

index2 = 0
while(index2<20):
    pyautogui.keyDown('ctrlleft')
    pyautogui.press('r')
    pyautogui.keyUp('ctrlleft')
    index2 = index2 + 1
    time.sleep(0.5)
    print(index2)

print('rewards increased')