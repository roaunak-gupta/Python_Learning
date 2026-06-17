pie = (22/7)

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return float(pie) * (self.radius ** 2)

    def peremeter(self):
        return 2 * float(pie) * self.radius


circle = Circle(5)
print(f"Peremeter of a circle : {circle.peremeter()}")
print(f"Area of a circle : {circle.area()}")
