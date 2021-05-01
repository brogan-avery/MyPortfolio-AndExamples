"""
***************************************************************
* Title: Priority Queues
* Author: Brogan Avery
* Created : 2021-03-05
* Course: CIS 152 - Data Structure
* Version: 1.0
* OS: macOS Catalina
* IDE: PyCharm
* Copyright : This is my own original work  based on specifications issued by the course instructor
* Description : An app that demos list based priority queues
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
***************************************************************
"""

from priorityQueue import PriorityQueue

# MAIN--------------------------------------------------------------------
if __name__ == '__main__':

    # node data
    jobNum1 = 1111
    jobNum2 = 1112
    jobNum3 = 1113
    jobNum4 = 1114
    jobNum5= 1115
    jobNum6 = 1116
    jobNum7 = 1117
    jobNum8 = 1118
    jobNum9 = 1119

    # priority levels
    p1 = 'A'
    p2 = 'B'
    p3 = 'C'
    p4 = 'D'

    jobList = PriorityQueue()

    # add jobs to list
    jobList.enqueue(jobNum1, p2)
    jobList.enqueue(jobNum2, p2)
    jobList.enqueue(jobNum3, p2)
    jobList.enqueue(jobNum4, p4)
    jobList.enqueue(jobNum5, p4)
    jobList.enqueue(jobNum6, p4)
    jobList.enqueue(jobNum7, p4)
    jobList.enqueue(jobNum8, p1)
    jobList.enqueue(jobNum9, p1)

    jobList.print_queue()

    jobList.dequeue()
    print("\nAfter dequeue:")
    jobList.print_queue()

    jobList.dequeue()
    print("\nAfter dequeue again:")
    jobList.print_queue()











