
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

'''מימושים אפשריים לקובץ

1. שמירה לקובץ (על דרך מה שממומש בתוך המחלקה).
class FileWriter(IWriter):
    def send_data(self, data: str, machine_name: str) -> None:
        with open(f"{machine_name}.txt", "a") as f:
            f.write(data + "\n")

2. שמירה ושליחה בפקטת HTTP.
import requests

class NetworkWriter(IWriter):
    def send_data(self, data: str, machine_name: str) -> None:
        url = f"http://{machine_name}/receive"
        response = requests.post(url, json={"data": data})
        response.raise_for_status()
        
3. שמירה במסד נתונים כמו JSON. 
class DatabaseWriter(IWriter):
    def __init__(self, db_connection):
        self.conn = db_connection

    def send_data(self, data: str, machine_name: str) -> None:
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO logs (machine, data) VALUES (?, ?)", (machine_name, data))
        self.conn.commit()
'''