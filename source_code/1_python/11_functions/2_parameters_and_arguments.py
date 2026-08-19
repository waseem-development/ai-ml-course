# def greeting(name): # here name is a variable called parameter and this is waiting to recieve a value from the function call
#     print(f"Hello How are you {name} 👋🏻")

# greeting("Waseem") # this value which we wrote inside the parenthesis is called "Argument"
# greeting("Abdul Razzaq")
# greeting("Fatima")
# greeting("Malak")
# greeting("Rehab")
# greeting("Youssef")


def add(a,b):
    print(f"The sum of {a} and {b} is {a+b}")

add(3,5)
add(3,7)
add(1,5)


# def describe_student(name, age, city):
#     return f"{name}, age {age}, from {city}"
 
# print(describe_student("Waseem", 22, "Quetta"))
# # "Ahmed, age 25, from Karachi"


# def calculate_price(price=150, discount=0.1): # default Parameter
#     return price - (price * discount)
 
# print(calculate_price())          # 135.0 (uses default)
# print(calculate_price(100, 0.25))  


# def describe_student(name, age, city):
#     return f"{name}, age {age}, from {city}"
 
# print(describe_student(city="Karachi", name="Ahmed", age=25))
# # order doesn't matter when you use keyword arguments