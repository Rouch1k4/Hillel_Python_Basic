#користувач вводить 5/ти значне число
user_input = int(input("Enter 5-digit number: "))

#ділемо число націло на десяти тисячні, тисячні, соті, десяткі, одиниці, та також завдяки %
ten_thousand = user_input // 10000
thousand = (user_input // 1000) % 10
hundreds = (user_input // 100) % 10
tens = (user_input // 10) % 10
ones = (user_input // 1) % 10

#обертаємо число
reversed_number = ones * 10000 + tens * 1000 + hundreds * 100 + thousand * 10 + ten_thousand
# виводимо на екран
print(reversed_number)
