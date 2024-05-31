import mss
import numpy as np
import cv2
import time
from pynput.keyboard import Controller, Listener, Key
from pynput.mouse import Controller as MouseController, Button
import threading

# Define the target color and threshold
targetColor = (120, 255, 166)
threshold = 15

# Define the coordinates for the cursor to move to
cursorPosition = (1494, 381)  # Adjust these coordinates as needed

# Define the main loop interval
mainLoopInterval = 30 * 60  # 30 minutes in seconds

def displayCommands():
    print("Press F9 to stop the script.")

# Function to check if the target color is present within the specified range
def isTargetColorPresent(frame, targetColor, threshold):
    # Calculate the absolute difference between the frame and target color
    diff = np.abs(frame - targetColor)
    return np.any(np.all(diff <= threshold, axis=-1))

# Function to perform the secondary loop actions
def performActions():
    keyboard = Controller()
    mouse = MouseController()
    
    for _ in range(5):
        keyboard.press('i')
        keyboard.release('i')
        mouse.position = cursorPosition
        mouse.click(Button.right)
        time.sleep(7)

# Main function to continuously scan the screen for the target color
def scanScreen():
    keyboard = Controller()
    with mss.mss() as sct:
        startTime = time.time()
        while not stopEvent.is_set():
            monitor = sct.monitors[1]
            keyboard.press('e')
            keyboard.release('e')
            screenshot = np.array(sct.grab(monitor))

            # Convert the color space from BGR to RGB
            frameRgb = cv2.cvtColor(screenshot, cv2.COLOR_BGR2RGB)

            # Check if the target color is present within the specified range
            if isTargetColorPresent(frameRgb, targetColor, threshold):
                keyboard.press(Key.space)
                keyboard.release(Key.space)
                time.sleep(0.1)

            # Check if 30 minutes have passed
            elapsedTime = time.time() - startTime
            if elapsedTime >= mainLoopInterval:
                performActions()
                startTime = time.time()

def onPress(key):
    if key == Key.f9:
        stopEvent.set()
        return False

def startListener():
    with Listener(on_press=onPress) as listener:
        listener.join()

displayCommands()
stopEvent = threading.Event()
scanThread = threading.Thread(target=scanScreen)
scanThread.start()
listenerThread = threading.Thread(target=startListener)
listenerThread.start()
scanThread.join()
listenerThread.join()
print("Script stopped.")
