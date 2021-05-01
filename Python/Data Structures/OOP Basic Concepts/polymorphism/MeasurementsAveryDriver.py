"""
***************************************************************
* Title : Measurements
* Author: Brogan Avery
* Created : 2021-02-03
* Course: CIS 152 - Data Structure
* Version: 1.0
* OS: macOS Catalina
* IDE: PyCharm
* Copyright : This is my own original work based on specifications issued by the course instructor
* Description : An app that lets users calculate the area and perimeter of a square or rectangle
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
***************************************************************
"""
from RectangleAvery import Rectangle
from SquareAvery import Square

# MAIN--------------------------------------------------------------------
if __name__ == '__main__':

    squareObj = Square(3)
    rectangleObj = Rectangle(3,4)

    print(squareObj)
    print(rectangleObj)

    """
    BIG O COMPLEXITY:
    The big O complexity is o(1) because the only n value is the size of the legnth and width and that will not affect the time in any meaningful way ever. 
    
    """