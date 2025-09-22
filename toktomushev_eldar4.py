flags = {
    'ru': {'red blue', 'white'},
    'kg': {'red yellow', 'red'},
    'ua': {'red blue', 'red', 'blue'},
    'uk': {'yellow', 'blue'},
    'kz': {'blue yellow', 'blue'},
    'tr': {'red white'},
    'jp': {'white red'},
    'uz': {'white blue', 'green'}
}

print("Введите цвет флага.")
print("Чтобы выйти, введите 'выход'.")

while True:
    color = input("Введите цвет: ").strip().lower()

    if color == 'выход':
        print("Вы вышли.")
        break

    matched_domains = []

    for domain, colors in flags.items():
        for combo in colors:
            if color in combo.split():
                matched_domains.append(domain)
                break 
