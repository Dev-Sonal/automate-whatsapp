import pyautogui
import time
time.sleep(4)
count=0
while count<=100: #no of times to display message
    pyautogui.typewrite(" hello ")
    pyautogui.press("enter")
    count=count+1
