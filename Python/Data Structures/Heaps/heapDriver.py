"""
***************************************************************
* Title: Heap validator driver
* Author: Brogan Avery
* Created : 2021-04-13
* Course: CIS 152 - Data Structure
* Version: 1.0
* OS: macOS Catalina
* IDE: PyCharm
* Copyright : This is my own original work  based on specifications issued by the course instructor
* Description : An app that acceps an array and checks if it is a valid heap or not
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
***************************************************************
"""

from heap import HeapValidator

def validationMessage(testValidation):
        if testValidation.isHeap():
                return "is a valid heap"
        else:
                return "is not a valid heap"


# MAIN--------------------------------------------------------------------
if __name__ == '__main__':
        # arrays to test
        arr1 = [20,13,67,3,12,6]
        arr2 = [9,8,7,3]
        arr3 = [2,6,9,12,14,17]
        arr4 = [60,50,45,25]

        size1 = len(arr1) - 1
        size2 = len(arr2) - 1
        size3 = len(arr3) - 1
        size4 = len(arr4) - 1

        # validation objects that have the corresponding array as a var
        testValidation1 = HeapValidator(arr1,size1)
        testValidation2 = HeapValidator(arr2, size2)
        testValidation3 = HeapValidator(arr3, size3)
        testValidation4 = HeapValidator(arr4, size4)

        # get a valid or invalid message
        print("Array 1: " , validationMessage(testValidation1))
        print("Array 2: ", validationMessage(testValidation2))
        print("Array 3: ", validationMessage(testValidation3))
        print("Array 4: ", validationMessage(testValidation4))

