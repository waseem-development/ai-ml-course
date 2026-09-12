# The @property approach makes the controlled access look like normal attribute access, which is why it's often more convenient and Pythonic.

# class Account:
#     def __init__(self, owner, balance):
#         self.owner = owner        # public
#         self._balance = balance   # "internal" by convention
#         self.__pin = "4471"       # name-mangled, hard to reach

# class Dog:
#     def __init__(self, name, breed, nickname):
#         self.owner = name          # public
#         self._breed = breed        # internal / protected by convention
#         self.__nickname = nickname # name-mangled

# class Car:
#     def __init__(self, owner, model, nickname):
#         self.owner = owner
#         self._model = model
#         self.__nickname = nickname

# acc = Account("Ahmed", 1000)
# print(acc.owner)          # "Ahmed" — fine, it's public
# print(acc._balance)       # works, but signals "you shouldn't":: This is intended for internal use. As if you are sayign "other programmers, please don't directly access it unless you know what you're doing"

# print(acc.__pin)          # AttrsibuteError — mangled to _Account__pin
# # print(acc._Account__pin)  # Would work: 4471


# Getter: this gets the data of the current object/instance 
# Setter: Modifies or sets the value of your particular attribute for that particular object


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.__marks = 0
#         self.set_marks(marks)

#     def get_marks(self):
#         return self.__marks

#     def set_marks(self, marks):
#         if 0 <= marks <= 100:
#             self.__marks = marks
#         else:
#             raise ValueError("Come on  man Marks must be between 0 and 100")


# student = Student("Waseem", 85)

# print(student.get_marks())

# student.set_marks(92)
# print(student.get_marks())

# student.set_marks(150)   # Invalid




class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    @property # this tells python that this is a getter method
    def salary(self):              # Getter
        return self._salary

    @salary.setter
    def salary(self, amount):      # Setter
        if amount >= 0:
            self._salary = amount
        else:
            raise ValueError("Salary cannot be negative!")


employee = Employee("Waseem", 50000)

print(employee.salary)     # Getter

employee.salary = 60000    # Setter
print(employee.salary)

employee.salary = -1000    # Invalid