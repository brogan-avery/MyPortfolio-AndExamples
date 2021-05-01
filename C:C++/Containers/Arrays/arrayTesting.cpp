/***************************************************
Title: Array testing
Author: Brogan Avery
Created: 7/6/20
Description : testing the upper and lower limits of an array with a given allowed range
OS: macOS Catalina
* Copyright : This is my own original work  based on specifications issued by the course instructor
***************************************************/

#include <string>
#include <iostream>
#include <iomanip>
using namespace std;

//prototypes
double testArrayAvg(int [], int);

int main() {
    const int LOWER = 1;
    const int UPPER = 20;
    const int TOO_LOW = 0;
    const int TOO_HIGH = 21;
    int array1[LOWER] = {5};
    int array2[UPPER] = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20};
    int array3[TOO_LOW];
    int array4[TOO_HIGH] = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21};
    int result = 0;
    
// test the lower limit
    result = testArrayAvg(array1, LOWER);
    
    if(result == -1){
        cout << "ERROR: The Average cannot be calculated because the size of the array is not within the valid range. " <<  endl;
    }
    else{
         cout << "The Average number is: " << result <<  endl;
    }
   
// test the upper limit
    result= testArrayAvg(array2, UPPER);
    
    if(result == -1){
        cout << "ERROR: The Average cannot be calculated because the size of the array is not within the valid range. " <<  endl;
    }
    else{
         cout << "The Average number is: " << result <<  endl;
    }
    
// test out of range
    result = testArrayAvg(array3, TOO_LOW);
    
    if(result == -1){
        cout << "ERROR: The Average cannot be calculated because the size of the array is not within the valid range. " <<  endl;
    }
    else{
         cout << "The Average number is: " << result <<  endl;
    }
    
// test out of range
    result = testArrayAvg(array4, TOO_HIGH);
    
    if(result == -1){
        cout << "ERROR: The Average cannot be calculated because the size of the array is not within the valid range. " <<  endl;
    }
    else{
         cout << "The Average number is: " << result <<  endl;
    }

    return 0;
}


// takes in array and size
double testArrayAvg(int thisArray[], const int SIZE){
    double total = 0;
    double avg = 0;
    
    if( SIZE < 1 || SIZE > 20){
        return -1;
    }
    else{
        for(int i = 0; i < SIZE; i++){
            total = total + thisArray[i];
        }
        
        avg = total/SIZE;
        
        return avg;
    }
}



