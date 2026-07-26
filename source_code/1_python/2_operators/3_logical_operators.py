a = True # Boolean data types
b = False # Boolean data types
d = True
c = a and b and d # True and False and True
print(c)

e = a or b and d
print(e)

print(not a)

while True: 
    age = int(input("Enter your age: "))
    has_ticket = True
    print(age >= 13 and has_ticket)