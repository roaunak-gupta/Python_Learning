class Students:

    def __init__(self, name, age, course):
        print("Init Method Running.")
        self.name = name
        self.age = age
        self.course = course
        print("Init Method End.")

    @staticmethod   #Static method used by Class level
    def hello():
        print(f"Hello, Welcome to the Collage.")


s1 = Students("Roaunak Gupta", 24, "B.Tech in Computer Science & Engineering")
s1.hello()
