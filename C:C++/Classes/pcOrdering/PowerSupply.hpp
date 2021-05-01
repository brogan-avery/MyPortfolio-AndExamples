/*
***************************************************************
* Class Name: PowerSupply
* Author: Brogan Avery
* Created: 2021-02-12
***************************************************************
*/

#ifndef PowerSupply_h
#define PowerSupply_h
#include <stdio.h>
#include <string>
#include <vector>
using namespace std;

// class declaration
class PowerSupply{
    private:
        int watts;
        double price;
    public:
        PowerSupply(); // default constructor
        PowerSupply(int, double);
        void setWatts(int);
        void setPrice(double);
        int getWatts();
        double getPrice();
        string toString();
};

// ==== constructors ====
    // default
PowerSupply::PowerSupply(){
    setWatts(0);
    setPrice(0);
}

PowerSupply::PowerSupply(int watts, double price){
    setWatts(watts);
    setPrice(price);
}

// ==== setters ====
void PowerSupply::setWatts(int watts){
    this->watts = watts;
}

void PowerSupply::setPrice(double price){
    this->price = price;
}

// ==== getters ====
int PowerSupply:: getWatts(){
    return watts;
}

double PowerSupply:: getPrice(){
    return price;
}

string PowerSupply:: toString(){
    string price = to_string(getPrice());
    price.resize(6);
    
    string str = " Watts: " + to_string(getWatts()) +  " | Price: $" + price;
    
    return str;
}



#endif /* PowerSupply_h */
