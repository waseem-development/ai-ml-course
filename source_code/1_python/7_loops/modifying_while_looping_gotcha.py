# numbers = [1, 2, 4, 6]
# for n in numbers:
#     if n % 2 == 0: # even numbers
#         numbers.remove(n) # remove all the even numbers
# print(numbers)

numbers = [1, 2, 4, 6]
for n in numbers[:]: # create a copy of numbers. Keep modifying the original while looking at the copy
    if n % 2 == 0: # even numbers
        numbers.remove(n) # remove all the even numbers
print(numbers)