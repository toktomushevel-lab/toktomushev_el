import math

class Square:
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return 4 * self.side

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

figures = [
    Square(5),
    Circle(3),
    Triangle(3, 4, 5)
]

for figure in figures:
    print(figure.perimeter())