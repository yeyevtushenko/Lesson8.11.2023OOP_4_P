class Student:
    def __init__(self):
        self.name = input("Введіть ім'я студента: ")
        self.age = int(input("Введіть вік студента: "))
        self.grade = input("Введіть клас студента: ")
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)
        print(f"Предмет {course} додано до списку курсів студента {self.name}.")


student1 = Student()


print(f"\nІм'я: {student1.name}")
print(f"Вік: {student1.age}")
print(f"Курс: {student1.grade}")
print(f"Список курсів: {student1.courses}")


num_courses = int(input("Введіть кількість курсів, які ви хочете додати: "))
for i in range(num_courses):
    course_name = input(f"Введіть назву {i + 1}-го курсу: ")
    student1.add_course(course_name)


print(f"\nІм'я: {student1.name}")
print(f"Вік: {student1.age}")
print(f"Курс: {student1.grade}")
print(f"Оновлений список курсів: {student1.courses}")