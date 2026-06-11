
class Car:
    def __init__(self):
        print("Car Initialize");
        self.acc = False
        self.brk = False
        self.cluch = False

    def start(self):
        self.cluch = True
        self.acc = True
        print("Car Started.")


car = Car() # Initalize the Car 
car.start() # This type of class exicute the command but there is hide the functions of the class (Car)