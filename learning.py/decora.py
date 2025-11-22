# # # def debug(func):
# # #     def wrapper(*args, **kwargs):
# # #         print(f"calling {func.__name__}")
# # #         return func(*args, **kwargs)
# # #     return wrapper
# # # @debug
# # # def say_hi():
# # #     print("hello")

# # # say_hi()

# # import time

# # def timer(func):
# #     def wrapper(*args, **kwargs):
# #         start = time.time()
# #         result = func(*args, kwargs)
# #         print(f"Time: {time.time() -start:.2f}s")
# #         return result
# #     return wrapper
# # @timer
# # def slow():
# #     time.sleeo(1)

# # slow


# def uppercase(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result.upper()
#     return wrapper
# @uppercase
# def greet(name):
#     return f"Hello {name}"
# print(greet("Alice"))


def count_calls(func):
    func.count = 0
    def wrapper(*args, **kwargs):
        func.calls += 1
        print(f"call # {func.calls}")
        return func(*args, **kwargs)
    return wrapper
@count_calls
def test():
    print("Testing")
test()
test()
