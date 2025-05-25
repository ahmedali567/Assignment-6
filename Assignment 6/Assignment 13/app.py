class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print("Engine started.")

class Car:
    def __init__(self, make, model, horsepower):
        self.make = make
        self.model = model
        self.engine = Engine(horsepower)

    def start(self):
        print(f"Starting {self.make} {self.model}...")
        self.engine.start()

# Example usage
my_car = Car("Toyota", "Corolla", 150)
my_car.start()
