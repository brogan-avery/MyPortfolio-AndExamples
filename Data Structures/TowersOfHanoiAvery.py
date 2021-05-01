"""
***************************************************************
* Title: Tower of Hanoi with recursion
* Author: Brogan Avery
* Created : 2021-02-07
* Course: CIS 152 - Data Structure
* Version: 1.0
* OS: macOS Catalina
* IDE: PyCharm
* Copyright : This is my own original work  based on specifications issued by the course instructor
* Description : An app that calculates how many moves a tower of hanoi game would take given the number of disks by using a recursive function
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
***************************************************************
"""

"""Recursion is when a step is repeated over and over again until a condition is met or found through the use of a 
function that calls itself. The only way I can ever understand recursion in a logical way is to think of Russian 
nesting dolls. If the goal is to find the last little one that does not open, we can think of each step we take as " 
open doll until you cannot". This step would be repeated for each doll exactly the same until the condition is met.
 In this program, a similar thing is happening. It repeats the function calling itself and preforming a set of instructions 
 util the condition where n == 1 is met."""

moveCount = 0 # used to keep track of how many moves it will take

def playGame(stick1, stick3, stick2, numOfDisks):

    global moveCount
    biggestDisk = 1 # represents the first item or the lowest / biggest disk
    if numOfDisks == biggestDisk: # sees if there is only one (or if there are more) left on the first stick
        moveCount += 1
        # print(moveCount + 1)
        return moveCount
    else:
        playGame(stick1, stick2, stick3, numOfDisks - 1,) # lowers the total number of moves left to complete the goal before calling this same method again
        moveCount += 1
        # print(moveCount + 1)
        playGame(stick2, stick3, stick1, numOfDisks - 1) # lowers the total number of moves left to complete the goal before calling this same method again
        return moveCount


# MAIN--------------------------------------------------------------------
if __name__ == '__main__':

    maxSize = int(input("Please enter how many disks you would like: "))

    # declare a list/array for each stick, since the game is not being played, this isnt really needed to make these into arrays but I am planing ahead
    stick1 = [0] * maxSize
    stick2 = [0] * maxSize
    stick3 = [0] * maxSize

    # fills the first stick with the amount of disks the user entered
    # i = 0
    # while i < maxSize:
    #     stick1[i] = i+1
    #     i+=1

    playGame(stick1, stick3, stick2, maxSize)

    print("this game will take a minimum of " , moveCount,  " moves to play" )







# def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
#     if n == 1:
#         print("Move disk 1 from rod", from_rod, "to rod", to_rod)
#         return
#     TowerOfHanoi(n - 1, from_rod, aux_rod, to_rod)
#     print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
#     TowerOfHanoi(n - 1, aux_rod, to_rod, from_rod)
#
#
# # Driver code
# n = 3
# TowerOfHanoi(n, 'A', 'C', 'B')
