"""
***************************************************************
* Title: first come first serve tickets
* Author: Brogan Avery
* Created : 2021-02-21
* Course: CIS 152 - Data Structure
* Version: 1.0
* OS: macOS Catalina
* IDE: PyCharm
* Copyright : This is my own original work  based on specifications issued by the course instructor
* Description : An app that uses a queue to give tickets to customers until they run out
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
***************************************************************
"""
from Queue import Queue
from random import randrange

# MAIN--------------------------------------------------------------------
if __name__ == '__main__':
# the instructions did not specify to use the language built in queue or not so I am taking the safe route and using my custom queue class

    maxSize = 1000 # up to 1000 people are allowed to stand in line.
    numPeople = randrange(1,maxSize + 1) # the range in python stops one before the second number, so to end at 1000, i have to put 1001
    theLine = Queue(maxSize) # make the queue of 1000 to put up to 1000 people in
    unhappyCustomers = 0 # used to track the people who leave the line from not being able to get enough tickets

    for person in range(1,numPeople): # fills the line with how ever many people get in line
        theLine.enqueue(person)

    theLineStartSize = theLine.get_size() # how many people got in line
    print(theLineStartSize, "people are in the line ")

# ===== SCENARIO 1 =====
    numTicketsLeft = 10 # total available tickets left to purchase

    for person in range(1,numPeople):
        while numTicketsLeft != 0:
            numTicketsWanted = randrange(1, 5)  # for each person
            print("The next person in line wants", numTicketsWanted)
            if numTicketsLeft >= numTicketsWanted:
                numTicketsLeft = numTicketsLeft - numTicketsWanted
                print("The person was given", numTicketsWanted)
                print("There are now ", numTicketsLeft, "left to sell")
                theLine.dequeue()
            else:
                print("Sorry, we do not have the number of tickets you requested. Get Lost.") # i am assuming that if a person wants 4 tickets and only 2 are left they will just leave and not buy only 2 since that would leave out their friends and thats mean :(
                theLine.dequeue()
                unhappyCustomers = unhappyCustomers + 1 # so I can subtract from the total number of people served since they leave the line but do not buy tickets. We just assume they are angry and leave.

    if numTicketsLeft == 0:
        print("SOLD OUT")

    theLineEndSize = theLine.get_size() # how many people were left in line
    numPeopleSoldTo = theLineStartSize - theLineEndSize - unhappyCustomers # gets the number of people that bought tickets (removes the people who left because they could not buy enough)

    print(numPeopleSoldTo, "people bought tickets")
    print("there are",numTicketsLeft, "left unsold")



# ==== SCENARIO 2 ====
    numTicketsLeft = 100  # total available tickets left to purchase

    for person in range(1, numPeople):
        while numTicketsLeft != 0:
            numTicketsWanted = randrange(1, 5)  # for each person
            print("The next person in line wants", numTicketsWanted)
            if numTicketsLeft >= numTicketsWanted:
                numTicketsLeft = numTicketsLeft - numTicketsWanted
                print("The person was given", numTicketsWanted)
                print("There are now ", numTicketsLeft, "left to sell")
                theLine.dequeue()
            else:
                print(
                    "Sorry, we do not have the number of tickets you requested. Get Lost.")  # i am assuming that if a person wants 4 tickets and only 2 are left they will just leave and not buy only 2 since that would leave out their friends and thats mean :(
                theLine.dequeue()
                unhappyCustomers = unhappyCustomers + 1  # so I can subtract from the total number of people served since they leave the line but do not buy tickets. We just assume they are angry and leave.

    if numTicketsLeft == 0:
        print("SOLD OUT")

    theLineEndSize = theLine.get_size()  # how many people were left in line
    numPeopleSoldTo = theLineStartSize - theLineEndSize - unhappyCustomers  # gets the number of people that bought tickets (removes the people who left because they could not buy enough)

    print(numPeopleSoldTo, "people bought tickets")
    print("there are", numTicketsLeft, "left unsold")


# ==== SCENARIO 3 ====
    numTicketsLeft = 1000  # total available tickets left to purchase

    for person in range(1, numPeople):
        while numTicketsLeft != 0:
            numTicketsWanted = randrange(1, 5)  # for each person
            print("The next person in line wants", numTicketsWanted)
            if numTicketsLeft >= numTicketsWanted:
                numTicketsLeft = numTicketsLeft - numTicketsWanted
                print("The person was given", numTicketsWanted)
                print("There are now ", numTicketsLeft, "left to sell")
                theLine.dequeue()
            else:
                print(
                    "Sorry, we do not have the number of tickets you requested. Get Lost.")  # i am assuming that if a person wants 4 tickets and only 2 are left they will just leave and not buy only 2 since that would leave out their friends and thats mean :(
                theLine.dequeue()
                unhappyCustomers = unhappyCustomers + 1  # so I can subtract from the total number of people served since they leave the line but do not buy tickets. We just assume they are angry and leave.

    if numTicketsLeft == 0:
        print("SOLD OUT")

    theLineEndSize = theLine.get_size()  # how many people were left in line
    numPeopleSoldTo = theLineStartSize - theLineEndSize - unhappyCustomers  # gets the number of people that bought tickets (removes the people who left because they could not buy enough)

    print(numPeopleSoldTo, "people bought tickets")
    print("there are", numTicketsLeft, "left unsold")
