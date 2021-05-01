"""
***************************************************************
* Title: Dijkstra's Algorithm
* Author: Brogan Avery
* Created : 2021-04-06
* Course: CIS 152 - Data Structure
* Version: 1.0
* OS: macOS Catalina
* IDE: PyCharm
* Copyright : This is my own original work  based on specifications issued by the course instructor
* Description : An app that demonstrates Dijkstra's algo to show the min distance from point a to all other points on the graph
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
***************************************************************
"""
from Graph import Graph
from Node import Node
import sys
from MatrixGraph import MatrixGraph
# MAIN--------------------------------------------------------------------
if __name__ == '__main__':
    # creates a node for each city
    ames = Node(0, "Ames, IA")
    dsm = Node(1, "Des Moines, IA")
    austin = Node(2, "Austin, TX")
    dallas = Node(3, "Dallas, TX")
    atlanta = Node(4, "Atlanta, GA")
    savannah = Node(5, "Savannah, GA")
    sanDiego = Node(6, "San Diego, CA")
    losAng = Node(7, "Los Angeles, CA")
    madison = Node(8, "Madison, WI")
    greenBay = Node(9, "Green Bay, WI")
    cities = [ames, dsm, austin, dallas, atlanta, savannah, sanDiego, losAng, madison, greenBay]

    # creates a graph that represents rows of lists that each contain 2 node objects and one int for distance
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

    # makes lists for each city that shows what city(s) you can go to from that city
    from0 = []
    from1 = []
    from2 = []
    from3 = []
    from4 = []
    from5 = []
    from6 = []
    from7 = []
    from8 = []
    from9 = []

    # will eventually hold the matrix values
    froma = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fromb = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fromc = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fromd = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    frome = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fromf = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fromg = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fromh = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fromi = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    fromj = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    fromMatrix = [froma, fromb, fromc, fromd, frome, fromf, fromg, fromh, fromi, fromj]

    # makes mini (paired) lists of a to location and its distance from the from location
    for edge in roadMap.graph:
        if edge[0].iData == 0:
            from0.append([edge[1],edge[2]])
        if edge[0].iData == 1:
            from1.append([edge[1],edge[2]])
        if edge[0].iData == 2:
            from2.append([edge[1],edge[2]])
        if edge[0].iData == 3:
            from3.append([edge[1],edge[2]])
        if edge[0].iData == 4:
            from4.append([edge[1],edge[2]])
        if edge[0].iData == 5:
            from5.append([edge[1],edge[2]])
        if edge[0].iData == 6:
            from6.append([edge[1],edge[2]])
        if edge[0].iData == 7:
            from7.append([edge[1],edge[2]])
        if edge[0].iData == 8:
            from8.append([edge[1],edge[2]])
        if edge[0].iData == 9:
            from9.append([edge[1],edge[2]])

    fromLists = [from0, from1, from2, from3, from4, from5, from6, from7, from8, from9]

    # gets all of the nodes that this node can go to and the distance between them and then replaces the distances in the matrix graph
    i = 0
    for pairedList in fromLists:
        for item in pairedList:
            fromMatrix[i][item[0].iData] = item[1]
        i = i + 1

    # will contain the fromMatrix values but swapping the rows and columns so that I can replace the zeros in ( like a punit square or multiplication table kind of)
    transposedFromMatrix = []

    # fills the transposed Matrix
    i = 0
    for c in range(10):
        rowList = []
        for row in fromMatrix:
            rowList.append(row[i])
        i = i + 1
        transposedFromMatrix.append(rowList)

    mapMatrixList = [] # will hold that values that will go into the actual MatrixGraph class

    # fills in the indexes from the transposed matrix
    for x in range(10):
        row = []
        for i in range(10):
            if transposedFromMatrix[x][i] != 0:
                row.append(transposedFromMatrix[x][i])
            elif fromMatrix[x][i] != 0:
                row.append(fromMatrix[x][i])
            else:
                row.append(0)
        mapMatrixList.append(row)

    # creates a square-matrix style graph from the normal graph to go into the Prim's algo function
    mapMatrix = MatrixGraph(10)

    mapMatrix.graph = mapMatrixList # sets the graph to the new matrix that was just created

    startNode = mapMatrix.dijkstras_algo()

    # formatting output
    for i in range(mapMatrix.numNodes):
        print("Distance from", cities[0].sData, "-", cities[i].sData, ":", startNode[i], "miles")
