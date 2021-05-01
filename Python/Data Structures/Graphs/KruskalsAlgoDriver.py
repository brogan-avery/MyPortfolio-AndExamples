"""
***************************************************************
* Title: Kruskal's Algorithm
* Author: Brogan Avery
* Created : 2021-03-25
* Course: CIS 152 - Data Structure
* Version: 1.0
* OS: macOS Catalina
* IDE: PyCharm
* Copyright : This is my own original work  based on specifications issued by the course instructor
* Description : An app that demonstrates Kruskals's algo to get the MST for a graph. Does this through a pretend USA road map.
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
***************************************************************
"""

from Graph import Graph
from Node import Node

# MAIN--------------------------------------------------------------------
if __name__ == '__main__':
    # creates a node for each city
    ames = Node(0,"Ames, IA")
    dsm = Node(1, "Des Moines, IA")
    austin = Node(2,"Austin, TX")
    dallas = Node(3, "Dallas, TX")
    atlanta = Node(4, "Atlanta, GA")
    savannah = Node(5, "Savannah, GA")
    sanDiego = Node(6, "San Diego, CA")
    losAng = Node(7, "Los Angeles, CA")
    madison = Node(8, "Madison, WI")
    greenBay = Node(9, "Green Bay, WI")

    roadMap = Graph(10)  # 10 cites/ nodes to go on graph
    roadMap.add_edge(ames, dsm, 30)  # 30 miles from ames to des moines
    roadMap.add_edge(austin, dallas, 100)
    roadMap.add_edge(atlanta, savannah, 50)
    roadMap.add_edge(sanDiego, losAng, 80)
    roadMap.add_edge(madison, greenBay, 80)
    roadMap.add_edge(dsm, austin, 800)
    roadMap.add_edge(austin, greenBay, 1000)
    roadMap.add_edge(losAng, dallas, 500)
    roadMap.add_edge(losAng, atlanta, 2000)
    roadMap.add_edge(dallas, greenBay, 1100)
    roadMap.add_edge(ames, madison, 500)
    roadMap.add_edge(ames, savannah, 950)
    roadMap.add_edge(ames, sanDiego, 1150)

    listOfEdges = roadMap.kruskals_algo()

    for edge in listOfEdges:
        print(edge[0], " to ", edge[1], ":", edge[2], "miles")

    # just demonstrates that a graph is a list of lists that contain 2 node objects and 1 int representing the distance between
    for x in roadMap.graph:
        print(x)