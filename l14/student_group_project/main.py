from student import Student
from group import Group, GroupFullException

# Створення студентів
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

# Створення групи
gr = Group('PD1')

# Додавання студентів
gr.add_student(st1)
gr.add_student(st2)

# Виведення групи
print(gr)

# Перевірка пошуку
assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
assert gr.find_student('Jobs2') is None

# Видалення студента
gr.delete_student('Taylor')

# Повторне виведення групи
print(gr)  # Only one student