def factorial(n):
    if n == 1 or n == 0:
        return 1

    return n * factorial(n-1)

# n * factorial(n-1): 5 (n-1 = 4) factorial(4)

# print(factorial(5)) #s 120


def fib(n):
    if n <= 1:               # base case
        return n
    return fib(n-1) + fib(n-2)   # recursive case
 
print(fib(6))   # 8
# [fib(n) for n in range(7)]
# # [0, 1, 1, 2, 3, 5, 8]




# def greet():
#     print("Hello")
#     return greet() # THis will throw a RecursionError but this is what recursion is

# greet()