# numbers = [123,6,535,14,21,23214,125,13]
# target = 21
# for n in numbers:
#     if n == target:
#         continue
#         print("\nI found", n, "Now skipping this value\n")
#     else:
#         print("\n", n, ": I will never get skipped because I am not the target\n")

# print("I am outside of the loop now")
# print("Anything, something, everything")

numbers = [1, 2, 3, 4, 5, 6]
 
for n in numbers:
    if n % 2 == 0:
        continue     # skip even numbers
    print(n)
 
