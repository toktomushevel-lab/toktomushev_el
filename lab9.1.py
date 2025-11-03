from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

class CreditCardPayment(Payment):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        print(f"Оплата {amount}сом с карты {self.card_number[-4:]} прошла успешно")

    def refund(self, amount):
        print(f"Возврат {amount}сом на карту {self.card_number[-4:]} выполнен")

class CryptoPayment(Payment):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address

    def pay(self, amount):
        print(f"Отправлено {amount}сом в криптовалюте на адрес {self.wallet_address[:6]}...")

    def refund(self, amount):
        print(f"Возврат {amount}сом в криптовалюте на адрес {self.wallet_address[:6]}...")

if __name__ == "__main__":
    payments = [
        CreditCardPayment("1111 2222 3333 4444"),
        CryptoPayment("0xabc123def456")
    ]

    for payment in payments:
        payment.pay(100)
        payment.refund(50)
        print("-" * 30)