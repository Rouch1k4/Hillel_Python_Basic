lst = [0, 1, 7, 2, 4, 8]
#lst = [1, 3, 5]
#lst = []
#lst = [6]
sum = 0
for index, value in enumerate(lst):
    if index % 2 == 0:
           sum += value

if lst:
    result = sum * lst[-1]
else:
    result = 0

print("result :", result)