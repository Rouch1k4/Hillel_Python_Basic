import random

length = random.randint(3,10) #довжина рядку

lst = [random.randint(1,10) for _ in range(length)] #список

new_lst = [lst[0], lst[3], lst[-2]]

print("lst : ", lst)
print("new_lst : ", new_lst)
