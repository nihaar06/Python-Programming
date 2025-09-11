from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        return 3.14*self.r*self.r
c=Circle(3)
r=Rectangle(4,2)
print("Area of Circle: ",c.area())
print("Area of Rectangle :",r.area())