class FireSpell:
    def cast(self, target):
        print(f"{target} получает урон огнём")

class IceSpell:
    def cast(self, target):
        print(f"{target} замораживается")

class HealingSpell:
    def cast(self, target):
        print(f"{target} восстанавливает здоровье")

spells = [
    FireSpell(),
    IceSpell(),
    HealingSpell()
]

for spell in spells:
    spell.cast("Гоблин")