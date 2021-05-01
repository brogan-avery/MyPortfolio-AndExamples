"""
***************************************************************
* Title: Binary Search Tree
* Author: Brogan Avery
* Created : 2021-03-18
* Course: CIS 152 - Data Structure
* Version: 1.0
* OS: macOS Catalina
* IDE: PyCharm
* Copyright : This is my own original work  based on specifications issued by the course instructor
* Description : An app that demonstrates a binary tree and node class to sort and traverse through an ordered list of names
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
***************************************************************
"""
from Node import Node
from queue import Queue

# MAIN--------------------------------------------------------------------
if __name__ == '__main__':
# BOYS
    print("BOYS:")
    rootNode = Node(1, "Noah") # makes a node based on first boy
    boysNameTree = rootNode  # 'grows' a tree from the root
    # declares unconnected / unattached nodes to latter add to tree
    node2 = Node(2, "Liam")
    node3 = Node(3, "Mason")
    node4 = Node(4, "Jacob")
    node5 = Node(5, "William")
    node6 = Node(6, "Ethan")
    node7 = Node(7, "James")
    node8 = Node(8, "Alexander")
    node9 = Node(9, "Michael")
    node10 = Node(10, "Benjamin")

    # add the nodes that has the number and name to a tree in a 'pseudo-random' order
    boysNameTree.insert(node9)
    boysNameTree.insert(node6)
    boysNameTree.insert(node3)
    boysNameTree.insert(node2)
    boysNameTree.insert(node7)
    boysNameTree.insert(node4)
    boysNameTree.insert(node5)
    boysNameTree.insert(node10)
    boysNameTree.insert(node8)

    # prints the tree in a sorted order
    boysNameTree.printTree()
    print()

    # search for some specific names
    name1 = boysNameTree.search("Noah")
    name2 = boysNameTree.search("James")
    name3 = boysNameTree.search("Jacob")
    name4 = boysNameTree.search("Brogan")

    namesToTest = [name1,name2,name3,name4] # add search results to a list to validate and print

    for name in namesToTest:
        if name != None:
            print(name.sData, "Found at node:", name.iData) # if found
        else:
            print("Name not found") # if not found


# GIRLS
    print("\nGIRLS:")
    rootNode = Node(1, "Emma")  # makes a node based on first girl
    girlsNameTree = rootNode  # 'grows' a tree from the root
    # declares unconnected / unattached nodes to latter add to tree
    node2 = Node(2, "Olivia")
    node3 = Node(3, "Sophia")
    node4 = Node(4, "Ava")
    node5 = Node(5, "Isabella")
    node6 = Node(6, "Mia")
    node7 = Node(7, "Abigail")
    node8 = Node(8, "Emily")
    node9 = Node(9, "Charlotte")
    node10 = Node(10, "Harper")

    # add the nodes that has the number and name to a tree in a 'pseudo-random' order
    girlsNameTree.insert(node9)
    girlsNameTree.insert(node6)
    girlsNameTree.insert(node3)
    girlsNameTree.insert(node2)
    girlsNameTree.insert(node7)
    girlsNameTree.insert(node4)
    girlsNameTree.insert(node5)
    girlsNameTree.insert(node10)
    girlsNameTree.insert(node8)

    # prints the tree in a sorted order
    girlsNameTree.printTree()
    print()

    # search for some specific names
    name1 = girlsNameTree.search("Ava")
    name2 = girlsNameTree.search("Emma")
    name3 = girlsNameTree.search("Emily")
    name4 = girlsNameTree.search("Brogan")

    namesToTest = [name1, name2, name3, name4]  # add search results to a list to validate and print

    for name in namesToTest:
        if name != None:
            print(name.sData, "Found at node:", name.iData)  # if found
        else:
            print("Name not found")  # if not found

# DFS
    # imagine a cursor object that goes to the left child of the "current root" until the left child is null.
    # It will not pick up that object until it visits the node for a second time.
    # the same is repeated for the right
    print("\nDFS")
    boysNameTree.dfs()

# BFS
    # this time, the cursor object is going to check if a node has a left child and if it has a right child, if it has either, it will pick them up in that order,
    # then with recursion, it checks the same thing for any of its children, each time, it adds the value to a list to return
    bfsList_empty = []
    print("\nBFS")
    bfsList = boysNameTree.bfs(bfsList_empty)
    for name in bfsList:
        print("Popularity Rank:", name.iData, " Name:", name.sData)



