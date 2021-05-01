"""
***************************************************************
* Title: Search and sort timing
* Author: Brogan Avery
* Created : 2021-03-09
* Course: CIS 152 - Data Structure
* Version: 1.0
* OS: macOS Catalina
* IDE: PyCharm
* Copyright : This is my own original work  based on specifications issued by the course instructor
* Description : An app that demonstrates search and sort algorithms as well as compares the timing between different ones
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
***************************************************************
"""

from random import randrange
from datetime import datetime

# taken from: https://www.geeksforgeeks.org/python-program-for-linear-search/
def linear_search(arr, x): # params are the array and the number looking for
    i = 0
    for i in range(len(arr)): # starts at one and checks each till it is found first
        if arr[i] == x:
            return i # returns index location
    else:
        return "Not found"

# taken from https://www.geeksforgeeks.org/python-program-for-binary-search/
def binary_search(arr, low, high, x): # the list, 0/ first index, last index/ length -1, the value being looked for
    # Check base case
    if high >= low:
        mid = (high + low) // 2
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        # Element is not present in the array
        return "Not Found"

# taken from https://www.geeksforgeeks.org/python-program-for-bubble-sort/
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
                # Swap the found minimum element with
        # the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# taken from: https://www.geeksforgeeks.org/python-program-for-insertion-sort/
def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key



# MAIN--------------------------------------------------------------------
if __name__ == '__main__':
    size = 15
    myList = [0] * size

    # populate a list with random nums 1-9
    i = 0
    for i in range(len(myList)):
        myList[i] = randrange(1,10)

# call linear search method
    #print(" 2 found at index: ", linear_search(myList, 2)) # search list from begining till it finds a 2
    """
    Linear Search:
        How it works: In a sorted list, the function begins from the first element and searches each sequential
        index till the desired value is found or the end of the list is reached. Then it returns the index where 
        the value was found or a message stating the value was not in the list.
        When to use it:  Because this method is based on a sequential search from beginning index to ending index, 
        the list is not required to be sorted before this method is implemented.   
        When it cannot be used: The biggest limitation of this method is that it will take longer than the binary search and this time will be noticeable with large lists
    """

# sort method
    myList.sort()   
    # print(myList)

 # call binary search method
    # #print(" 3 found at index: ", binary_search(myList, 0, len(myList)-1 , 3)) # search list from begining till it finds a 2
    """
    Binary Search:
        How it works: In a sorted list, the function finds the middle index by dividing the length of the list
        in 2 and then going to that index. It then splits the list into two lists including the values on either side of
        the middle element. Since the list is already sorted, if the number we are looking for is larger than the
        middle element, the number we are looking for has to be in the list to the right or if the number we are
        looking for is smaller than the middle element, the number we are looking for has to be in the list to the left. Or the
        value being searched for could of course not be present. This essentially cuts the amount of time to traverse a list in half since it
        cut the length of the list in half. 
        When to use it: This becomes most advantageous when the list size is very long.
        When it cannot be used: The list much first be sorted in order to use this method of searching
    """
# bubble sort
# with 10,000
    # populate with random nums 1-9
    # size = 10000
    # myList = [0] * size
    #
    # i = 0
    # for i in range(len(myList)):
    #     myList[i] = randrange(1, 10)
    #
    # #print(myList)
    # startTime = datetime.now()
    # bubble_sort(myList)
    # endTime = datetime.now()
    # #print(myList)
    #
    # lapsedTime = endTime - startTime
    # print("seconds: ", lapsedTime.seconds)

# with 100,000 ( or way less because my computer is super slow and old...)
    # populate with random nums 1-9
    # size = 16000
    # myList = [0] * size
    #
    # i = 0
    # for i in range(len(myList)):
    #     myList[i] = randrange(1, 10)
    #
    # # print(myList)
    # startTime = datetime.now()
    # bubble_sort(myList)
    # endTime = datetime.now()
    # # print(myList)
    #
    # lapsedTime = endTime - startTime
    #
    # print("seconds: ", lapsedTime.seconds)


# selection sort
# with 10,000
    # populate with random nums 1-9
    # size = 10000
    # myList = [0] * size
    #
    # i = 0
    # for i in range(len(myList)):
    #     myList[i] = randrange(1, 10)
    #
    # #print(myList)
    # startTime = datetime.now()
    # selection_sort(myList)
    # endTime = datetime.now()
    # #print(myList)
    #
    # lapsedTime = endTime - startTime
    # print("seconds: ", lapsedTime.seconds)

# with 100,000 ( or way less because my computer is super slow and old...)
    # populate with random nums 1-9
    # size = 16000
    # myList = [0] * size
    #
    # i = 0
    # for i in range(len(myList)):
    #     myList[i] = randrange(1, 10)
    #
    # # print(myList)
    # startTime = datetime.now()
    # selection_sort(myList)
    # endTime = datetime.now()
    # # print(myList)
    #
    # lapsedTime = endTime - startTime
    #
    # print("seconds: ", lapsedTime.seconds)

# insertion sort
# with 10,000
# populate with random nums 1-9
    size = 10000
    myList = [0] * size

    i = 0
    for i in range(len(myList)):
        myList[i] = randrange(1, 10)

    #print(myList)
    startTime = datetime.now()
    insertion_sort(myList)
    endTime = datetime.now()
    #print(myList)

    lapsedTime = endTime - startTime
    # print("seconds: ", lapsedTime.seconds)

# with 100,000 ( or way less because my computer is super slow and old...)
    #populate with random nums 1-9
    size = 16000
    myList = [0] * size

    i = 0
    for i in range(len(myList)):
        myList[i] = randrange(1, 10)

    # print(myList)
    startTime = datetime.now()
    insertion_sort(myList)
    endTime = datetime.now()
    # print(myList)

    lapsedTime = endTime - startTime

    print("seconds: ", lapsedTime.seconds)

















