/**************************************************************
* Title: New and Delete Question 3
* Author: Brogan Avery
* Created : 2021-03-22
* Email: bmavery@dmacc.edu
* Course: CIS 164- Advanced C++
* OS: macOS Catalina
* IDE: Xcode
* Description : An app that



* Copyright : This is my own original work  based on specifications issued by the course instructor
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
***************************************************************/


#include <string>
#include <iostream>
#include <iomanip>
using namespace std;

int main() {

    const int SIZE1 = 100;
    const int SIZE2 = 50;

    int *newArray1; /// pointer for new array 1
    int *newArray2; /// pointer for new array 2

    // Allocate memory for array 1
    newArray1 = new int[SIZE1]; /// makes new array of size

    // print before delete newArray1
    for (int i = 0; i < SIZE1; i++) {
        cout << newArray1[i] << " ";
    }

    delete[] newArray1; /// removes the array from memory space

    cout << " " << endl;
    // print after delete newArray1
    for (int i = 0; i < SIZE1; i++) {
        cout << newArray1[i] << " ";
    }

    // Allocate memory for array 2
    newArray2 = new int[SIZE2]; /// makes new array of size

    for (int i = 0; i < SIZE2; i++) {
        newArray2[i] = 7;
    }

    cout << " " << endl;
    // print newArray2
    for (int i = 0; i < SIZE2; i++) {
        cout << newArray2[i] << " ";
    }

    cout << " " << endl;
    // print newArray1 after it is deleted and newArray2 is initialized
    for (int i = 0; i < SIZE1; i++) {
        cout << newArray1[i] << " ";
    }

    return 0;
}

/**
 Output:

 0 0 268718604 1610612736 -1844706980 32767 0 0 4546352 1 0 0 2 0 3 0 0 0 0 0 6 0 0 0 0 0 0 0 4 0 0 0 0 0 268719507 -268435456 2 536870912 0 20054019 -1844690120 32767 0 0 4546608 1 4546640 1 2 2 4 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 4547008 1 1 1 4 0 0 0 0 1 0 0 0 0 29 0 0 131072 4546672 1 4546816 1 0 0 0 0 0 0 0 0
 0 0 268718604 1610612736 -1844706980 32767 0 0 4546352 1 0 0 2 0 3 0 0 0 0 0 6 0 0 0 0 0 0 0 4 0 0 0 0 0 268719507 -268435456 2 536870912 0 20054019 -1844690120 32767 0 0 4546608 1 4546640 1 2 2 4 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 4547008 1 1 1 4 0 0 0 0 1 0 0 0 0 29 0 0 131072 4546672 1 4546816 1 0 0 0 0 0 0 0 0
 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
 0 0 268718604 1610612736 -1844706980 32767 0 0 4546352 1 0 0 2 0 3 0 0 0 0 0 6 0 0 0 0 0 0 0 4 0 0 0 0 0 268719507 -268435456 2 536870912 0 20054019 -1844690120 32767 0 0 4546608 1 4546640 1 2 2 4 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 4547008 1 1 1 4 0 0 0 0 1 0 0 0 0 29 0 0 131072 4546672 1 4546816 1 0 0 0 0 0 0 0 0

 No matter where the first array is printed, its output will be random memory location vs actual values since it has never been initialized in this program. The second array however will print normally will all 7s ass expected.
 */


