'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''

from math import pi

class rectangle:
    """ models a rectangle with length and width """
    def __init__(self, length, width):
        self.length = length
        self.width = width
        # self.area2 = self.width * self.length # not asked for, some experimentation

    def __str__(self):
        return f"Rectangle with length: {self.length}, width: {self.width}"

    def area(self):
        """ calculates the area of the rectangle"""
        return self.width * self.length

    def perimeter(self):
        """ calculates the perimeter of the rectangle """
        return 2 * (self.width + self.length)

class circle:
    """ models a circle by radius """
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"Circle of radius: {self.radius}"

    def area(self):
        """ calculates the area of the circle """
        return pi * self.radius**2

    def circumference(self):
        """ calculates circumference of the circle"""
        return 2 * pi * self.radius

my_rect = rectangle(10, 5)
print(my_rect)
print(f"Area = {my_rect.area()}")
print(f"Perimeter = {my_rect.perimeter()}")
# print(my_rect.area2)

my_circ = circle(5)
print(my_circ)
print(f"Area = {my_circ.area()}")
print(f"Circumference = {my_circ.circumference()}")
