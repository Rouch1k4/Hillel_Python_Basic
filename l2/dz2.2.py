#користувач вводить 5/ти значне число
user_input = int(input("Enter 5-digit number: "))

#ділемо число націло на десяти тисячні, тисячні, соті, десяткі, одиниці, та також завдяки %
ten_thousand = user_input // 10000
thousand = (user_input // 1000) % 10
hundreds = (user_input // 100) % 10
tens = (user_input // 10) % 10
ones = (user_input // 1) % 10
#виводимо на екран завдяки print та міняємо змінні місцями в протилежну сторону
print(ones, tens, hundreds, thousand, ten_thousand)
