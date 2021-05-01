
/***************************************************
Title: Cruise Ship Driver
Author: Brogan Avery
Created: 7/8/20
Description : A driver to test the ship classes and subclasses of it
OS: macOS Catalina
* Copyright : This is my own original work  based on specifications issued by the course instructor
***************************************************/

#include "ship.hpp"
#include "cruiseShip.hpp"
#include "cargoShip.hpp"
#include <string>
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    const int SIZE = 3;
    Ship *fleet[SIZE] = {
        new Ship("Santa Maria", "1492"),
        new CruiseShip("Nina","1492", 50),
        new CargoShip("Pinta", "1492", 101 )
    };
    
    for(int i = 0; i < SIZE; i++){
        fleet[i]->print();
    }
    return 0;
}
