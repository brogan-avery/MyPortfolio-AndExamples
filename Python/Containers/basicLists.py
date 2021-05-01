"""
***************************************************
Title: list one
Author: Brogan Avery
Created: 2020-01-19
Description : lists demo
OS: macOS Catalina
Copyright : This is my own original work based on specifications issued by the course instructor
***************************************************
"""
print("Original list:")
listOne = ["the", "brown", "cow"]
print(listOne)
print( "\n")

listOne.append("ran")
print("Append:")
print(listOne)
print( "\n")

listOne.remove("ran")
print("Remove:")
print(listOne)
print( "\n")

listOne_copy = listOne.copy()
print("Copy:")
print(listOne_copy)
print( "\n")

print("Count:")
print(listOne.count("the"))
print( "\n")

listOne.insert(1, "big")
print("Insert:")
print(listOne)
print( "\n")

listTwo = ["and", "the", "yellow", "cat"]
listOne.extend(listTwo)
print("Extend:")
print(listOne)
print( "\n")

print("Index, found:")
print(listOne.index("cow"))
print( "\n")

listOne.reverse()
print("reverse:")
print(listOne)
print( "\n")

listOne.sort()
print("Sort:")
print(listOne)
print( "\n")

listOne.clear()
print("Clear:")
print("Empty list:", listOne)
print( "\n")

print("Index, not found: Displays an ERROR")
print(listOne.index("cow"))
