# def total(*args): # *args creates a tuple
#     for i in args:
#         print(i)

#     print(type(args))    # <class 'tuple'>
#     return sum(args)
 
# total(4, 9)              # 13
# total(1, 2, 3, 4, 5)     # 15
# total()                  # 0


def build_profile(**kwargs):
    print(kwargs)
    print(type(kwargs))   # <class 'dict'>
    return kwargs
 
build_profile(name="Ahmed", age=25)
# {'name': 'Ahmed', 'age': 25}
 
build_profile(city="Karachi")
# {'city': 'Karachi'}s