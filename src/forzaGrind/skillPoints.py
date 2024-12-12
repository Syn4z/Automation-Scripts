from pynput.keyboard import Controller, Listener, Key
import threading
import time

keyboard = Controller()
stopEvent = threading.Event()

def displayCommands():
    print("Press F9 to stop the script.")

def performSequence():
    while not stopEvent.is_set():
        time.sleep(2)
        # Step 1: Press and release Enter
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        print("Pressed and released 'Enter'")
        time.sleep(5)  # Wait for 6 seconds

        # Step 2: Press and hold 'W' for 18 seconds, then release
        keyboard.press('w')
        print("Pressed and holding 'W'")
        time.sleep(18)  # Hold 'W' for 18 seconds
        keyboard.release('w')
        print("Released 'W'")

        # Step 3: Wait for 10 seconds
        time.sleep(10)

        # Step 4: Press and release 'X'
        keyboard.press('x')
        keyboard.release('x')
        print("Pressed and released 'X'")
        time.sleep(1)

        # Step 5: Press and release 'Enter'
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        print("Pressed and released 'Enter'")

        # Step 6: Wait for 5 seconds before looping
        time.sleep(6)

def onPress(key):
    if key == Key.f9:
        stopEvent.set()
        return False

def startListener():
    with Listener(on_press=onPress) as listener:
        listener.join()

# Display command instructions
displayCommands()

# Start the threads
sequenceThread = threading.Thread(target=performSequence)
sequenceThread.start()

listenerThread = threading.Thread(target=startListener)
listenerThread.start()

# Wait for threads to finish
sequenceThread.join()
listenerThread.join()
print("Script stopped.")
