class Product:
    def __init__(self, price):
        self.__price = price

    def set_discount(self, percent):
        discount = self.__price * (percent / 100) 
        new_price = self.__price - discount
        if new_price < 0:
            self.__price = 0 
        else:
            self.__price = new_price

    def final_price(self):
        return self.__price          
    
p = Product(1500)
p.set_discount(50)
print(p.final_price())