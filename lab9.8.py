class Car:
    def move(self, distance):
        time = distance / 60
        fuel = distance * 0.08
        print("Машина проедет", distance, "км за", round(time, 2), "ч. Расход топлива:", round(fuel, 2), "л.")

class Truck:
    def move(self, distance):
        time = distance / 40
        fuel = distance * 0.2
        print("Грузовик проедет", distance, "км за", round(time, 2), "ч. Расход топлива:", round(fuel, 2), "л.")

class Bicycle:
    def move(self, distance):
        time = distance / 15
        print("Велосипед проедет", distance, "км за", round(time, 2), "ч. Расход топлива: 0 л.")

def simulate_transport(transport_list, distance):
    for vehicle in transport_list:
        vehicle.move(distance)

cars = [Car(), Truck(), Bicycle()]
simulate_transport(cars, 120)