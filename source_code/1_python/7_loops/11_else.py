numbers = [4, 8, 15, 16, 23, 42]
 
for n in numbers:
    if n == 100:
        print("Found it!")
        break
else:
    print("100 was never in the list")