class Order:
    def __init__(self, base_amount):
        self.base_amount = base_amount

    def calculate_total(self):
        return self.base_amount


class DineInOrder(Order):
    def calculate_total(self):
        return self.base_amount * 1.1


class TakeAwayOrder(Order):
    def calculate_total(self):
        return self.base_amount


class DeliveryOrder(Order):
    def calculate_total(self):
        return self.base_amount * 1.1


order1 = DineInOrder(300)
order2 = TakeAwayOrder(200)
order3 = DeliveryOrder(150)

print(order1.calculate_total())
print(order2.calculate_total())
print(order3.calculate_total())