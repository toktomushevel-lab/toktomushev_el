import random
from utils import get_number_input

def play_round(round_number):
    speed = random.randint(1, 10)
    print(f"Раунд {round_number}")

    for _ in range(3):
        guess = get_number_input("Введи число: ")
        if guess == speed:
            print("Ты уничтожил астероид!")
            return True
        elif guess < speed:
            print("Скорость астероида больше")
        else:
            print("Скорость астероида меньше")

    print("Планета разрушена! Было число:", speed)
    return False

def start_game():
    print("Игра: Космический рейнджер")
    print("Угадай скорость астероида (1–10)")

    for round_number in range(1, 6):
        if not play_round(round_number):
            break
    else:
        print("Ты спас планету! Победа!")