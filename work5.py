import random

def cosmic_ranger():
    round_number = 1

    while round_number <= 10:
        asteroid_speed = random.randint(1, 10)
        attempts = 0

        print(f"Раунд {round_number}: Защити планету! Угадай скорость астероида (1-10)")

        while attempts < 3:
            try:
                guess = int(input("угадай скорость астероида: "))
            except ValueError:
                print("Пожалуйста, вводи число от 1 до 10")
                continue

            attempts += 1

            if guess == asteroid_speed:
                print("Астероид уничтожен! Переход к следующему раунду")
                round_number += 1
                break
            elif guess < asteroid_speed:
                print("Скорость астероида больше.")
            else:
                print("Скорость астероида меньше.")

        else:
            print(f"Поражение! Планета уничтожена. Загаданная скорость была {asteroid_speed}")
            return

    print("Поздравляем! Ты спас планету от всех астероидов!")

cosmic_ranger()