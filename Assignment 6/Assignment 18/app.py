class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative!")
        self._price = value

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

product = Product(100)
print(product.price) 

product.price = 120
print(product.price) 

try:
    product.price = -50 
except ValueError as e:
    print(e)

del product.price 
