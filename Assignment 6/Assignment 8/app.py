class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

teacher = Teacher("Mr. Ahmed ", "Mathematics")
print(f"Name: {teacher.name}, Subject: {teacher.subject}")
