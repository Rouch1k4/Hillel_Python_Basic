from math import remainder

total_number = int(input("Enter a number more then 0 and less then 8640000 : "))
if  0 <= total_number < 8640000:
    # 1 day = 24 * 60 * 60 / 1 hour = 60 * 60 / 1 min = 60
    days, remainder = divmod(total_number, 86400)
    hours, remainder = divmod(remainder,3600)
    minutes, seconds = divmod(remainder,60)

    #перевірка дні чи днів
    if 11 <= days % 100 <= 14:
        day_word = "днів"
    elif days % 10 == 1:
        day_word = "день"
    elif 2 <= days % 10 <= 4:
        day_word = "дні"
    else:
        day_word = "днів"


    time_str =f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"

    #вивід print
    print(f"{days} {day_word} {time_str}")
else:
    print("Invalid operation")