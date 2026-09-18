class Animal:
    def __init__(self, name):
        self.name = name
 
    def eat(self):
        print(f"{self.name} is eating")
 
class Cat(Animal):     # Cat inherits from Animal
    pass
 
# whiskers = Cat("Whiskers")
# whiskers.eat()                  # inherited — works with no rewrite
# isinstance(whiskers, Animal)    # True





class Animal:
    def __init__(self, name):
        self.name = name
# animal is the parent class, cat is the child class
class Cat(Animal): 
    def __init__(self, name, indoor):
        super().__init__(name)   # reuse the parent's setup
        self.indoor = indoor     # then add Cat-specific data
 
# whiskers = Cat("Whiskers", True)
# print(whiskers.name)     # "Whiskers" — handled by Animal
# print(whiskers.indoor)   # True — handled by Cat














class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class AdminUser(User):
    def __init__(self, name, email, permissions):
        super().__init__(name, email)  # User handles name + email
        self.permissions = permissions # Admin adds permissions


admin = AdminUser("Paxto", "paxto@email.com", ["delete", "ban"])

# print(admin.name)          # Paxto
# print(admin.email)         # paxto@email.com
# print(admin.permissions)   # ["delete", "ban"]























class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class DigitalProduct(Product):
    def __init__(self, name, price, download_url):
        super().__init__(name, price)
        self.download_url = download_url

# course = DigitalProduct(
#     "Python Course",
#     20,
#     "example.com/download"
# )


















class Model:
    def __init__(self, name):
        self.name = name
        self.trained = False


class ImageClassifier(Model):
    def __init__(self, name, classes):
        super().__init__(name)
        self.classes = classes

# model = ImageClassifier(
#     "Cat Classifier",
#     ["Bengal", "Siamese", "Persian"]
# )














class Animal:
    def speak(self): # same method for both parent and child classes
        print("Some generic animal sound")
 
class Dog(Animal):
    def speak(self):       # overrides Animal.speak: It will override the parent's this "speak" method
        print("Woof!")

# Animal().speak()   # Some generic animal sound
# Dog().speak()      # Woof! This is called   overriding








class Flyer:
    def move(self):
        print("Flying")


class Swimmer:
    def move(self):
        print("Swimming")


class Duck(Swimmer, Flyer):

    def move(self):
        Flyer.move(self)
        Swimmer.move(self)


Duck().move()   # shows the full search order: MRO = Method Resolution Order