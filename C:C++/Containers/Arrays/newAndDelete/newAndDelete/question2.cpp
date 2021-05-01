/**************************************************************
* Title: New and Delete Question 2
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

    const int SIZE = 100; /// array size
    int *initVal = new int(0);
    int *newArray = new int[SIZE](); /// array of all 0s


    // print before delete
    for (int i = 0; i < SIZE; i++) {
        cout << newArray[i] << " ";
    }

    cout << " " << endl;
    delete[] newArray; /// removes the array from memory space

    // print after delete
    for (int i = 0; i < SIZE; i++) {
        cout << newArray[i] << " ";
    }

    return 0;
}

/**
 Output:
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 268706460 -1073741824 348 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

The first output will constantly print all 0s as expected.
However, the second line of output sometimes will,but sometimes it will add in some random numbers or be completely different.
This is because the delete[] line means that the pointer is now pointing to a spot where that memory was but now that spot may
be filled with something else which leads to the unpredictable behavior.
 */

