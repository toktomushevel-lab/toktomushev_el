from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

class Lion(Animal):
    def eat(self):
        print("Лев ест мясо")

    def sleep(self):
        print("Лев спит на лежа")

class Elephant(Animal):
    def eat(self):
        print("Слон ест баанан")

    def sleep(self):
        print("Слон спит стоя")

class Snake(Animal):
    def eat(self):
        print("Змея ест пауков")

    def sleep(self):
        print("Змея спит свернувшись")

lion = Lion()
elephant = Elephant()
snake = Snake()

lion.eat()
lion.sleep()
elephant.eat()
elephant.sleep()
snake.eat()
snake.sleep()