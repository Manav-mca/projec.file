# # # Using @property decorator (python way)
# # class person:
# #     def __init__(self, name):
# #         self._name = name
# #     @property
# #     def name(self):
# #         """Getter"""
# #         return self._name
# #     @name.setter
# #     def name(self, value):
# #         """Setter"""
# #         if not isinstance(value, str):
# #             raise ValueError("Name must be a string")
# #         self._name = value

# # # Usage
# # person = person("John")
# # print(person.name)
# # person.name = "Bob"

# # # Property with validation

# # class Temperature:
# #     def __init__(self, celsius=0):
# #         self._celsius = celsius
    
# #     @property
# #     def celsius(self):
# #         return self._celsius
    
# #     @celsius.setter
# #     def celsius(self, value):
# #         if value < -273.15:
# #             raise ValueError("Temperature below absolute zero is not possible")
# #         self._celsius = value
    
# #     @property
# #     def fahrenheit(self):
# #         return (self._celsius * 9/5) + 32

# # # Usage
# # temp = Temperature(25)
# # print(temp.celsius)     # 25
# # print(temp.fahrenheit)  # 77.0
# # temp.celsius = 30       # Valid


# def Hello():
#     print("Hello, my name is manav ")
#     print("Are your fine")
#     print("I am fine")


# def add(a, b):
#     print(a+b)
# Hello()
# add(1, 3)


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def area(self):
        return self._width

    def set_width(self, value):
        if value <= 0:
            raise ValueError("width must be positive")
        self._width = value
    width = property(area, set_width)

# Usage
rect = Rectangle(10, 5)
print(rect.width)
rect.width = 20
