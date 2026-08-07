l1 = [100,2,34,57,121,787,212]

# l2 = l1 # this does not create a copy rahter it creates a reference to the same list and if we change one of them, both will get changed
# l2.append(66)
# print(id(l1))
# print(id(l2))

# l2 = l1.copy()
# l2.append(1000)
# print(id(l1))
# print(id(l2))

# b = a.copy() # it creates a shallow copy and only copies the first level 
# a.append(6)
# b.append(7)
# print(a)
# print(b)

# a[3].append(3)

# print(a)
# print(b)

a = [1, 2, 3, [4, 5]]
import copy
b = copy.deepcopy(a)
a[3].append(3)
print(a)
print(b)