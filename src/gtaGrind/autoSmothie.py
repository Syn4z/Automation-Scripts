import pyautogui
import time
from pynput import keyboard
import threading

cooking = [
    (1081, 287), 
    (1164, 287),  
    (808, 570),  
    (804, 673)
]

reload = {
    "pos1": (431, 395),
    "pos2": (1029, 405),
    "pos3": (1203, 402),
    "pos4": (872, 396),
    "pos5": (834, 544),
    "pos6": (857, 681)
}

stopScript = threading.Event()
keyboardController = keyboard.Controller()

def displayCommands():
    print("Press F9 to stop the script.")

def perform_actions():
    try:
        while not stopScript.is_set():
            # Run the cooking loop for 5 minutes 30 seconds
            startTime = time.time()
            while time.time() - startTime < 330:
                if stopScript.is_set():
                    return
                for i, pos in enumerate(cooking):
                    if stopScript.is_set():
                        return
                    pyautogui.moveTo(pos[0], pos[1], duration=0.05)
                    if i < 3:
                        pyautogui.rightClick()
                    else:
                        pyautogui.leftClick()
                time.sleep(5.5)
            
            if stopScript.is_set():
                return
            
            keyboardController.press(keyboard.Key.esc)
            time.sleep(0.1)
            keyboardController.release(keyboard.Key.esc)
            time.sleep(1)
            keyboardController.press('q')
            time.sleep(0.1)
            keyboardController.release('q')
            time.sleep(1)
            keyboardController.press('e')
            time.sleep(0.1)
            keyboardController.release('e')
            time.sleep(1)
            pyautogui.moveTo(*reload["pos1"], duration=1.0)
            pyautogui.mouseDown(button='left')
            pyautogui.moveTo(*reload["pos2"], duration=1.0)
            pyautogui.mouseUp(button='left')
            pyautogui.moveTo(*reload["pos3"], duration=1.0)
            keyboardController.press(keyboard.Key.ctrl)
            pyautogui.mouseDown(button='left')
            pyautogui.moveTo(*reload["pos4"], duration=1.0)
            pyautogui.mouseUp(button='left')
            keyboardController.release(keyboard.Key.ctrl)
            pyautogui.moveTo(*reload["pos5"], duration=1.0)
            pyautogui.click(button='left')
            keyboardController.press(keyboard.Key.backspace)
            keyboardController.release(keyboard.Key.backspace)
            keyboardController.type('49')
            pyautogui.moveTo(*reload["pos6"], duration=1.0)
            pyautogui.click(button='left')
            keyboardController.press(keyboard.Key.esc)
            time.sleep(0.1)
            keyboardController.release(keyboard.Key.esc)
            time.sleep(1)
            keyboardController.press('q')
            time.sleep(0.1)
            keyboardController.release('q')
            time.sleep(1)
            keyboardController.press('e')
            time.sleep(0.1)
            keyboardController.release('e')
            time.sleep(1)

    except Exception as e:
        print(f"An error occurred: {e}")

def on_press(key):
    if key == keyboard.Key.f9:
        stopScript.set()
        return False

def start_listener():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

displayCommands()
moveThread = threading.Thread(target=perform_actions)
moveThread.start()
listenerThread = threading.Thread(target=start_listener)
listenerThread.start()
moveThread.join()
listenerThread.join()
print("Script stopped.")
