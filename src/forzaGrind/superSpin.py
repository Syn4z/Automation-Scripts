import pyautogui
import time
from pynput import keyboard
import threading

# Define coordinates for actions
coordinates = [
    (967, 556),  # Coordinate 1
    (953, 731),  # Coordinate 2
    (494, 391),  # Coordinate 3
    (1586, 640)  # Coordinate 4
]

stopScript = threading.Event()
keyboardController = keyboard.Controller()
cars = int(input("Enter the desired amount of cars: "))
repeatCount = 0

def displayCommands():
    print("Press F9 to stop the script.")

def safe_sleep(duration):
    """Sleep in short intervals, checking for the stop signal."""
    interval = 0.1  # Check every 0.1 seconds
    elapsed = 0
    while elapsed < duration:
        if stopScript.is_set():
            return
        time.sleep(interval)
        elapsed += interval

def perform_actions(repeatCount, cars):
    while repeatCount < cars:
        safe_sleep(2)
        
        # Step 1: Go to coordinate 1 and left click
        pyautogui.moveTo(*coordinates[0], duration=0.05)
        pyautogui.mouseDown(button='left')
        pyautogui.mouseUp(button='left')
        print("Clicked at Coordinate 1")
        safe_sleep(0.5)

        # Step 2: Press and release 'X'
        keyboardController.press('x')
        keyboardController.release('x')
        print("Pressed and released 'X'")
        safe_sleep(1)

        # Step 3: Go to coordinate 2 and left click
        pyautogui.moveTo(*coordinates[1], duration=0.05)
        pyautogui.mouseDown(button='left')
        pyautogui.mouseUp(button='left')
        print("Clicked at Coordinate 2")
        safe_sleep(1)

        # Step 4: Press and release left arrow
        keyboardController.press(keyboard.Key.left)
        keyboardController.release(keyboard.Key.left)
        print("Pressed and released Left Arrow")
        safe_sleep(0.5)

        # Step 5: Press and release Enter (twice)
        keyboardController.press(keyboard.Key.enter)
        keyboardController.release(keyboard.Key.enter)
        print("Pressed and released Enter")
        safe_sleep(1)
        keyboardController.press(keyboard.Key.enter)
        keyboardController.release(keyboard.Key.enter)
        print("Pressed and released Enter again")
        safe_sleep(9)

        # Step 6: Press and release ESC
        keyboardController.press(keyboard.Key.esc)
        keyboardController.release(keyboard.Key.esc)
        print("Pressed and released ESC")
        safe_sleep(1)

        # Step 7: Go to coordinate 3 and left click
        pyautogui.moveTo(*coordinates[2], duration=0.05)
        pyautogui.mouseDown(button='left')
        pyautogui.mouseUp(button='left')
        print("Clicked at Coordinate 3")
        safe_sleep(2)

        # Step 8: Go to coordinate 4 and left click
        pyautogui.moveTo(*coordinates[3], duration=0.05)
        pyautogui.mouseDown(button='left')
        pyautogui.mouseUp(button='left')
        print("Clicked at Coordinate 4")
        safe_sleep(1.5)

        # Step 9: Press and release Enter
        keyboardController.press(keyboard.Key.enter)
        keyboardController.release(keyboard.Key.enter)
        print("Pressed and released Enter")
        safe_sleep(1.5)
        keyboardController.press(keyboard.Key.right)
        keyboardController.release(keyboard.Key.right)
        print("Pressed and released Right Arrow")
        safe_sleep(0.5)
        keyboardController.press(keyboard.Key.enter)
        keyboardController.release(keyboard.Key.enter)
        print("Pressed and released Enter")
        safe_sleep(1.5)
        keyboardController.press(keyboard.Key.right)
        keyboardController.release(keyboard.Key.right)
        print("Pressed and released Right Arrow")
        safe_sleep(0.5)
        keyboardController.press(keyboard.Key.enter)
        keyboardController.release(keyboard.Key.enter)
        print("Pressed and released Enter")
        safe_sleep(1.5)
        keyboardController.press(keyboard.Key.up)
        keyboardController.release(keyboard.Key.up)
        print("Pressed and released Up Arrow")
        safe_sleep(0.5)
        keyboardController.press(keyboard.Key.enter)
        keyboardController.release(keyboard.Key.enter)
        print("Pressed and released Enter")
        safe_sleep(1.5)
        keyboardController.press(keyboard.Key.right)
        keyboardController.release(keyboard.Key.right)
        print("Pressed and released Right Arrow")
        safe_sleep(0.5)
        keyboardController.press(keyboard.Key.enter)
        keyboardController.release(keyboard.Key.enter)
        print("Pressed and released Enter")
        safe_sleep(1.5)

        keyboardController.press(keyboard.Key.esc)
        keyboardController.release(keyboard.Key.esc)
        safe_sleep(1)
        keyboardController.press(keyboard.Key.esc)
        keyboardController.release(keyboard.Key.esc)

        print("Sequence completed, restarting...")
        repeatCount += 1
        safe_sleep(0.5)
    stopScript.set()   

def on_press(key):
    if key == keyboard.Key.f9:
        stopScript.set()
        return False

def start_listener():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# Display command instructions
displayCommands()

# Start the threads
actionThread = threading.Thread(target=perform_actions(repeatCount, cars))
actionThread.start()

listenerThread = threading.Thread(target=start_listener)
listenerThread.start()

# Wait for threads to finish
actionThread.join()
listenerThread.join()
print("Script stopped.")
