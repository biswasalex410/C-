import pyautogui
import time
message = 100
while message > 0:
    time.sleep(0)
    pyautogui.typewrite('Hi BC!!!')
    pyautogui.press('enter')
    message = message - 1