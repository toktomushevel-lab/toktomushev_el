from abc import ABC, abstractmethod

class PaymentSystem(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(PaymentSystem):
    def process_payment(self, amount):
        print(f"Оплата картой на сумму {amount} сом")

class CryptoPayment(PaymentSystem):
    def process_payment(self, amount):
        print(f"Оплата криптовалютой на сумму {amount} сом")

class BankTransfer(PaymentSystem):
    def process_payment(self, amount):
        print(f"Оплата банковским переводом на сумму {amount} сом")

cc = CreditCardPayment()
crypto = CryptoPayment()
bank = BankTransfer()

cc.process_payment(999)
crypto.process_payment(333)
bank.process_payment(555)