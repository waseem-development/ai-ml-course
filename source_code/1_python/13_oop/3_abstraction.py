from abc import ABC, abstractmethod # ABC (Abstract Base Class) tells Python: "This is an abstract class. It is meant to be a blueprint for other classes, not something we directly create objects from."
 
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass    # no implementation — subclasses must provide one
 
# shape = Shape()   # TypeError — can't instantiate an ABC
 
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return 3.14159 * self.radius ** 2
 
# Circle(3).area()   # 28.27...


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# # You cannot create an object of an abstract class
animal = Animal()   # TypeError