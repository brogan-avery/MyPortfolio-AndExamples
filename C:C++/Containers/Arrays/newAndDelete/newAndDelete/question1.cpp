/**************************************************************
* Title: New and Delete Question 1
* Author: Brogan Avery
* Created : 2021-03-22
* Email: bmavery@dmacc.edu
* Course: CIS 164- Advanced C++
* OS: macOS Catalina
* IDE: Xcode
* Description : tests the creating and deleting a new dynamic array
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
   const int SIZE = 100;
    int *newArray; /// pointer for new array

    newArray = new int[SIZE]; /// makes new array of size 'SIZE'

    for (int i = 0; i < SIZE; i++) { /// populates it with numbs from 1-100
        newArray[i] = i+1;
    }

    for (int i = 0; i < SIZE; i++) { /// prints
        cout << newArray[i] << " ";
    }

    delete[] newArray; /// removes the array from memory space

    return 0;
}

/**
 Output:
 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100

 Yes the program runs as expected and I have not run across any memory leaking issues.
 */

