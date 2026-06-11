class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car Started...")
    @staticmethod
    def stop():
        print("Car Stopped...")


class ToyotaCar(Car):
    def __init__(self, name, type):
        self.name = name
        # Here we use Super() keyword to access the attribute of parant class.
        super().__init__(type)
        # This line of code to run the parant class method in child class using super()
        super().start()


car1 = ToyotaCar("Fortuner", "Petrol")
print(car1.type)
car1.stop()

