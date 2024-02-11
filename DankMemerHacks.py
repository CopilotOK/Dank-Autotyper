import pyautogui
import time
import keyboard



def autoDank():
    while True:
        pyautogui.click(x=1335, y=963)
        pyautogui.write("/beg")
        time.sleep(3)
        pyautogui.click(x=906, y=816)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.click(x=1335, y=963)
        pyautogui.write("/hunt")
        time.sleep(3)
        pyautogui.click(x=785, y=400)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.write("/fish")
        time.sleep(3)
        pyautogui.click(x=744, y=472)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.write("/dig")
        time.sleep(3)
        pyautogui.click(x=684, y=876)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.click(x=1335, y=963)
        pyautogui.write("/postmemes")
        time.sleep(4)
        pyautogui.click(x=645, y=878)
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(3)
        pyautogui.click(x=669, y=760)
        time.sleep(1.5)
        pyautogui.click(x=708, y=720)
        time.sleep(1.5)
        pyautogui.click(x=681, y=809)
        time.sleep(1.5)
        pyautogui.click(x=602, y=733)
        time.sleep(1.5)
        pyautogui.click(x=512, y=872)
        time.sleep(3)  
        x = keyboard.read_key()
        if x=="esc":
            exit()



confirmation = pyautogui.confirm(text='Are you sure want to start this autotyper?\nTo stop anytime, press escape',
title='Dank Memer Hacks', buttons=['Yes','Cancel'])
if confirmation=='Yes':
    autoDank()
else:
    exit()
# pyautogui.click(x=1335, y=963)
# x = pyautogui.position()
# print(x)