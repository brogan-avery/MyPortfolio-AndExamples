"""
***************************************************************
* Title: Binary Search Decision Tree
* Author: Brogan Avery
* Created : 2021-03-25
* Course: CIS 152 - Data Structure
* Version: 1.0
* OS: macOS Catalina
* IDE: PyCharm
* Copyright : This is my own original work  based on specifications issued by the course instructor
* Description : An app that uses a binary search tree from previous assignments and modifies it to be used for a decision making tree. In this cass, it decides if an object is a planet or not by calling a method in the node class
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
***************************************************************
"""
from NodeForDecTree import Node

class Planet:
    def __init__(self, crt1, crt2, ctr3):
        self.crt1 = crt1 # criteria to be met (questions asked)
        self.crt2 = crt2
        self.crt3 = ctr3

def is_it_a_planet(planet):
    # Does it orbit the sun?
    if planet.crt1 == "yes":
        decisionTree = Node(1, "yes")
    else:
        decisionTree = Node(1, "no")

    # does it stay round?
    if planet.crt2 == "yes":
        decisionTree.insert(Node(2, "yes"))
    else:
        decisionTree.insert(Node(2, "no"))

    # has it cleared the area of space around it?
    if planet.crt3 == "yes":
        decisionTree.insert(Node(3, "yes"))
    else:
        decisionTree.insert(Node(3, "no"))

    # Returns results
    list = []
    if decisionTree.decision_tree_results(list) == True:
        return "IS a planet"
    else:
        return "is NOT a planet"


# MAIN--------------------------------------------------------------------
if __name__ == '__main__':

    mars = Planet("yes", "yes", "yes")
    pluto = Planet("yes", "yes", "no")
    someSpaceJunk = Planet("no", "no", "no")

    print("Mars", is_it_a_planet(mars))
    print("Pluto", is_it_a_planet(pluto))
    print("Piece of space junk", is_it_a_planet(someSpaceJunk))
