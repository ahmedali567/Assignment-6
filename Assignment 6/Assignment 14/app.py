class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def show_employees(self):
        print(f"Department: {self.name}")
        for emp in self.employees:
            print(f"- {emp.name}")

alice = Employee("Ahmed")
bob = Employee("Ali")

hr_department = Department("Human Resources")
hr_department.add_employee(alice)
hr_department.add_employee(bob)

hr_department.show_employees()
