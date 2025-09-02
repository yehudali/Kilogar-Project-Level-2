import chek
import time



while chek.listener.running:
    # להריץ קוד במקביל אם צריך
    time.sleep(0.01)
chek.listener.start()