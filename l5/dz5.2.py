ask_user = 'y'
while ask_user.lower() == "y":
    first_num = float(input("Enter  first number: "))
    operation = input("Enter  operation '+' '-' '/' '*' : ")
    second_num = float(input("Enter  second number: "))
    if operation == '+':
        result = first_num + second_num
        print("result : ", result)
    elif operation == '-':
        result = first_num - second_num
        print("result : ", result)
    elif operation == '*':
        result = first_num * second_num
        print("result : ", result)
    elif operation == '/':
        if second_num != 0:
            result = first_num / second_num
            print("result : ", result)
        else:
            print("second number is zero")

    else:
        print("Invalid operation")
    ask_user = input("You want to use calculator? y/n : ")