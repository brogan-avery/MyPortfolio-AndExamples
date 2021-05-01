/*
***************************************************************
* Class Name: Desktop
* Author: Brogan Avery
* Created: 2021-02-12
***************************************************************
*/

#ifndef Desktop_h
#define Desktop_h
#include <stdio.h>
#include <string>
#include "PowerSupply.hpp"
#include "Computer.hpp"
using namespace std;

// class declaration
class Desktop{
    private: // objects have a data type of another class
        PowerSupply powerSupply;
        Computer computer;
        double price;
    public:
        Desktop(); // default constructor
        Desktop(PowerSupply, Computer, double);
        void setPowerSupply(PowerSupply);
        void setComputer(Computer);
        void setPrice(double);
        PowerSupply getPowerSupply();
        Computer getComputer();
        double getPrice();
        string getTotal();
        string toString();
};

// ==== constructors ====
     //default
Desktop::Desktop(){
    setPowerSupply(PowerSupply());
    setComputer(Computer());
    setPrice(0);
}

Desktop::Desktop(PowerSupply powerSupply, Computer computer, double price){
    setPowerSupply(powerSupply);
    setComputer(computer);
    setPrice(price);
}
// ==== setters ====
void Desktop::setPowerSupply(PowerSupply powerSupply){
    this->powerSupply = powerSupply;
}

void Desktop::setComputer(Computer computer){
    this->computer = computer;
}

void Desktop::setPrice(double price){
    this->price = price;
}

// ==== getters ====
PowerSupply Desktop:: getPowerSupply(){
    return powerSupply;
}

Computer Desktop:: getComputer(){
    return computer;
}

double Desktop:: getPrice(){
    return price;
}

// added for testing
string Desktop:: getTotal(){
    double total = getPrice() + getPowerSupply().getPrice() + getComputer().getPrice() + getComputer().getCpu().getPrice() + getComputer().getMemory().getPrice() + getComputer().getStorage().getPrice();
    
    string totalStr = to_string(total);
    
    totalStr.resize(7);
    return totalStr;
}

string Desktop:: toString(){
    string price = to_string(getPrice());
    price.resize(6);
    
    string str =  "Power Supply: " + getPowerSupply().toString() + " | Computer: " + getComputer().toString() + " | Price: " + price;
    
    return str;
}


#endif /* Desktop_h */
