import pyautogui
from PIL import ImageGrab
import time

def get_mouse_pixel():
    x, y = pyautogui.position()
    screenshot = ImageGrab.grab()
    pixel_color = screenshot.getpixel((x, y))
    return pixel_color

while True:
    pixel_color = get_mouse_pixel()
    print(f"Pixel color at mouse position: {pixel_color}")
    