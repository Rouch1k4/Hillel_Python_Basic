class GroupFullException(Exception):
    def __init__(self, message="У групі не може бути більше 10 студентів"):
        super().__init__(message)

class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} y.o."


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, record book: {self.record_book}"

    def __eq__(self, other):
        return isinstance(other, Student) and self.record_book == other.record_book

    def __hash__(self):
        return hash(self.record_book)


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupFullException()
        self.group.add(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number: {self.number}\n{all_students}'



st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')

#Додаємо 10 студентів
for i in range(10):
    st = Student('Male', 20+i, f'Name{i}', f'Last{i}', f'RB{i}')
    gr.add_student(st)

#Видаляємо двох — звільняємо місце для Jobs і Taylor
gr.delete_student('Last0')
gr.delete_student('Last1')

#Тепер можемо безпечно додати ще 2 студентів
gr.add_student(st1)
gr.add_student(st2)

# Спроба додати 11-го → має викликати помилку
try:
    extra = Student('Male',  25, 'Extra', 'Student', 'RB999')
    gr.add_student(extra)
except GroupFullException as e:
    print(f"️Помилка: {e}")

print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

