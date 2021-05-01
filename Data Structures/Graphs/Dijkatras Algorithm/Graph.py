"""
***************************************************************
* Class Name: Graph
* Author: Brogan Avery
* Created: 2021-03-25
***************************************************************
"""

class Graph:
    def __init__(self, numNodes):
        self.numNodes = numNodes # number of nodes on the graph
        self.graph = [] # empty list to store lists that contain 2 nodes and an edge

    def add_edge(self, nodeA, nodeB, edgeBetween): # an edge can also be like a row of a graph/dict
        self.graph.append([nodeA, nodeB, edgeBetween]) # add a list that represents node A, Node B, and the distance or weight between

    def find(self, nodeCountList, i):
        if nodeCountList[i] == i:
            return i
        return self.find(nodeCountList, nodeCountList[i])

    def apply_union(self, nodeCountList, rank, x, y): # adds parents to children
        xroot = self.find(nodeCountList, x)
        yroot = self.find(nodeCountList, y)
        if rank[xroot] < rank[yroot]:
            nodeCountList[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            nodeCountList[yroot] = xroot
        else:
            nodeCountList[yroot] = xroot
            rank[xroot] += 1

    def kruskals_algo(self):
        result = []
        i, i2 = 0, 0 # index places
        # print(self.graph)
        self.graph = sorted(self.graph, key=lambda item: item[2])
        nodeCountList = [] # will be a count for the number of nodes on graph, ex: [0,1,2,3,4,5,6,7,8,9]
        rank = [] # will fill with 0s
        for node in range(self.numNodes):
            nodeCountList.append(node)
            rank.append(0)
        while i2 < self.numNodes - 1:
            nodeA, nodeB, edgeBetween = self.graph[i] # adds edge list to graph list
            i = i + 1
            x = self.find(nodeCountList, nodeA.iData)
            y = self.find(nodeCountList, nodeB.iData)
            if x != y:
                i2 = i2 + 1
                result.append([nodeA.sData, nodeB.sData, edgeBetween]) # adds lists to list
                self.apply_union(nodeCountList, rank, x, y)
        return result

