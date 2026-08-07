point = (4, 7, 9, 8, 9, 10)
 
x, y, z, a, b, c = point
# print(x, y, z)  

first, second, *rest, second_last, last = point
print(first)
print(second)
print(rest)
print(second_last)
print(last)