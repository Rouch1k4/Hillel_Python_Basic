lst = [1, 2, 3, 4, 5, 6]
#lst = [1, 2, 3]
#lst = [1, 2, 3, 4, 5]
#lst = [1]
#lst = []

#розділяємо середину
mid = (len(lst) + 1) // 2

#перша та друга частина
first_part = lst[:mid]
second_part = lst[mid:]

#створення нового списку та print
result = [first_part, second_part]
print(result)