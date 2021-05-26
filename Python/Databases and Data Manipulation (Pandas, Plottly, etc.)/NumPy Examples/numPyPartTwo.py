''''
Author: Brogan Avery
Date: 2020/09/14
Project Title: numPy demo part 2
'''

from numpy import *
#————————————————————————————————————————————————————————————————————————————————————
if __name__ == '__main__':
    myArr = array([[1,2,5],[8,0,-7], [7,3,9]])

    print('Here is the array: \n', myArr)

    print('transpose inverts the rows and columns of the array : \n', transpose(myArr))

    print('swapping axes does the same as transpose when working with a 2d array, it inverts the row with the column : \n', swapaxes(myArr,0,1))

   # print('reversing the order of all of the values for the entire array: \n', flip(myArr))

    myArr = fliplr(myArr)
    print('reversing the order of all of the values for each row: \n', myArr)

    myArr = append(myArr,[[3,4,5]], axis=0)

    print('Array with row added: \n', myArr)

    myArr = append(myArr, [[7], [8], [9], [0]], axis=1)

    print('Array with column added: \n', myArr)

    myArr = delete(myArr,3,1)
    print('After deleting the last column: \n', myArr)

    myArr = myArr.reshape(6,2)
    print('The resized array:\n',myArr)

    splitArray = split(myArr,3)
    print('splitting the array into 3 2x2 arrays - (the middle array): \n', splitArray[1] )

    print('the third array in the split array flattened: \n', splitArray[2].flatten())
