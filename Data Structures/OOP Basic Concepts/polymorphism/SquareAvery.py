"""
***************************************************************
* Class Name: Square
* Author: Brogan Avery
* Created: 2021-02-03
***************************************************************
"""

from MeasurementsAvery import Measurements

class Square(Measurements):

    def __init__(self, side):
        self._side = side

    def perimeter(self):
        perimeter = self._side * 4
        return "The perimeter of the square is " + str(perimeter)

    def area(self):
        area = self._side * self._side
        return "The area of the square is " + str(area)

    def __str__(self):
        return "Square: Length of sides - " + str(self._side) + ", " + self.perimeter() + ", " + self.area()


