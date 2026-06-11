class Student:
    def __init__(self, chem, phy, math, eng):
        self.chem = chem
        self.phy = phy
        self.math = math
        self.eng = eng
        self.persentage = str(
            (self.chem + self.phy + self.math + self.eng) / 4) + "%"

    def calcPersentage(self):
        self.percentage = str(
            (self.chem + self.phy + self.math + self.eng) / 4) + "%"

    @property
    def calcPersentage_property(self):
        return str((self.chem + self.phy + self.math + self.eng) / 4) + "%"


student1 = Student(85, 56, 96, 47)
print(student1.persentage)

student1.phy = 45
print(student1.calcPersentage_property) # The propertiy Decorator is automaticaly calculate the current data.
