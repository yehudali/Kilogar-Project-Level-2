
from abc import ABC, abstractmethod
import datetime
import time
class IWriter(ABC):
    @abstractmethod
    def send_data(self, data: str, machine_name: str) -> None:
        pass

    def time_print():
     while True:
       now = datetime.datetime.now()
       with open('keylogger.txt', 'a') as file:
         file.write("***"+now.strftime("%Y-%m-%d %H:%M:%S"+"***"+'\n'))
       time.sleep(60)
IWriter.time_print()