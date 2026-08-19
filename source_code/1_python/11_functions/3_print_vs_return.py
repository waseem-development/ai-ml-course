# def add_print(a,b):
#     print(f"The sum of {a} and {b} is {a+b}")

# def add_return(a,b):
#     return a + b


# # add_print(3,5)
# a = 3
# b = 5
# five_three_sum = add_return(a,b)
# print(five_three_sum)
# print(f"The sum of {a} and {b} is {five_three_sum}")



# def add_v1(a, b):
#     print(a + b)
 
# def add_v2(a, b):
#     return a + b
#     fjfklajsfklaj 
 
# result1 = add_v1(2, 3)   # prints 5, but result1 is None
# result2 = add_v2(2, 3)   # nothing printed, but result2 is 5
# print(result1)
# print(result2)

def get_min_max_sum(numbers):
    return min(numbers), max(numbers), sum(numbers)

l1 = [1,2,3,4,5,6]
minumum, maximum, sumnum = get_min_max_sum(l1) # tuple unpacking
print(f"minumum: {minumum}, maximum: {maximum}, sum: {sumnum}")
