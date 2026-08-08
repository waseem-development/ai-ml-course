age = int(input("Enter your age: "))
 
while age < 0:
    print("Age cannot be negative.")
    age = int(input("Enter your age: "))
 
print("Thanks! Your age is", age)