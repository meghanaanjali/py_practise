from math import pi

class Circle:
    def __init__(self,r) :
        self.r = r

    def area(self):
        return pi * (self.r ** 2)
    
    def peri(self):
        return 2 * pi * self.r 

c1 = Circle(4)  
c1.area()   
print ('Area of c1 is ',c1.area())
print ('Perimeter of c1 is ',c1.peri())