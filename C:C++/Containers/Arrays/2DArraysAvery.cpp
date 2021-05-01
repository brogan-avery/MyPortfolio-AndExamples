//
//  2DArraysAvery.cpp
//  gets the amount of food eatten every day in one week by three monkeys and then find the average amount they eat in one day and the max and min for the highest or lowest individual
//
//  Created by Brogan Avery on 6/18/20.
//  bmavery@dmacc.edu

#include <string>
#include <iostream>
#include <iomanip>
using namespace std;

// the "column" must be declared global and in prototypes
// kind like in a database, you add more rows all the time but not typically more columns once it is set up like you want
const int DAYS = 5;

//prototypes
double average(double [][DAYS] , int);
double least(double [][DAYS], int);
double greatest(double [][DAYS], int);

int main() {
    const int MONKEYS = 3;
    double lbsPerDayPerMonkey[MONKEYS][DAYS];
    // following two arrays are added for formatting and user friendliness in console
    string monkeySpecies[MONKEYS] = {"Howler", "Spider", "Capuchin"};
    string daysOfWeek[DAYS] = {"Monday", "Tuesday" , "Wednesday", "Thursday", "Friday"};
    
    // i = number of monkeys to go through outter loop , from 2d array type int
    // j = loop through the array of specific monkeys from string array
    for(int i = 0, j = 0 ; i < MONKEYS; i++, j++){
        cout <<  "Enter how many pounds of food the " << monkeySpecies[j] << " monkey ate every day this week." << endl;
        
        // inner for loop
        // k = looping through num of days from the 2d array type int
        // l = looping through the days of the week from array type string
        for(int k = 0, l = 0 ; k < DAYS; k++, l++){
            cout << "Total food intake for " << daysOfWeek[l] << ": " << endl;
            cin >> lbsPerDayPerMonkey[i][k]; // i = MONKEYS, k = DAYS
            
            // while loop will not let user enter in a negative value
            while(lbsPerDayPerMonkey[i][k] <= -1){
            cout << "Total food intake for " << daysOfWeek[l] << ": " << endl;
            cin >> lbsPerDayPerMonkey[i][k]; // i = MONKEYS, k = DAYS
            }
           
        }
    }
    
    // since cols are already part of the array declaration, only send the rows
    double avg = average(lbsPerDayPerMonkey, MONKEYS);
    double min = least(lbsPerDayPerMonkey, MONKEYS);
    double max = greatest(lbsPerDayPerMonkey, MONKEYS);
    
    cout << "The average amount of food required to feed 3 monkeys for one day: " << fixed << setprecision(2) << avg << " lbs." << endl;
    
    cout << "The least amount of food one of the monkeys ate in one day: " << min << " lbs." << endl;
    
    cout << "The largest amount of food one of the monkeys ate in one day: " << max << " lbs." << endl;
    
    return 0;
} //end main

double average(double lbsPerDayPerMonkey[][DAYS], int MONKEYS){
    double total = 0; // total amount of food consumed in one week by 3 monkeys
    double avg = 0; // the average amount of food it takes to feed 3 monkeys every day
    
    for (int i = 0; i< MONKEYS; i++){
        for (int j = 0; j< DAYS; j++){
            total = total + lbsPerDayPerMonkey[i][j];
        }
    }
    
    avg = total/ DAYS;
    
    return avg;
} //end func

double least(double lbsPerDayPerMonkey[][DAYS], int MONKEYS){
    double min = lbsPerDayPerMonkey[0][0] ;
    
    for (int i = 0; i < MONKEYS; i++){
        for (int j = 0; j < DAYS; j++){
           if (min > lbsPerDayPerMonkey[i][j]){
               min = lbsPerDayPerMonkey[i][j];
           }
        }
    }
    
    return min;
} //end func

double greatest(double lbsPerDayPerMonkey[][DAYS], int MONKEYS){
    double max = lbsPerDayPerMonkey[0][0] ;
    
    for (int i = 0; i < MONKEYS; i++){
        for (int j = 0; j < DAYS; j++){
           if (max < lbsPerDayPerMonkey[i][j]){
               max = lbsPerDayPerMonkey[i][j];
           }
        }
    }
    
    return max;
} //end func
