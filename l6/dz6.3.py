user_num = int(input("enter num: "))

while user_num > 9:
    product = 1
    #розділяємо число користувача на окремі числи
    for digit in str(user_num):
        product *= int(digit)
    user_num = product
print(user_num)