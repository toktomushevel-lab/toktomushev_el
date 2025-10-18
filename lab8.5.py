class Transport:
    def __init__(self, speed, capacity):
        self.speed = speed
        self.capacity = capacity

    def travel_time(self, distance):
        return distance / self.speed


class Bus(Transport):
    pass


class Train(Transport):
    pass


class Airplane(Transport):
    def travel_time(self, distance):
        return super().travel_time(distance) * 0.8


bus = Bus(60, 50)
train = Train(120, 200)
airplane = Airplane(800, 180)

distance = 400

print(bus.travel_time(distance))
print(train.travel_time(distance))
print(airplane.travel_time(distance))