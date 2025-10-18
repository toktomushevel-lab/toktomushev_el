class Manager:
    def work(self):
        print("Менеджер проводит встречи")

class Developer:
    def work(self):
        print("Разработчик пишет код")

class Designer:
    def work(self):
        print("Дизайнер рисует макеты")

employees = [
    Manager(),
    Developer(),
    Designer()
]

for employee in employees:
    employee.work()