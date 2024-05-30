from pynput.keyboard import Controller, Listener, Key
import threading
import time
import random

keyboard = Controller()
stopEvent = threading.Event()

def displayCommands():
    print("Press F9 to stop the script.")

def pressKeys():
    while not stopEvent.is_set():
        key = random.choice(['a', 'w', 's', 'd'])
        interval = random.uniform(0.5, 3.0)
        press_duration = random.uniform(0.1, interval)
        keyboard.press(key)
        time.sleep(press_duration)
        keyboard.release(key)
        time.sleep(interval - press_duration)

def onPress(key):
    if key == Key.f9:
        stopEvent.set()
        return False

def startListener():
    with Listener(on_press=onPress) as listener:
        listener.join()

displayCommands()
pressKeyThread = threading.Thread(target=pressKeys)
pressKeyThread.start()
listenerThread = threading.Thread(target=startListener)
listenerThread.start()
pressKeyThread.join()
listenerThread.join()
print("Script stopped.")
