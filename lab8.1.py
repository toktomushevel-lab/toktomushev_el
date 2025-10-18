class BankAccount:
    def __init__(self, name, accountnumber, balance, pin):
        self.name = name
        self.__accountnumber = accountnumber
        self.__balance = balance
        self.__pin = pin


    def accountnumber(self, pin):
        if pin != self.__pin:
            return "Неверный pin-код"
        return f"Номер счета 4217637888609"


    def deposit(self, amount, pin):
        if pin != self.__pin:
            return "Неверный pin-код"
        
        if amount <= 0:
            return "Сумма пополнения должна быть положительной"
        
        self.__balance += amount
        return f"Счёт пополнен на {amount} сом. Новый баланс: {self.__balance} сом"


    def withdraw(self, amount, pin):
            if pin != self.__pin:
                return "Неверный pin-код"
            
            if amount <= 0:
                return "Сумма снятия должна быть положительной"
        
            if amount > self.__balance:
                return "Недостаточно средств на счёте"
        
            self.__balance -= amount
            return f"Снято {amount} сом. Остаток: {self.__balance} сом"
    

    def get_balance(self, pin):
            if pin != self.__pin:
                return "Неверный pin-код"
            
            return f"Баланс счёта: {self.__balance} сом"
    


acc = BankAccount("Иванчик", 4217637888609, 1000, 1234)
print(acc.name)
print(acc.accountnumber(1234))
print(acc.deposit(600, 1234))
print(acc.withdraw(300, 1234))
print(acc.get_balance(1234))
print(acc.get_balance(78743281))