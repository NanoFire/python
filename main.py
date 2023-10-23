from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
while(keyboard.is_pressed('q')==False):
    if pyautogui.pixel(1000,500)==(75, 219, 106):
        click(1000,500)