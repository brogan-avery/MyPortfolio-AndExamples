/*
 ***************************************************
 Title: budgeting app
 Author: Brogan Avery
 Created: 7/1/20
 Description :makes a monthly budget using classes
 OS: macOS Catalina
 * Copyright : This is my own original work  based on specifications issued by the course instructor
 ***************************************************
 */

#include "budgetAvery.hpp"
#include <string>
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    //objects
    Budget jan; //uses default constructor
    Budget feb(500,100,50); // uses non-default constructor
    Budget mar(450,50,20); // uses non-default constructor
    
    cout << "Total bills for January: $" << jan.total() << endl;
    cout << "Total bills for February: $" << feb.total() << endl;
    cout << "Total bills for March: $" << mar.total() << endl;
    
    return 0;
}
