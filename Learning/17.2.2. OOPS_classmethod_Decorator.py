# A class method is bound to the class & receives the class as an implicit first argument
# NOTE :- A Class method cannot access or modify class state & generally for utility.


class Person:
    name = "Anonymous"

    def changeName(self, name):
        self.name = name


person1 = Person()
print(person1.name)
person1.changeName("Roaunak Gupta")
# They cannot change the class attribute insted-of they create new instance of a attribute.
print(person1.name)
# Here you can also see changeName Method cannot change the person name of original.
print(Person.name)


class Student:
    name = "Anonymous"

    def changeName(self, name):

        self.name = name  # They create new instance of the name object
        # Method-1 : They overwrite the name of the class.
        self.__class__.name = name

    # Method-2 : This is the method to change the class attribute.
    @classmethod
    def changeName1(cls, name):
        cls.name = name


studnet = Student()
studnet.changeName("Roaunak Gupta")
print(f"Student : {studnet.name}")
studnet.changeName(f"Student name change by changeName method : {Student.name}")
studnet.changeName1("Uday Gupta")
print((f"Studnet name change by changeName1 Method : {Student.name }"));

