class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.__discount = 0

    def get_price(self):
        if self.__discount > 0:
            return self.price * (1 - self.__discount / 100)
        return self.price

    def set_discount(self, discount, is_admin=False):
        if not is_admin:
            print("Ошибка: нет прав администратора")
            return
        if not (0 <= discount <= 100):
            print("Скидка должна быть от 0 до 100")
            return
        self.__discount = discount
        print(f"Скидка {discount}% установлена")

if __name__ == "__main__":
    p = Product("Ноутбук", 50000)
    print("Цена:", p.get_price())
    p.set_discount(10)
    p.set_discount(10, is_admin=True)
    print("Цена со скидкой:", p.get_price())