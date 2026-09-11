# def dog_details():
#     dog_name = "Jack" # attribute

#     def bark(dog_name): # method
#         print(f"{dog_name} is a dog and dogs bark bow bow")

#     bark(dog_name)

# dog_details()
class Car():
    def __init__(self):
        pass

g_class = Car()
toyota_revo = Car()

class Dog():

    species = "Canine" # class attribute
    
    def __init__(self, name, breed): # methods
        self.name = name # instance attributes
        self.breed = breed # instance attributes

    def bark(self, dog_name): # method
        print(f"{dog_name} is a dog and dogs bark bow bow")
    
        

# Note: ***** Objects are also called instances *****

rex = Dog("rex", "Belgian Shephard")      # create an object (instantiate)
print(f"{rex.name} is a {rex.breed} breed dog and its species is {rex.species}")
rex.bark("rex")
print()
milo = Dog("milo", "Husky")     # a second, independent object
print(f"{milo.name} is a {milo.breed} breed dog and its species is {milo.species}")
milo.bark("milo")
print()
sheepu = Dog("sheepu", "Bulldog") 
print(f"{sheepu.name} is a {sheepu.breed} breed dog and its species is {sheepu.species}")
sheepu.bark("sheepu")
print()
# print(type(rex))    # <class '__main__.Dog'>
# print(rex is milo)  # False — two separate objects





age = 12312 # variables
name="a" # variables

def name(): # function
    pass 