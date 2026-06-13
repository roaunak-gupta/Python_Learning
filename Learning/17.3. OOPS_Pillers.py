# Object Orianted Programming have 4 basic Pillers in any Language.
# 1. Abstractions
# 2. Encapsulation
# 3. Polymorphism
# 4. Inheritance

#-----------------------------------------------------------------------


#! 1. Class and Object

# A Class is a blueprint for creating objects.
# An Object is an instance of a class .



class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


car1 = Car("Toyota", "Fortuner")
car2 = Car("Honda", "City")

print(car1.brand)  # Toyota
print(car2.model)  # City


#-----------------------------------------------------------------------


#!2. Constructor(__init__)
# A constructor is a special method that runs automatically when an object is created.

class Student:
    def __init__(self, name):
        self.name = name


s1 = Student("Somu")
print(s1.name)


#-----------------------------------------------------------------------


#! 3. Encapsulation
# Encapsulation means hiding data and controlling access to it.


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    def get_balance(self):
        return self.__balance


account = BankAccount(10000)
print(account.get_balance())

# Benefit: Protects data from accidental modification.


#-----------------------------------------------------------------------


#! 4. Inheritance
# Inheritance allows one class to acquire properties and methods of another class .


class Animal:
    def speak(self):
        print("Animal speaks")


class Dog(Animal):
    def bark(self):
        print("Dog barks")


d = Dog()
d.speak()
d.bark()


#-----------------------------------------------------------------------


#! 5. Polymorphism
# Polymorphism means same method name, different behavior.


class Dog:
    def sound(self):
        print("Bark")


class Cat:
    def sound(self):
        print("Meow")


animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()


#-----------------------------------------------------------------------


#! 6. Abstraction
# Abstraction means showing only essential details and hiding implementation.

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car started")


c = Car()
c.start()
