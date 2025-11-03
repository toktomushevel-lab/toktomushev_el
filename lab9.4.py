class BankAccount:
    def __init__(self, owner, balance, pin):
        self.__owner = owner
        self.__balance = balance
        self.__pin = pin

    def deposit(self, amount, pin):
        if pin != self.__pin:
            print("Неверный PIN")
            return
        if amount <= 0:
            print("Сумма должна быть положительной")
            return
        self.__balance += amount
        print(f"Пополнено {amount} Баланс: {self.__balance}")

    def withdraw(self, amount, pin):
        if pin != self.__pin:
            print("Неверный PIN")
            return
        if amount <= 0:
            print("Сумма должна быть положительной")
            return
        if amount > self.__balance:
            print("Недостаточно средств")
            return
        self.__balance -= amount
        print(f"Снято {amount} Баланс: {self.__balance}")

    def change_pin(self, old_pin, new_pin):
        if old_pin != self.__pin:
            print("Неверный старый PIN")
            return
        if len(str(new_pin)) != 4 or not str(new_pin).isdigit():
            print("PIN должен состоять из 4 цифр")
            return
        self.__pin = new_pin
        print("PIN успешно изменён")

if __name__ == "__main__":
    acc = BankAccount("Иванчик", 1000, 1234)
    acc.deposit(500, 1234)
    acc.withdraw(300, 1234)
    acc.change_pin(1234, 4321)
    acc.withdraw(200, 4321)
