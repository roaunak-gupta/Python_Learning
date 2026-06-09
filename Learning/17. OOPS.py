
class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} Say Woof!"

name = input("Enter your name : ")
dog = Dog(name,3)
print(dog.bark()) 