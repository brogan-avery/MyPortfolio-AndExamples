''''
Author: Brogan Avery
Date: 2020/09/12
Project Title: numPy demo
'''

from numpy import *
#————————————————————————————————————————————————————————————————————————————————————
if __name__ == '__main__':
    arr1 = array([[10,15,20],[2,3,4],[9,14.5,18]])
    arr2 = array([[1,2,5],[8,0,12],[11,3,22]])

    print('Here is arr1: \n', arr1)
    print('\nThe shape of arr1: \n', arr1.shape)
    print('\nA 2x2 slice: \n', arr1[0:2,0:2],'\n') # [startrow:endrow, starcol:endcol]

    even = True
    odd = False
    for row in arr1:
        for item in row:
            if(item % 2 ==0):
                print('The value in index ', item, ' is', even )
            else:
                print('The value in index ', item, ' is', odd)


    print('\nThe sum of arr1 and arr2:\n',add(arr1,arr2) )
    print('\nThe product of arr1 and arr2:\n', multiply(arr1, arr2))

    print('\nThe sum of all elements in arr2:\n', arr2.sum())
    print('\nThe product of all elements in arr2:\n', prod(arr2))
    print('\nThe largest number in arr2:\n', arr2.max())
    print('\nThe smallest number in arr2:\n', arr2.min())