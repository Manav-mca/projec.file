# Example 6: Class methods with class variables
class Product:
    tax_rate = 0.1  # Class variable
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    @classmethod
    def set_tax_rate(cls, rate):
        cls.tax_rate = rate
    
    def total_price(self):
        return self.price * (1 + Product.tax_rate)

p1 = Product("Laptop", 1000)
p2 = Product("Mouse", 50)
Product.set_tax_rate(0.15)
print(f"{p1.name}: ${p1.total_price()}")  # Laptop: $1150.0

# Example 7: Private class variables
class Database:
    _connection_count = 0  # Private class variable
    
    def __init__(self, name):
        self.name = name
        Database._connection_count += 1
    
    @classmethod
    def get_connections(cls):
        return cls._connection_count

db1 = Database("users")
db2 = Database("products")
print(f"Active connections: {Database.get_connections()}")  # 2

# Example 8: Class variable inheritance
class Animal:
    species_count = 0
    
    def __init__(self, name):
        self.name = name
        Animal.species_count += 1

class Dog(Animal):
    breed_count = 0
    
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        Dog.breed_count += 1

d1 = Dog("Rex", "German Shepherd")
d2 = Dog("Max", "Golden Retriever")
print(f"Animals: {Animal.species_count}")  # 2
print(f"Dogs: {Dog.breed_count}")  # 2

# Example 9: Dictionary as class variable
class Config:
    settings = {"debug": False, "version": "1.0"}
    
    def __init__(self, app_name):
        self.app_name = app_name
    
    def update_setting(self, key, value):
        Config.settings[key] = value

app1 = Config("WebApp")
app2 = Config("MobileApp")
app1.update_setting("debug", True)
print(f"App1 debug: {app1.settings['debug']}")  # True
print(f"App2 debug: {app2.settings['debug']}")  # True (shared!)

# Example 10: Constants as class variables
class MathConstants:
    PI = 3.14159
    E = 2.71828
    
    def __init__(self, name):
        self.calculator_name = name
    
    def circle_area(self, radius):
        return MathConstants.PI * radius ** 2

calc = MathConstants("Scientific")
print(f"Area: {calc.circle_area(5)}")  # Area: 78.53975