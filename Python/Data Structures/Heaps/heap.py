"""
***************************************************************
* Class: MaxHeap Validation
* Author: Brogan Avery
* Created : 2021-04-13
***************************************************************
"""
class HeapValidator:
    def __init__(self, arr, size, i = 0):
        self.arr = arr # heap to validate
        self.size = size
        self.i = i

    def isHeap(self): # method that sorts the heap to validate it, makes sure all children are smaller than parent
        if self.i >= int((self.size - 2) / 2):
            return True
        if (self.arr[self.i] >= self.arr[2 * self.i + 1] and self.arr[self.i] >= self.arr[2 * self.i + 2] and self.isHeap() and self.isHeap()):
            return True
        return False
