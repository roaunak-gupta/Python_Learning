# Wrapping data and function in single unit (Object)

class Student:
    def __init__(self,name):
        self.name = name
    
    def display(self):
        print(self.name)

s = Student("Roaunak Gupta")
s.display()