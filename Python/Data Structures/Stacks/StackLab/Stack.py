"""
***************************************************************
* Class Name: Stack
* Author: Brogan Avery
* Created: 2021-02-05
***************************************************************
"""
from LabCode.StackLab.StackEmptyException import StackEmptyException
from LabCode.StackLab.StackFullException import StackFullException


class Stack:
    def __init__(self, max_size=5):
        self.top = -1
        self.max_size = max_size  # the max number of items than can go into the stack
        self.items = [" " for x in range(max_size)]  # making the stack more like a C++ array

    def is_empty(self): # boolean
        return self.top == -1

    def is_full(self): # boolean
        return self.top == self.max_size - 1  # returns a boolean true or false if the the index of the object at the top of the stack is same as the last index possible in the stack.

    def push(self, item):
        if self.is_full() == True:
           raise StackFullException()
        else:
            self.top = self.top + 1 # makes a new top and then puts the value of item into that spot
            self.items[self.top] = item

    def pop(self): # does the exact opposite of push()
        item_str = " "
        if self.is_empty() == True:
            raise StackEmptyException()
        else:
            topVal = self.items[self.top] # for testing only
            self.items[self.top] = " " # emptys the spot the top was in by redeclaring it back to an empty string
            self.top = self.top - 1
            return topVal

# I had to change this one even though we were not supposed to
    def peek(self):
        if not self.is_empty():
            #self.top = self.top - 1
            return self.items[self.top]
        else:
            raise StackEmptyException()

    def size(self):
        return self.top + 1

    def print_stack_up(self):
        i = 0
        stack_str = ""

        if self.is_empty() == True:
            raise StackEmptyException()
        else:
            while i < self.max_size:
                stack_str = stack_str + self.items[i] +"\n"
                i = i + 1
            return stack_str  # Possibly you will remove this line, this is for running Unit Tests before writing code