from abc import ABC, abstractmethod

class Course(ABC):
    @abstractmethod
    def start(self): pass
    @abstractmethod
    def get_materials(self): pass
    @abstractmethod
    def end(self): pass

class PythonCourse(Course):
    def start(self): print("Старт Python курса")
    def get_materials(self): return ["Введение", "Типы", "Циклы", "ООП"]
    def end(self): print("Python курс завершён")

class MathCourse(Course):
    def start(self): print("Старт курса по математике")
    def get_materials(self): return ["Алгебра", "Геометрия", "Анализ"]
    def end(self): print("Математика завершена")

for c in [PythonCourse(), MathCourse()]:
    c.start()
    print(c.get_materials())
    c.end()
    print("-" * 20)
