# a = [1, 2, 3, [4, 5]]

# print(a[3][0])
# print(a[3][1])

# # Truthy values & falsy values
# b = []

# if not b:
#     print("B is empty")


# str to list
# name = "Waseem"
# b = list(name)
# # print(b)

# # list to str
# c = "-".join(b)
# print(c)


a_tuple = (1, 2, 3)
a_list = list(a_tuple)
print(a_list)        # [1, 2, 3]
 
back_to_tuple = tuple(a_list)
print(back_to_tuple) # (1, 2, 3)