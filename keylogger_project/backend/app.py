import requests

url = "http://127.0.0.1:5000/api/upload"
payload = {
    "machine": "PC-10",
    "data": "היי, זה יהודה"
}

payload = {
    "machine": "PC-1",
    "data": "בוקר טוב"
}

payload = {
    "machine": "PC-2",
    "data": "הבוקר לא אכלתי קרונפלקס"
}


payload = {
    "machine": "PC-3",
    "data": "במקום זה הכנתי חביתה"
}


payload = {
    "machine": "PC-4",
    "data": "אז זהו זה היה הסיפור שלי להבוקר"
}


payload = {
    "machine": "PC-5",
    "data": "נשתמע"
}
response = requests.post(url, json=payload)
print(response.status_code)
print(response.json())
