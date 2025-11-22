# # class Parent:
# #     def __init__(self, name):
# #         self.name = name
    
# #     def speak(self):
# #         return f"{self.name}. Parent says hello"

# # class Child(Parent):
# #     def __init__(self, name, age):
# #         super().__init__(name)
# #         self.age = age
    
# #     def speak(self):  # Method overriding
# #         return f"{self.name} says hello"
    
# # p1 = Parent("john")
# # c1 = Child("john", 23)
# # print(p1.speak())
# # print(c1.speak())


# # key concept 
# class Animal:
#     def move(self):
#         return "I can move"
    
# class Doat(Animal):
#     def bark(self):
#         return "I can bark"

# # return super().move() 
# # return "I can move"
# d1 = Doat()
# print(d1.move())
# print(d1.bark())


# Multiple inheritance
class A:
    def method_a(self):
        return "A"
class B:
    def method_b(self):
        return "B"
class C(A, B):
    def C(A, B):
        return "c"


