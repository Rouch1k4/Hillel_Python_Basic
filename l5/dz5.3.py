import string

text = input("Type your message : ")

#прибрали зайві символи
clean_text = ''
for char in text:
    if char not in string.punctuation:
        clean_text += char

#створюємо рядок та робимо кожне слово з великої букви
lst = clean_text.split()
capitalized_lst = [word.capitalize() for word in lst]

#створюємо хештег та обєднуємо
hashtag = '#' + ''.join(capitalized_lst)

# перевіряємо довжину та обрізаємо до 140 символів, якщо треба
if len(hashtag) > 140:
    hashtag = hashtag[:140]

# виводимо готовий хештег
print("Hashtag:", hashtag)