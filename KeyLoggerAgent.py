from pynput.keyboard import Key, KeyCode, Listener


'''התוכנית הזו:
1.עוקבת אחרי ההקשות,והשחרור (באמצעות ספריית פיינפוט)
2.דואגת שהפלט יצא נקי מהספרייה,ללא סימנים מיותרים(באמצעות הגדרת מילון"מקשים מיוחדים", והחלפה שלהם..וכו)
3.שומרת על פקודת עצירה(באמצעות מעקב אחרי ההקשה האחרונה, וההקשה הנוכחית, ומחיקה של ההקשה הקודמת בשחרור ההקשה הנוכחית,בלחיצה על ctrl+q מסתיימת ההרצה)'''


#מילון מקשים מיוחדים
special_keys = {
#    'Key.space': ' ',
#    'Key.enter': '\n',
#    'Key.up': '',
#    'Key.right': ' ',
#    'Key.left': '',
#    'Key.down': '\n',
#    'Key.ctrl_l': '<ctrl >',
#    '\\x03': '<copy >',
#    'Key.backspace': '',
#    '\\x18': '<cut >',
#    '\\x16': '<paste >'
#
}

#הגדרת סט שמכיל תמיד רק הקשה אחרונה
pressed_keys = set()

def on_press(key):
    pressed_keys.add(key)   #הוספת לסט

    # בדיקה: אם קטרול וקיו נלחצים-לעצירה
    if Key.ctrl_l in pressed_keys and (KeyCode.from_char('q')or KeyCode.from_char('/')) in pressed_keys:
        # print("Ctrl + Q pressed - stop listener")
        listener.stop()

    #  "ניקוי,וסידור": הפלט כמפורט להלן:
    key = special_keys.get(str(key), key)  # אם זה זוהה כמקש מיוחד– תחליף אותו. אחרת תשאיר
    key = str(key).replace("'", "")  # מנקה גרשיים
    if not key.isalpha() or key.isnumeric():  # אם לא "אות" או "מספר"
        key = f'{key} '  # מוסיף רווח קדמי

    #יצוא ההקשות!
    return key


def on_release(key):
    pressed_keys.discard(key) # הסרה מהסט-בשחרור

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
