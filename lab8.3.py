class Course:
    def __init__(self, name, max_students):
        self.__name = name
        self.__students = []
        self.__max_students = max_students

    def add_student(self, name):
        if len(self.__students) < self.__max_students:
            self.__students.append(name)
            return True
        return False

    def remove_student(self, name):
        if name in self.__students:
            self.__students.remove(name)
            return True
        return False

    def get_students(self):
           return self.__students.copy()

course = Course("Python 101", 3)

course.add_student("Эльдар")
course.add_student("Алим")
course.add_student("Арлен")
print(course.get_students()) 

course.remove_student("Алим")
print(course.get_students())

course.add_student("Жумаш")
print(course.get_students())