# 1- .index
# my_list_numbers = [1, 2, 3, 4, 5, 6, 9, 10, 20, 30, 20, 40, 20, 60]
# my_range_list = list(range(2, 1000002, 2))
# print(my_range_list)
# print(len(my_range_list))
# print(my_list_numbers.index(20))

# 2. len()
# print("The size of our list is:", len(my_list_numbers)) # len is the short form of length

# 3- .append method
# num = int(input("enter a number to be added in the list: "))
# my_list_numbers.append(num)
# my_list_numbers.append([70,80,90,100])

# 4- .extend()
# my_list_numbers.extend([70,80,90,100])
# print(my_list_numbers)

# 5- .insert(index, value)
# my_list_numbers = [10, 20, 30, 40, 50, 60]
# my_list_numbers.insert(3, 70)
# print(my_list_numbers)

 
# l1 = [1, 8, 7, 2, 21, 15]
# l1.insert(-1, 99)
# print(l1)

# .pop()
# l1 = [1, 8, 7, 2, 21, 15]
# l1.pop()
# l1.pop(-1) # == l1.pop()
# removed_value = l1.pop(3)
# print("I just removed" ,removed_value,"from the list: ", l1)

# .remove(value)
# l1 = [1, 8, 7, 2, 21, 15, 21, 21, 21, 100, 23, 21, 22, 21, 21]
# l1.remove(21)
# print(l1)

# .count(value)
# print("The value 21 appears",l1.count(21), "times in your list")

# .sort()
# l1 = [1, 8, 7, 2, 21, 15]
# # l1.sort() # It will sort them in ascending order
# l1.sort(reverse=True) # sort in descending order
# print(l1)


# .sorted()
l1 = [1, 8, 7, 2, 21, 15]
# l2 = sorted(l1)
# print(l1)
# print(l2)

# # .reverse()
# l1.reverse()
# print(l1)

# del
# del l1
# del l1[2]
# print(l1)


# .clear()
# l1.clear()
# print(l1)


# ------------  Combining two or more list  ------------
# a = [1,2,3,4,5]
# b = [6,7,8,9,10]
# d = [11,12,13,15,14]
# c = a + b + d
# print(c)
# print()


# ------------  Repeating the elements of an list (array)  ------------
# a = [1,2,3,4,5]

# print(a * 2)



# Mutability Trap

# a = [[]] * 3
# # a[0] = 3
# a[0].append(5)
# print(a)

# print(id(a[0]))
# print(id(a[1]))
# print(id(a[2]))



a = [1, 2, 3, 4, 5]
print(max(a))
print(min(a))
print(sum(a))