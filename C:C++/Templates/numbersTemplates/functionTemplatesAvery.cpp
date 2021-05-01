
/***************************************************
Title: Templates
Author: Brogan Avery
Created: 7/17/20
Description :  program that uses two template functions (min and max) that take in two arguments and return either the larger or the smaller number respectively
OS: macOS Catalina
* Copyright : This is my own original work  based on specifications issued by the course instructor
***************************************************/

#include <string>
#include <iostream>
#include <iomanip>
#include "numbers.hpp"

using namespace std;

// template for max
template <class T1, class T2>
float max(T1 num1, T2 num2)
{
    if( num1 > num2){
        return num1;
    }
    
    else{
        return num2;
    }
}

// template for min
template <class T1, class T2>
float min(T1 num1, T2 num2)
{
    if( num1 < num2){
        return num1;
    }
    
    else{
        return num2;
    }
}

int main() {
    int number = 1;
    double doub = 1.1;
    float flt = 1.111;
    Number obj(2);
   
    cout << "The larger number is " << max(number, doub) << endl;
    cout << "The larger number is " << max(number, flt) << endl;
    cout << "The larger number is " << max(number, obj.getSomeNumber()) << endl;
    cout << "The larger number is " << max(doub,obj.getSomeNumber())
    << endl;
    cout << "The larger number is " << max(flt, doub) << endl;
    
    cout << "The smaller number is " << min(number, doub) << endl;
    cout << "The smaller number is " << min(number, flt) << endl;
    cout << "The smaller number is " << min(number, obj.getSomeNumber()) << endl;
    cout << "The smaller number is " << min(doub,obj.getSomeNumber())
    << endl;
    cout << "The smaller number is " << min(flt, doub) << endl;
    
    return 0;
}



