from pynput.keyboard import Key, Listener
from datetime import datetime
import threading
import time

kaes = ""
tapping = []

def on_press(key):
    global kaes
    try:
        k = key.char
    except AttributeError:
        k = str(key)

    kaes += k
    tapping.append(k)

    if kaes.endswith("show"):
        print("היסטוריית הקשות:\n" + ''.join(tapping))
        kaes = ""

def on_release(key):
    return False if key == Key.esc else None

def every_5_seconds():
    global kaes
    while True:
        time.sleep(5)
        if kaes.strip():
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"{timestamp} - הקשות אחרונות: {kaes}")
            kaes = ""

threading.Thread(target=every_5_seconds, daemon=True).start()

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()