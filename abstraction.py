from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    
# Concrete class    
class Rectangle(Shape):
    
    def __init__(self, length:int, breadth:int) -> None:
        self.length = length
        self.breadth = breadth
    
    
    def area(self) -> None:
        area = self.length * self.breadth
        print(f"Area of the rectangle is {area}")
    
    def perimeter(self) -> None:
        perimeter = 2 * (self.length + self.breadth)
        print(f"Perimeter of the rectangle is {perimeter}")


r1 = Rectangle(2,2)
r1.area()
r1.perimeter()
        
    
    