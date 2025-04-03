import string
import keyword
text = input("Type your variable : ")
if not text:
#перевірка умов які були в завданні
    print(False)
elif text[0].isdigit():
    print(False)
elif not text.islower():
    print(False)
elif ' ' in text:
    print(False)
elif any(char in string.punctuation and char != '_' for char in text):
    print(False)
elif text in keyword.kwlist:
    print(False)
else:
    print(True)
