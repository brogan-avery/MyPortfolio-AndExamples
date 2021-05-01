"""
***************************************************************
* Class Name: Node
* Author: Brogan Avery
* Created: 2021-03-18
***************************************************************
"""
from queue import Queue

class Node:
    def __init__(self, iData = None, sData = None):
        self.sData = sData # string data
        self.iData = iData # int data
        self.left = None # left child
        self.right = None # right child

    # compares the in-value node to the "current root" node
    def insert(self,node): # New node that is not yet on tree
        if self.iData: # currentRootNode.iData
            if node.iData < self.iData: # uses pre order to traverse left branch first
                if self.left is None: # self.left = the left child of the "current root" node
                    self.left = node # sets the left child to the data of the new node
                else:
                    self.left.insert(node) # method calls self using the left child of the "current root" node as the new "current root" node
            elif node.iData > self.iData:
                if self.right is None: # self.right = the right child of the "current root" node
                    self.right = node # sets the right child to the data of the new node
                else:
                    self.right.insert(node) # method calls self using the right child of the "current root" node as the new "current root" node
        else:
            self = node # node becomes root node(self node) (top of a child-parent node triangle)

    def search(self,searchFor): # string of a name user is looking for
        if searchFor == self.sData: # compares the string being searched for to the string value of the "current root" node
            return self
        else:
            if self.left: # if this "current root" node has a left child that exists:
                leftResult = self.left.search(searchFor) # calls this method for the left child, saves return value to var
                if leftResult == None:
                    pass
                else:
                    return leftResult
            if self.right:
                rightResult = self.right.search(searchFor)
                if rightResult == None:
                    pass
                else:
                    return rightResult
            return None

    def printTree(self):
        if self.left:
            self.left.printTree()
        print("idata:", self.iData, " sdata:", self.sData)
        if self.right:
            self.right.printTree()

    def dfs(self,list): # recursive in order DFS traversal
        if self.left:
            self.left.dfs(list)
        #print("idata:", self.iData, " sdata:", self.sData)
        list.append(self)
        if self.right:
            self.right.dfs(list)
        return list

    def bfs(self, list): # recursive BFS traversal
        if not list: # to add first root node if list is empty
            list.append(self)

    # if the node has a left child it will add it to the list, if it has a right child, it will add it to the list
        if self.left:
            if self.left != None:
                list.append(self.left)
                if self.right:
                    if self.right != None:
                        list.append(self.right)
                self.left.bfs(list)
                self.right.bfs(list)

        elif self.right:
            if self.right != None:
                list.append(self.right)
                self.right.bfs(list)
        return list

    def decision_tree_results(self,list):
        list = self.dfs(list) # gets the list in order of the the nodes
        for response in list:
            if response.sData == "no": # if a response to a question is no, it returns false because the object is not a planet
                return False
        # if response is yes, returns true
        return True




