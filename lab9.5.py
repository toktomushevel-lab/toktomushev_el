class UserProfile:
    def __init__(self, email, password):
        self.__email = email
        self.__password = password
        self._status = "Базовый"

    def login(self, email, password):
        if email == self.__email and password == self.__password:
            print("Вход выполнен успешно")
            return True
        else:
            print("Ошибка: неверный логин или пароль")
            return False

    def upgrade_to_premium(self):
        self._status = "Премиум"
        print("Статус обновлён до Премиум")

    def get_info(self):
        return f"Email: {self.__email}, Статус: {self._status}"


if __name__ == "__main__":
    user = UserProfile("user@gmail.com", "12345")

    if user.login("user@gmail.com", "12345"):
        print(user.get_info())
        user.upgrade_to_premium()
        print(user.get_info())
    else:
        print("Доступ запрещён")