def dog_details():
    dog_name = "Jack" # attribute

    def bark(dog_name): # method
        print(f"{dog_name} is a dog and dogs bark bow bow")

    bark(dog_name)

dog_details()


class Dog:
    pass    # empty class for now
 
rex = Dog()      # create an object (instantiate)
milo = Dog()     # a second, independent object
 
print(type(rex))    # <class '__main__.Dog'>
print(rex is milo)  # False — two separate objects