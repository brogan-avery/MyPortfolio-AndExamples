"""
***************************************************************
* Title: Stack Class
* Author: Brogan Avery
* Created : 2021-02-06
* Course: CIS 152 - Data Structure
* Version: 1.0
* OS: macOS Catalina
* IDE: PyCharm
* Copyright : This is my own original work  based on specifications issued by the course instructor
* Description : An app that demonstrates stacks
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
***************************************************************
"""

from Stack import Stack
from LabCode.StackLab.StackEmptyException import StackEmptyException
from LabCode.StackLab.StackFullException import StackFullException

# MAIN--------------------------------------------------------------------
if __name__ == '__main__':

# empty stack
    stack1 = Stack(3)

    print("\nSTACK IS EMPTY: ")
    print("is empty: ", stack1.is_empty())
    print("is full: ", stack1.is_full())
    print("size: ", stack1.size())

# try to print empty stack
    try:
        print("print string: ", stack1.print_stack_up())
    except StackEmptyException:
        print("Stack is empty")
# try to print peek
    try:
        print("peek: ", stack1.peek())
    except StackEmptyException:
        print("Stack is empty")
# try to print pop
    try:
        print("pop: ", stack1.pop())
    except StackEmptyException:
        print("Stack is empty")

# add to it
    print("\nADD TO STACK: ")
    stack1.push("item 1")
    stack1.push("item 2")
    stack1.push("item 3")

# try to add to a full list
    try:
        stack1.push("item 4")
    except StackFullException:
        print("Stack is full")
    print("print string: ", stack1.print_stack_up())

    print("is empty: ", stack1.is_empty())
    print("is full: ", stack1.is_full())
    print("size: ", stack1.size())
    print("peek: ", stack1.peek())
    print("print string: ", stack1.print_stack_up())
    print("item popped: ", stack1.pop())
    print("print string after pop: ", stack1.print_stack_up())










