/***************************************************
Title: Tax Bracket Enum
Author: Brogan Avery
Created: 6/29/20
Description : program lets users select a tax group and calculate what they owe in income tax based on what they entered.
OS: macOS Catalina
* Copyright : This is my own original work  based on specifications issued by the course instructor
***************************************************/

#include <string>
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
   
    // var of data type enum to hold tax bracket groups
    enum statusGroup{SINGLE, MARIED_FILING_TOGETHER, MARIED_FILLING_SEPERATE, HEAD_OF_HOUSEHOLD, WIDOWER_WITH_DEPENDANT_CHILD};
    
    // array size
    const int NUM_OF_OPTIONS = 5;
    
    // array to hold the percent associated with each status in the enum of tax statuses
    double percentOwed[NUM_OF_OPTIONS] = {35, 20, 33, 25, 15};
    
    // string representation
    string status[NUM_OF_OPTIONS] = {"Single",  "Married filing together", "Married filing separated", "Head of Household", "Widower with Dependent Child"};
    
    int chosenGroup = 0;
    double income = 0;
    double amountOwed = 0;
    
    cout << "The following options are the tax bracket groups for 2019 income tax. Enter the number of the group which best describes you. \n" << endl;
    
    // prints out what percent each group would owe
    for(int i = SINGLE, j = SINGLE +1; i <= WIDOWER_WITH_DEPENDANT_CHILD; i++, j++ ){
        cout << "Tax group " << j << ") is described as: " << status[i] << " and owes " << percentOwed[i] << "% of their income in taxes. \n" << endl;
    }
    
    // get user input for the group they identify as a part of
    cout << "Enter the group number to which you belong (1-5): " << endl;
    
    cin >> chosenGroup;
    
    // bad input handling
    while(chosenGroup < 1 || chosenGroup > 5){
        cout <<  "Enter a valid number." << endl;
        cin >> chosenGroup;
    }
    
    // get user input for their past year's income total
    cout << "Enter your total income for the 2019 year: " << endl;
    
    cin >> income;
    
    // calculates and prints the amount the user will owe
    amountOwed = (percentOwed[chosenGroup-1] * 0.01) * income;
    
    cout << "Your reported income from the 2019 year: $" << fixed << setprecision(2)<< income << endl;
    
    // output the string value associated with the enum option that they selected minus 1 since the groups ranged from 1-5 and not 0-4 for usability
     cout << "Your reported tax group from the 2019 year: " << status[chosenGroup-1] << endl;
    
    cout << "Based on what you reported you owe " << fixed << setprecision(0) << percentOwed[chosenGroup-1] << "%" << " of your income" << endl;
    
    cout << "Based on what you reported you owe $" << fixed << setprecision(2) << amountOwed << endl;
    
    return 0;
}
