class EmailNotification:
    def send(self, message):
        print(f"Отправка email: {message}")

class SMSNotification:
    def send(self, message):
        print(f"Отправка SMS: {message}")

class PushNotification:
    def send(self, message):
        print(f"Отправка push-уведомления: {message}")

notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]

for n in notifications:
    n.send("Ваш заказ отправлен")