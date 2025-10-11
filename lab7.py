class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

class Mammal(Animal):
    def __init__(self, name, species, age, fur_type):
        super().__init__(name, species, age)
        self.fur_type = fur_type
    def make_sound(self):
        return f"{self.name} лает!"
    def give_birth(self):
        return f"{self.name} рожает детенышей!"

class Reptile(Animal):
    def __init__(self, name, species, age, scale_type):
        super().__init__(name, species, age)
        self.scale_type = scale_type
    def hiss(self):
        return f"{self.name} шипит!"
    def lay_eggs(self):
        return f"{self.name} откладывает яйца!"

dog = Mammal("Чихуахуа", "Собака", 3, "Короткая")
snake = Reptile("Ползунок", "Змея", 2, "Чешуйчатая")

print(dog.make_sound(), dog.give_birth())
print(snake.hiss(), snake.lay_eggs())