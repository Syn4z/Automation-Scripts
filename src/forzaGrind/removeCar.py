import pyautogui
import time
from pynput import keyboard
import threading


# Define coordinates for actions
coordinates = [
    (942, 682),  # Coordinate 1
    (126, 1001),  # Coordinate 2
]

keyboardController = keyboard.Controller()
cars = int(input("Enter the desired amount of cars: "))
repeatCount = 0

start_time = time.time()
while repeatCount < cars:
    time.sleep(1)

    keyboardController.press(keyboard.Key.enter)
    keyboardController.release(keyboard.Key.enter)
    print("Pressed and released Enter")
    time.sleep(0.3)
    
    # Step 1: Go to coordinate 1 and left click
    pyautogui.moveTo(*coordinates[0], duration=0.05)
    pyautogui.mouseDown(button='left')
    pyautogui.mouseUp(button='left')
    print("Clicked at Coordinate 1")
    time.sleep(0.2)

    # Step 3: Go to coordinate 2 and left click
    pyautogui.moveTo(*coordinates[1], duration=0.05)
    pyautogui.mouseDown(button='left')
    pyautogui.mouseUp(button='left')
    print("Clicked at Coordinate 2")
    repeatCount += 1
    print(f"Car {repeatCount} out of {cars} removed.")

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Total execution time: {elapsed_time:.2f} seconds")