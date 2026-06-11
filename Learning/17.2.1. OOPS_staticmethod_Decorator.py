class Students:

    def __init__(self, name, age, course):
        print("Init Method Running.")
        self.name = name
        self.age = age
        self.course = course
        print("Init Method End.")

    # Static method used by Class level. A static method is a method that belongs to a class but does not use instance data (self) or class data (cls).
    @staticmethod
    def hello():
        print(f"Hello, Welcome to the Collage.")


s1 = Students("Roaunak Gupta", 24, "B.Tech in Computer Science & Engineering")
# We cannot directly call the method until method have self perameter or method have @staticmethod.
s1.hello()
