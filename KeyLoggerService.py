from abc import ABC, abstractmethod
from typing import List
import KeyLoggerAgent


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
  self._active = True

 def stop_logging(self) -> None:
  self._active = False

 def get_logged_keys(self) -> List[str]:
  #מחזיר עותק (ולא את המקורי)
  return list(self._keys)

