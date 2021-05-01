/**************************************************************
* Title: Pass by Reference
* Author: Brogan Avery
* Created : 2021-03-22
* Email: bmavery@dmacc.edu
* Course: CIS 164- Advanced C++
* OS: macOS Catalina
* IDE: Xcode
* Description : An app that passes a number initialized to zero to a function by reference that
 prompts a user to enter a number from 1-100. then proves that the scope of the referenced
 value extends to the main function from which it was called.
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

// Prototypes :
void getNumber(int&);

int main() {
    int number = 0;
    getNumber(number);
    cout << " User entered the number: " << number << endl;
    
    return 0;
}

void getNumber(int &number){
    while (number > 100 || number < 1){
    cout << "Enter a number from 1 - 100" << endl;
        cin >> number;
    }
}
