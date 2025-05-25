class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

emp = Employee("Ahmed", 50000, "123-45-6789")

print("Name:", emp.name)

print("Salary:", emp._salary)

try:
    print("SSN:", emp.__ssn)
except AttributeError:
    print("SSN: Cannot access private attribute directly.")
