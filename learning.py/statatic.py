# static method

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
    
# Usage:
result = Calculator.add(5, 3)
print(result)

class Calculator2:
    def add (self, a, b):
        return a + b
    
c = Calculator2()
print(c.add(22, 3))
    