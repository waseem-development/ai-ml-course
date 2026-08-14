numbers = [4, 8, 15, 16, 23, 42]

total = 0 # accumulator
print(sum(numbers))   
for n in numbers:
    total += n # +=  ==> total = total + 1

print(total)

prod = 1
for n in numbers:
    prod *= n # +=  ==> total = total + 1

print(prod)
# str_list = ["I", "Love", "Python", "and", "It", "is", "fun"]

# message = ""

# for m in str_list:
#     message += m + ""
# print(message)
