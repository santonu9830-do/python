from abc import ABC, abstractmethod
import math

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Rectangle subclass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Circle subclass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Create objects
rectangle = Rectangle(10, 5)
circle = Circle(7)

# Display areas
print("Area of Rectangle:", rectangle.area())
print("Area of Circle:", circle.area())



































