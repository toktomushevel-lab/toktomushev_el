def get_number_input(prompt):
    """Запрашивает число у пользователя, пока не введет корректное."""
    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)
        print("Нужно ввести число!")