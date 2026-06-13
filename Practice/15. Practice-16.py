class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print(f"Role : {self.role}")
        print(f"Department : {self.dept}")
        print(f"Salary : {self.salary}\n")


class Engineer(Employee):
    def __init__(self, name, empID, age, role="Engineer", dept="TBD", salary="TBD"):
        self.name = name
        self.age = age
        self.empID = empID
        super().__init__(role, dept, salary)


emp1 = Employee("Engineer", "IQA", "650000")
emp1.showDetails()

engineer = Engineer("Roaunak Gupta", 8003000, 24, "Engineer")
engineer.showDetails()
