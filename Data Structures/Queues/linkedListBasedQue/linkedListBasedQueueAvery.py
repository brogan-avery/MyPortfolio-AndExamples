"""
***************************************************************
* Title: Linked List Based Queues
* Author: Brogan Avery
* Created : 2021-03-1
* Course: CIS 152 - Data Structure
* Version: 1.0
* OS: macOS Catalina
* IDE: PyCharm
* Copyright : This is my own original work  based on specifications issued by the course instructor
* Description : An app that demos a queue being implemented as a linked list rather than an array ( in pythonic and c++ kind of like ways)
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
***************************************************************
"""
from Queue import Queue


# MAIN--------------------------------------------------------------------
if __name__ == '__main__':
# I was not quite sure how to go about this one in python so I just used the custom queue class and modified it a bunch to use with a linked list instead of an array since that seems to make the most sense

    myLinkedList = Queue() # declare an actual linked list in python vs an array like list
    print(myLinkedList) # print out to show that the linked list is empty

    myLinkedList.enqueue("item 1") # adds 1st item to queue
    myLinkedList.enqueue("item 2") # adds 2nd item to queue
    myLinkedList.enqueue("item 3") # adds 3rd item to queue
    myLinkedList.enqueue("item 4") # adds 4th item to queue
    print(myLinkedList) # shows the 4 items are in the queue in the order they were added

    myLinkedList.dequeue() # removes the first item that went into the queue
    print(myLinkedList)

    print(myLinkedList.peek()) # the way the peek at the top of the stack is implemented

    print(myLinkedList.size) # size of queue

    print(myLinkedList.is_empty()) # is empty method

    # there (in theory) is no "full point" in the linked list memory space permitting I guess

    myLinkedList.print_queue() # print out each item in order