"""
***************************************************************
* Class Name: Node
* Author: Brogan Avery
* Created: 2021-03-05
***************************************************************
"""

class Node:
    def __init__(self, jobNum, priorityLevel):
        self.jobNum = jobNum
        self.priorityLevel = priorityLevel

    def __str__(self):
        return str(self.jobNum) + " " + str(self.priorityLevel)

