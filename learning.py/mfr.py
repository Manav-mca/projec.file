from functools import reduce

#Sample data 
# numbers = 1
# while numbers <= 10:
#     print(numbers)
# #     numbers +=1
# numbers = [1,2,3,4,5,6,7,8,9,10]
# # map - transforms each element in the list
# squares = list(map(lambda x: x**2, numbers))
# print(f"squares: {squares}")
# cubes = list(map(lambda x: x**3, numbers))
# print(f"cubes: {cubes}")
 
# # Filter - deep elements that match a condition

# evens = list(filter(lambda x: x % 2 == 0 , numbers))
# print(f"Even numbers: {evens}")

# odd = list(filter(lambda x: x % 2 == 1 ,numbers))
# print(f"Odd numbers: {odd}")


# # map - transforms 
# # reduce - combine all elements into a single value
# total = reduce(lambda x, y: x + y ,
#                 filter(lambda x: x % 2 == 0,
#                         map(lambda x: x**2, numbers)))
# print(f"Sum of squares of evens: {total}")


# more examples
names = ["Alice", "boo", "charlie", "diana"]
ages = [25,30,35,28]
# zip - combines two or more lists into a list of tuples
combined = list(filter(lambda x: x >= 30 ,ages))


#Filter examples
long_ages = list(filter(lambda x: len(x) > 4, names))
adults = list(filter(lambda x: x >= 30, ages))

# Reduce examples
longest_name = reduce(lambda x, y: x if len(x) > len(y) else y, names)
max_age = reduce(lambda x, y : x if x > y else y, ages) 

print(f"Longest_name : {long_ages}")
print(f"Adults: {adults}")
print(f"Longest_name : {longest_name}")
print(f"Max_age : {max_age}")


