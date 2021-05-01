//
//  functionsAndArraysAvery.cpp
//  program that includes functions that allow for seaching in an array
//
//  Created by Brogan Avery on 6/17/20.
//  bmavery@dmacc.edu

#include <string>
#include <iostream>
#include <iomanip>
using namespace std;

//prototypes
//send and empty array to a function and populates it
void getNumbers(int [], int);
// finds the max value in an array and returns it (assuming it is taking in the already populated array)
int findMax(int [], int);
// finds the max value in an array and returns it (assuming it is taking in the already populated array)
int findMin(int [], int);
// finds the index of a given value
int find(int [], int, int);


int main() {
    const int SIZE = 5;
    int myArray[SIZE];
    int max = 0;
    int min = 0;
    int lookingFor = 0; // a value that we are searching the array for
    int search = 0; //var name assigned to the find function
    string foundMessage = "The first number you were look for was: "; // a message that tells what the found numbers index is or says that it was not found
    string foundMessage2 = "The second number you were look for was: "; // a message that tells what the found numbers index is or says that it was not found ( the second time the function is called)
    
    getNumbers(myArray,SIZE);
    max = findMax(myArray, SIZE);
    min = findMin(myArray, SIZE);
    
    cout << "----------" << endl;
    
    //  for the purpose of testing both outcomes (found in the array or not), enter 1 number that is in the array and 1 that is not in the following 2 prompts, it does not matter which you do first
    cout << "Enter a number to see if it is in the array" << endl;
    cin >> lookingFor;
    
    search = find(myArray,SIZE,lookingFor);
    
    foundMessage = foundMessage + to_string(lookingFor);
    
    if(search == -1 ){
       foundMessage = foundMessage + ". This number was not found" ;
    }
    else{
       foundMessage = foundMessage + ". This number was found at index " + to_string(search);
    }
    
    cout << "Enter another number to see if it is in the array" << endl;
    cin >> lookingFor;
    
    search = find(myArray,SIZE,lookingFor);
    
    foundMessage2 = foundMessage2 + to_string(lookingFor);
    
    if(search == -1 ){
       foundMessage2 = foundMessage2 + ". This number was not found" ;
    }
    else{
       foundMessage2 = foundMessage2 + ". This number was found at index " + to_string(search);
    }
    
    
    for(int i = 0; i < SIZE; i++){
        cout << " The value in index " << i << " is: " <<  myArray[i] << endl;
    }
    
    cout << "The max value in the array is: " << max <<endl;
    cout << "The min value in the array is: " << min <<endl;
    cout << foundMessage << endl;
    cout << foundMessage2 << endl;

    return 0;
} //end main

// this is void, because even though it seems like changing the values of the array within this function should not change them in the main function, it does.
void getNumbers(int myArray[], int SIZE){
    cout << "Enter 5 numbers to store them in an array" << endl;
    for(int i = 0; i < SIZE; i++){
        cout << "Enter value for index " << i << ": " << endl;
        cin >> myArray[i];
    }
} //end function

int findMax(int myArray[], int SIZE){
    int max = myArray[0];
    
    for(int i = 0; i < SIZE; i++){
        if (max < myArray[i]){
            max = myArray[i];
        }
    }
    
    return max;
} //end function

int findMin(int myArray[], int SIZE){
    int min = myArray[0];
    
    for(int i = 0; i < SIZE; i++){
        if (min > myArray[i]){
            min = myArray[i];
        }
    }
    
    return min;
} //end function

int find(int myArray[], int SIZE, int lookingFor){
    int foundAt = -1;
    for(int i = 0; i < SIZE; i++){
        if (lookingFor == myArray[i]){
            foundAt = i;
        }
    }
    
    return foundAt;
} // end function
