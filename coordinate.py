import pyautogui
import time 
try:
    while True:
        x, y = pyautogui.position()  # Get the mouse coordinates
        print(f'Mouse coordinates: x={x}, y={y}')
        time.sleep(1)
except KeyboardInterrupt:
    print('\nExiting...')