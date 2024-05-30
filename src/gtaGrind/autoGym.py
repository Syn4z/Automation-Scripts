import mss
import numpy as np
import cv2
import time
from pynput.keyboard import Controller, Listener, Key
import threading

# Define the target color and threshold
targetColor = (120, 255, 166)
threshold = 15

def displayCommands():
    print("Press F9 to stop the script.")

# Function to check if the target color is present within the specified range
def isTargetColorPresent(frame, targetColor, threshold):
    # Calculate the absolute difference between the frame and target color
    diff = np.abs(frame - targetColor)
    return np.any(np.all(diff <= threshold, axis=-1))

# Main function to continuously scan the screen for the target color
def scanScreen():
    keyboard = Controller()
    with mss.mss() as sct:
        while not stopEvent.is_set():
            monitor = sct.monitors[1]
            keyboard.press('e')
            keyboard.release('e')
            screenshot = np.array(sct.grab(monitor))

            # Convert the color space from BGR to RGB
            frame_rgb = cv2.cvtColor(screenshot, cv2.COLOR_BGR2RGB)

            # Check if the target color is present within the specified range
            if isTargetColorPresent(frame_rgb, targetColor, threshold):
                keyboard.press(Key.space)
                keyboard.release(Key.space)
                time.sleep(0.1)

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
