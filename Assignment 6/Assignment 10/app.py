class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")

# Creating an instance of the Dog class
my_dog = Dog("Buddy", "Golden Retriever")

# Calling the bark method
my_dog.bark()
