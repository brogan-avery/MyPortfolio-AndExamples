"""
***************************************************************
* Title: Cycles
* Author: Brogan Avery
* Created : 2021-01-29
* Course: CIS 152 - Data Structure
* Version: 1.0
* OS: macOS Catalina
* IDE: PyCharm
* Copyright : This is my own original work  based on specifications issued by the course instructor
* Description : An app that prints methods of an object of a class bicycle that is based on the abstract class
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
***************************************************************
"""

from BicycleAvery import Bicycle

# MAIN--------------------------------------------------------------------
if __name__ == '__main__':

    bike = Bicycle() # new bicycle object with no args
    bike2 = Bicycle(2,1) # new bicycle object with args

    print(bike)
    print(bike2)

    # calls methods
    bike.ride()
    bike.stop()

"""
   BIG O COMPLEXITY:
   The Big O complexity is o(1) because there is nothing changeable so the time will be independent of any change because there simply is no change. 
"""
