#користувач вводить число
user_input = int(input("Enter a number 4 digit number: "))
#ділемо число націло на тисячні, соті десяткі одиниці та також завдяки %
thousand = user_input // 1000
hundreds = (user_input // 100) % 10
tens = (user_input // 10) % 10
ones = (user_input // 1) % 10
#виводимо на екран
print(thousand)
print(hundreds)
print(tens)
print(ones)