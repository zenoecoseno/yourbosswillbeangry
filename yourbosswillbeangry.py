from time import sleep
import random
import pyautogui
import time

def move_mouse():
    print("Moving mouse for 30 seconds...")
    # Get the current position of the mouse
    start_x, start_y = pyautogui.position()

    # Move the mouse in a small square to simulate activity
    for _ in range(15):  # Move for 30 seconds
        # Move the mouse slightly in a random direction
        pyautogui.moveTo(start_x + 100, start_y)  # Move right
        time.sleep(0.5)  # Wait for half a second
        pyautogui.moveTo(start_x, start_y + 200)  # Move down
        time.sleep(0.5)  # Wait for half a second
        pyautogui.moveTo(start_x - 300, start_y)  # Move left
        time.sleep(0.5)  # Wait for half a second
        pyautogui.moveTo(start_x, start_y - 200)  # Move up
        time.sleep(0.5)  # Wait for half a second

def press_start():
    # Press start back and forth for n seconds
    work=random.randint(5,15)
    print(f"Pressing the start button for {work} seconds...")
    for _ in range(work):
        pyautogui.press('win')
        sleep(1)

def main():
    while True:

        # press start button
        press_start()
        t = random.randint(100, 200)
        print(f"Mouse movement complete. Waiting for {t} seconds...")
        time.sleep(t)  # random time

if __name__ == "__main__":
    main()