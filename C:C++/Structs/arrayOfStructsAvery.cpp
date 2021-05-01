
/***************************************************
Title: Bill Calculations
Author: Brogan Avery
Created: 6/24/20
Description : lets user enter in bills for 4 months and then calculates the averages
OS: macOS Catalina
* Copyright : This is my own original work  based on specifications issued by the course instructor
***************************************************/

#include <string>
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    
    const int MONTHS = 4;
    double totalSpentIn4Month = 0;
    double avg = 0;
    
    // 4 months worth of each type of bill
    double rentTotals = 0;
    double gasTotals = 0;
    double waterTotals = 0;
    double garbageTotals = 0;
    string allDonations[MONTHS]; //since its a string and they are not going to be added together and need to be displayed on their own
   
    // the average spent on each bill per month
    double rentAvg = 0;
    double gasAvg = 0;
    double waterAvg = 0;
    double garbageAvg = 0;
    
    struct monthlyExpenses{
        int rent;
        double gas;
        double water;
        double garbage;
        string donation;
        double total; //per month
    };
    
    // array to hold struct objects
    monthlyExpenses expenses[MONTHS];
    
    cout << "To estimate your monthly expenses for the year, you will need to enter in the amount you spent on these items for each of the past four months: rent, gas, water, garbage, and if you donated anything. /n" << endl;
    
    for(int i = 0, j = 1; i < MONTHS ; i++, j++){
        cout << "Enter the total amounts spent for each item for month " << j << endl;
        cout << "How much was spent on rent in month " << j << "?" << endl;
        cin >> expenses[i].rent;
        rentTotals = rentTotals + expenses[i].rent;
            
        cout << "How much was spent on gas in month " << j << "?" << endl;
        cin >> expenses[i].gas;
        gasTotals = gasTotals + expenses[i].gas;
        
        cout << "How much was spent on water in month " << j << "?" << endl;
        cin >> expenses[i].water;
        waterTotals = waterTotals + expenses[i].water;
        
        cout << "How much was spent on garbage in month " << j << "?" << endl;
        cin >> expenses[i].garbage;
        garbageTotals = garbageTotals + expenses[i].garbage;
        
        cout << "If anything was given to donation this month enter that. " << endl;
        cin >> expenses[i].donation;
        allDonations[i] = expenses[i].donation;
        
        //get monthly totals
        expenses[i].total = expenses[i].rent + expenses[i].gas + expenses[i].water + expenses[i].garbage;
        
        cout << "Your total bills for month " << j << " were: $" << fixed << setprecision(2) << expenses[i].total << endl;
        
        // get total of monthly totals
        totalSpentIn4Month = totalSpentIn4Month + expenses[i].total;
    }
    
    // get each average
    avg = totalSpentIn4Month/ MONTHS;
    rentAvg = rentTotals / MONTHS;
    gasAvg = gasTotals / MONTHS;
    waterAvg = waterTotals / MONTHS;
    garbageAvg = garbageTotals / MONTHS;
    
    cout << "-----------------" << endl;
    cout << "On living expenses over the past four month you spent a total of : $" << totalSpentIn4Month;
     cout << "\n" << endl;
    
    cout << "The average you spent on living expenses each month was: $" << avg << endl;
    cout << "\n" << endl;
    
    cout << "Based on the average you spent each month for each bill you will need to set aside this amount to cover each of the following living expenses every month: " << endl;
    cout << "Rent: $" << rentAvg << endl;
    cout << "Gas: $" << gasAvg << endl;
    cout << "Water: $" << waterAvg << endl;
    cout << "Garbage: $" << garbageAvg << endl;
    
    cout <<"Here is what you gave to donation each month: " << endl;
    cout << "-----------------" << endl;
    
    for(int i = 0, j = 1; i < MONTHS; i++, j++){
        cout << "Month " << j << ": ($)" << allDonations[i] << endl;
    }
    
    return 0;
}
