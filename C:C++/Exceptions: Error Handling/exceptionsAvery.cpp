
/***************************************************
Title: exceptions
Author: Brogan Avery
Created: 7/12/20
Description : prompts user to enter an even number from 1-100 and uses exception handling to deal with bad input
OS: macOS Catalina
* Copyright : This is my own original work  based on specifications issued by the course instructor
***************************************************/

#include <string>
#include <iostream>
#include <iomanip>
using namespace std;

//prototype
int multiply(int,int);

int main() {
    int num1 = 0;
    int num2 = 0;
    
    cout << "To find the product of two numbers follow the prompts below." << endl;
    
    cout << "Enter an even number between 1 and 100." << endl;
    cin >> num1;
    
    cout << "Enter a second even number between 1 and 100." << endl;
    cin >> num2;
    
    try{
        cout << "The product of " << num1 << " and " << num2 << " is: " << multiply(num1, num2) << endl;
    }
    
    // throw comes from the function
    catch(...){
        cout << "Caught exception from multiply(). One of the numbers you entered were outsize of range or were not even. " << endl;
    }
    
    return 0;
}

int multiply(int num1, int num2){
    
//tries to set the variable or throws an error if one of the conditions are met
    int product = 0;
    
    if (num1 < 1 || num1 >100){
        throw num1;
    }
    
    if (num1 < 2 || num2 >100){
        throw num2;
    }
    
    if (num1 % 2 != 0){
        throw num1;
    }
    
    if (num2 % 2 != 0){
           throw num2;
    }
    // if not throw, it returns the product
    product = num1 * num2;
    return product;
}
