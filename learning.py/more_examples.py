# Example 1: Counter with class variable
class Student:
    total_students = 0  # Class variable to track total students
    
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable
        Student.total_students += 1  # Increment class variable

s1 = Student("Alice", 20)
s2 = Student("Bob", 22)
print(f"Total students: {Student.total_students}")  # 2

# Example 2: Default values with class variables
class BankAccount:
    interest_rate = 0.05  # Class variable - same for all accounts
    
    def __init__(self, owner, balance):
        self.owner = owner      # Instance variable
        self.balance = balance  # Instance variable
    
    def add_interest(self):
        self.balance += self.balance * BankAccount.interest_rate

acc1 = BankAccount("John", 1000)
acc2 = BankAccount("Jane", 2000)

# Change interest rate for all accounts
BankAccount.interest_rate = 0.07
acc1.add_interest()
acc2.add_interest()
print(f"{acc1.owner}: ${acc1.balance:.2f}")  # John: $1070.00
print(f"{acc2.owner}: ${acc2.balance:.2f}")  # Jane: $2140.00

# Example 3: Modifying class variable through instance
class Employee:
    company = "TechCorp"  # Class variable
    
    def __init__(self, name):
        self.name = name  # Instance variable

emp1 = Employee("Alice")
emp2 = Employee("Bob")

# This creates an instance variable, doesn't change class variable
emp1.company = "NewCorp"
print(f"{emp1.name} works at {emp1.company}")  # Alice works at NewCorp
print(f"{emp2.name} works at {emp2.company}")  # Bob works at TechCorp
print(f"Company class variable: {Employee.company}")  # TechCorp

# Example 4: List as class variable (dangerous!)
class Team:
    members = []  # Class variable - shared by all instances!
    
    def __init__(self, name):
        self.name = name  # Instance variable
    
    def add_member(self, member):
        self.members.append(member)  # Modifies shared list!

team1 = Team("Alpha")
team2 = Team("Beta")

team1.add_member("John")
team2.add_member("Jane")

print(f"Team1 members: {team1.members}")  # ['John', 'Jane']
print(f"Team2 members: {team2.members}")  # ['John', 'Jane'] - Same list!

# Example 5: Correct way with instance variables
class TeamFixed:
    def __init__(self, name):
        self.name = name
        self.members = []  # Instance variable - each team has own list
    
    def add_member(self, member):
        self.members.append(member)

team3 = TeamFixed("Gamma")
team4 = TeamFixed("Delta")

team3.add_member("Alice")
team4.add_member("Bob")

print(f"Team3 members: {team3.members}")  # ['Alice']
print(f"Team4 members: {team4.members}")  # ['Bob']