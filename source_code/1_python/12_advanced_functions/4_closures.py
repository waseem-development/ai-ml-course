# def make_multiplier(factor):
#     def multiply(n):
#         return n * factor    # remembers "factor"
#     return multiply
 
# double = make_multiplier(2)
# # triple = make_multiplier(3)
 
# print(double(5))   # 10
# print(double(10))
# print(double(3))
# # triple(5)   # 15


# def make_counter():
#     count = 0

#     def increment():
#         nonlocal count
#         count += 1
#         return count
#     return increment
 
# counter = make_counter()
# print(counter())   # 1
# print(counter())   # 2
# print(counter())   # 3







def tasbeeh():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


counter = tasbeeh()

while True:
    user_input = input("Press + to count: ")

    if user_input.strip() == "+":
        print(counter())
    elif user_input.lower().strip() == "exit":
        exit()
    else:
        print("Wrong Input")