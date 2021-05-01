"""
***************************************************************
* Title: Priority Queue DMV App
* Author: Brogan Avery
* Created : 2021-03-05
* Course: CIS 152 - Data Structure
* Version: 1.0
* OS: macOS Catalina
* IDE: PyCharm
* Copyright : This is my own original work  based on specifications issued by the course instructor
* Description : An app that demos list based priority queues to make a priorities list of people in line at the DMV
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
***************************************************************
"""

from queue import PriorityQueue
from random import randrange

# MAIN--------------------------------------------------------------------
if __name__ == '__main__':
    line = PriorityQueue()

    numCustomers = 100

    # fill queue with 100 people
    for i in range(numCustomers):
        priority = randrange(1, 6)
        line.put((priority, "Customer Number: " + str(i)))

    # print them in priority order
    for i in range(numCustomers):
        print(line.get())



