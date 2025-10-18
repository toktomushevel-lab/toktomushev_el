class SmartWatch:
    def __init__(self, battery=100):
        self.__battery = min(max(battery, 0), 100)

    def use(self, minutes):
        discharge = minutes // 10 
        self.__battery = max(self.__battery - discharge, 0)

    def charge(self, percent):
        if percent < 0:
            raise ValueError("Нельзя заряжать на отрицательный процент")
        self.__battery = min(self.__battery + percent, 100)

    def get_battery(self):
        return self.__battery

watch = SmartWatch()
print(watch.get_battery())

watch.use(25)
print(watch.get_battery())

watch.charge(5)
print(watch.get_battery())

watch.use(1000)
print(watch.get_battery())

watch.charge(50)
print(watch.get_battery())
