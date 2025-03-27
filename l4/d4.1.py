lst = [0, 1, 0, 12, 3]
#lst =[0]
#lst =[1, 0, 13, 0, 0, 0, 5]
#lst =[9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
new_lst = []
#завдяки циклу for перевіряємо чи число != 0
for l in lst:
    if l != 0:
       new_lst.append(l) #все що не є 0 добав новий список

num_zeros = lst.count(0) #кількість 0

#добавляємо 0
for l in range(num_zeros):
    new_lst.append(0)

print(new_lst)