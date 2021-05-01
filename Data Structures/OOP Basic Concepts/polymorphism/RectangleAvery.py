"""
***************************************************************
* Class Name: Rectangle
* Author: Brogan Avery
* Created: 2021-02-03
***************************************************************
"""
from MeasurementsAvery import Measurements

class Rectangle(Measurements):

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def perimeter(self):
        perimeter = (2 * self._width) + (2 * self._length)
        return "The perimeter of the rectangle is " + str(perimeter)

    def area(self):
        area = self._width * self._length
        return "The area of the rectangle is " + str(area)

    def __str__(self):
        return "Rectangle: Length - " + str(self._length) + ", Width -  " + str(self._width) + ", " + self.perimeter() + ", " + self.area()





