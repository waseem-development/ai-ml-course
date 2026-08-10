# nested_list = [[1,2,3], [4,5,6]]

# for nes_list in nested_list:
#     for each_element in nes_list:
#         print(each_element)

# for i in nested_list:
#     print(i)

for row in range(1, 10):
    for column in range(1,row+1):
        print(column, end=" ")
    print()
