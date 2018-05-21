class Rectangle:

    def __init__ (self, l, b):
        self.l = l
        self.b = b

    def area (self):
        return self.l * self.b
    
    def peri (self):
        return 2 * (self.l + self.b)

r1 = Rectangle (2,3)
print ('Area of r1 is ',r1.area())
print ('Perimeter of r1 is ',r1.peri())
