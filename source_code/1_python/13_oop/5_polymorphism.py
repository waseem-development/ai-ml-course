class Circle:
    def __init__(self, r): self.r = r
    def area(self): return 3.14159 * self.r ** 2 # we have the same method but it is used in a different manner for both classessssss
 
class Square:
    def __init__(self, s): self.s = s
    def area(self): return self.s ** 2 # we have the same method but it is used in a different manner for both classes
 
shapes = [Circle(3), Square(4)]
for shape in shapes: # we loop over the "shapes" list 
    print(shape.area())   # each uses its OWN area() logic
# 28.27... # area of circle
# 16 # area of square