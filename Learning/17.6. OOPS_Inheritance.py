class Car:
    @staticmethod
    def start():
        print("Car Started...")

    @staticmethod
    def stop():
        print("Car Stopped...")


class ToyotaCar(Car):
    def __init__(self, name, FuelType):
        self.name = name
        self.FuelType = FuelType


car1 = ToyotaCar("Fortuner", "Petrol")
car1.start()
