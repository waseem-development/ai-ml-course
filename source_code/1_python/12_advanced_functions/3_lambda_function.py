x = lambda n: n * 2 # Lambda doesn't execute immediately
# Python creates a function. It does not execute it.

# print(x) # <function <lambda> at 0x7f...>   ==> This variable contains a function.

# print(x(5))


# ************ Lambda with Multiple Parameters ************
add = lambda a, b: a + b
# print(add(12,6))

multiply = lambda a, b: a * b
# print(multiply(5, 4))

# ************ Lambda with zero Parameters ************
hello = lambda: "Hello Paxto!"
# print(hello())

# ************ Lambda Can Return Any Expression ************
greet = lambda name: "Hello " + name
# print(greet("Paxto"))

is_even = lambda n: n % 2 == 0
# print(is_even(10))

length = lambda text: len(text)
# print(length("Python"))

maximum = lambda a, b: max(a, b)
# print(maximum(10, 20))

# ************ Lambda + max() / min() ************
students = [
    {"name": "Ali", "marks": 85},
    {"name": "Ahmed", "marks": 92},
    {"name": "Bilal", "marks": 78}
]

# def get_marks(student):
#     return student["marks"]

# def maximum_marks(students):
#     return max(students, key=get_marks)

# print(maximum_marks(students))


top_student = max(
    students,
    key=lambda student: student["marks"]
)
print(top_student)