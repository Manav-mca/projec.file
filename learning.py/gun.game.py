# snak water gun:
import random

def ckeck(comp, user):
    if comp == user:
        return 0 
    
    if (comp == 0 and user == 1):
        return -1
    
    if (comp == 1 and user == 2):
        return -1
    
    return 1

choices= [ "Snake", "Water", "Gun"]
print("Welcome to Snake Water Gun Game!")
print("0 - Snake, 1 - Water, 2 - Gun")

user  = int(input("Enter your choice: "))
comp = random.randint(0, 2)

print(f"You chose: {choices[user]}")
print(f"computer chose: {choices[comp]}")

result = ckeck(comp, user)
if result == 0:
    print("It's a tie!")
elif result == -1:
    print("You lose!")
else:
    print("You win!")
    


