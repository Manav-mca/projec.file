""" Instance variable and class variables are two different types of attributes
in object -oriented programming:
Class Variables
. shared by all instances of a class
. Defined at the class level (outside methods)
. same value across all objects unless explicitly
changed

Instance Variables
. unique to each instance/object
. difined inside methods (usuallu __init__)
. each object has its own copy 
. modified through specific instance

 """


class car:
    # Class variable - shared by all instances
    wheels = 4
    def  __init__(self, brand, model ):
        # Instance variables - unique to each instance 
        self.brand = brand
        self. model = model
# usage 
car1 = car("Toyota", "Camry")
car2 = car("Honda", "Civic")

# Instance variables are different for different 
print(f"Brand Name: {car1.brand}, Car Model: {car1.model}")
print(f"Brand Name: {car2.brand}, Car Model: {car2.model}")


# class variable is same for all instances
print(f"Number of wheels: {car.wheels}")

# changing class variable
car. wheels = 6
print(f"Number of wheels: {car.wheels}")
print(f"Number of wheels: {car1.wheels}")
print(f"Number of wheels: {car2.wheels}")

#But instance veriables remain  separete 

print(car1.brand)
print(car2.brand)


# more examples of class variable


