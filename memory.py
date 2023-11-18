import time
import pyautogui

def check_white_flash():
    coordinates = [(569, 328), (700, 338), (830, 327),  # Replace with the actual 9 pixel coordinates you want to check
                   (825, 461), (700, 471), (556, 474),
                   (561, 617), (701, 600), (804, 598)]

    white_flashes = []

    # Check each pixel
    for coord in coordinates:
        pixel_color = pyautogui.pixel(coord[0], coord[1])
        if pixel_color == (255, 255, 255):  # RGB value for white
            white_flashes.append(coord)

    return white_flashes

def click_at_coordinates(coordinates):
    for coord in coordinates:
        pyautogui.click(coord[0], coord[1])

def main():
    while True:
        white_flash_coordinates = check_white_flash()  # Check for white flashes

        if white_flash_coordinates:
            click_at_coordinates(white_flash_coordinates)  # Click the flashed pixels
            white_flash_coordinates = []  # Clear the list

if __name__ == "__main__":
    main()      
