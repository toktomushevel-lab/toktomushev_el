class Student:
    def access_portal(self):
        print("Студент: просмотр расписания и оценок")

class Teacher:
    def access_portal(self):
        print("Преподаватель: выставление оценок и управление курсами")

class Administrator:
    def access_portal(self):
        print("Администратор: управление пользователями и системой")

users = [Student(), Teacher(), Administrator()]

for user in users:
    user.access_portal()