

















def tasbeeh():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


counter = tasbeeh()

while True:
    user_input = input("Press + to count: ")

    if user_input == "+":
        print(counter())
    else:
        print("Wrong Input")