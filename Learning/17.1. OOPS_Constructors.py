class Students:
    # Defalut Constructor
    def __init__(self):
        pass

    # Parameterized Constructor
    def __init__(self, name, age=0, course="B.Tech"):
        print("Adding new Studnets...")
        self.name = name
        self.age = age
        self.course = course


students = Students("Roaunak",24)

print(students.name,students.age,students.course)
  

