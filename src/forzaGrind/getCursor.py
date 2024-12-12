import pyautogui
from pynput.keyboard import Listener, Key
import threading

stopEvent = threading.Event()
counter = 0

def displayCommands():
    print("Commands:")
    print("Press F8 to print the current mouse coordinates.")
    print("Press F9 to stop the script.")

def onPress(key):
    global counter
    if key == Key.f9:
        stopEvent.set()
        return False
    elif key == Key.f8:
        x, y = pyautogui.position()
        counter += 1
        print(f'\n{counter}: X: {x}, Y: {y}')

def startListener():
    with Listener(on_press=onPress) as listener:
        listener.join()

displayCommands()
# Start the listener in a separate thread
listenerThread = threading.Thread(target=startListener)
listenerThread.start()
# Wait for the listener thread to finish
listenerThread.join()
print("Script stopped.")
