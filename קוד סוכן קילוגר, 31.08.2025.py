#ספריית תאריך
import datetime
#ספריית זמן
import time
#הרצה של קודים במקביל
import threading




# #פותח קובץ וכותב לקובץ
#  with open('keylogger.txt', 'a') as file:
#    file.write(key)

#מדפיס זמנים
def time_print():
 while True:
   now = datetime.datetime.now()
   # with open('keylogger.txt', 'a') as file:
   #   file.write("***"+now.strftime("%Y-%m-%d %H:%M:%S"+"***"+'\n'))
   time.sleep(60)

#
play=threading.Thread(target=time_print, daemon=True)
play.start()


# with Listener(on_press=on_press,on_release=on_release) as listener:
#  listener.join()


