//
//  arrayElementsAverageAvery.cpp
//  prompts user for 5 temps and stores them in an array then prints the average
//
//  Created by Brogan Avery on 6/17/20.
//  Copyright © 2020 Brogan Avery. All rights reserved.
//  bmavery@dmacc.edu

#include <string>
#include <iostream>
#include <iomanip>
#include <array>
using namespace std;

//prototypes
double averageFourTemperatures(double, double,double,double);

int main() {
    const int SIZE = 5;
    array<double, SIZE> temperatures = {};
    double totalTemps = 0;
    double average = 0;
    
   //populates array
    for (int i = 0; i < SIZE; i++){
        cout << "Enter a temperature" <<endl;
        cin >> temperatures[i];
    }
    
    //totals the temps to get the average
    for(auto temp: temperatures){
        totalTemps = totalTemps + temp;
    }
    
    average = totalTemps / SIZE;
    
    cout << "Average: "<< fixed << setprecision(2) << average << "°F" << endl;
    
    return 0;
}



// Tests and result
// temperatures[0] =1.1
// temperatures[1] =2.2
// temperatures[2] =3.3
// temperatures[3] =4.4
// temperatures[4] =5.5
//result of average + formated string = 3.30°F
