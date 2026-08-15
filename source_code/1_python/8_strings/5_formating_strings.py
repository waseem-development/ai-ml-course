x = "12345"

# print(x.isdigit())         # True

# print("123abc".isdigit())  # False
# print("12.5".isdigit())      # False
# print("-123".isdigit())    # False


name = "Waseem"

# print(name.isalpha())   # True
# print("میں وسیم ہوں".isalpha())  # False


# print("Waseem123".isalnum())  # True
# print("12345".isalnum())      # True
# print("Waseem".isalnum())     # True


# print("   ".isspace())      # True
# print("\t".isspace())       # True
# print("\n".isspace())       # True

# print("Waseem Ahmed".isspace()) # False
age_text = input("Enter your age: ")

while not age_text.isdigit():
    print("Please enter only numbers not alphabets")
    age_text = input("Enter your age: ")

age = int(age_text)
print("You are", age, "years old")
