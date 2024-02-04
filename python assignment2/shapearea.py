#Shape Area Calculator
import math

class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius
square = Square(5)
rectangle = Rectangle(4, 6)
circle = Circle(3)

print(f"Area of square: {square.area()}")
print(f"Area of rectangle: {rectangle.area()}")
print(f"Area of circle: {circle.area()}")
