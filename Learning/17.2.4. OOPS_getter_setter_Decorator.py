class Employee:
    def __init__(self, name, empID, designation, salary):
        self.name = name
        self.empID = empID
        self.designation = designation
        self._salary = salary

    # Getter Method
    @property
    def salary(self):
        return self._salary

    # Setter Method
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative.")
        self._salary = value


emp = Employee("Roaunak Gupta", 8003000, "D.E.T.", 25564)
print(emp.salary)  # Getter called
emp.salary = 60000  # Setter called
print(emp.salary)


# Traditional way for getter and setter method
class Studnet:
    def __init__(self, name, rollno, course, year):
        self.name = name
        self.rollno = rollno
        self.course = course
        self.year = year

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_rollno(self):
        return self.rollno

    def set_rollno(self, rollno):
        self.rollno = rollno

    def get_course(self):
        return self.course

    def set_course(self, course):
        self.course = course

    def get_year(self):
        return set.year

    def set_year(self, year):
        self.year = year


student = Studnet("Roaunak Gupta", 203620109014, "B.Tech", "4th")
print(student.get_course())
student.set_course("M.Tech")
print(student.get_course())