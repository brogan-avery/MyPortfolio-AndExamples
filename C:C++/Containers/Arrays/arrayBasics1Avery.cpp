//
//  arrayBasics1Avery.cpp
// asks users for doubles and stores them in an array and them displays the first, middle, and last
//
//  Created by Brogan Avery on 6/17/20.
//  bmavery@dmacc.edu

#include <string>
#include <iostream>
#include <iomanip>
#include <array>
using namespace std;

int main() {
    const int SIZE = 9;
    array<double, SIZE> items = {};
    
    //populates array
    for (int i = 0; i < SIZE; i++){
        cout << "Enter a number with a decimal" <<endl;
        cin >> items[i];
    }
    
    cout << "First element: " << items[0] << endl;
    cout << "Fifth element: " << items[4] << endl;
    cout << "last element: " << items[8] << endl;
    return 0;
}
