/*
***************************************************************
* Class Name: Battery
* Author: Brogan Avery
* Created: 2021-02-12
***************************************************************
*/

#ifndef Battery_h
#define Battery_h
#include <stdio.h>
#include <string>
#include <vector>
using namespace std;

// class declaration
class Battery{
    private:
        int amps;
        double price;
    public:
        Battery(); // default constructor
        Battery(int, double);
        void setAmps(int);
        void setPrice(double);
        int getAmps();
        double getPrice();
        string toString();
};

// ==== constructors ====
    // default
Battery::Battery(){
    setAmps(0);
    setPrice(0);
}

Battery::Battery(int amps, double price){
    setAmps(amps);
    setPrice(price);
}

// ==== setters ====
void Battery::setAmps(int amps){
    this->amps = amps;
}

void Battery::setPrice(double price){
    this->price = price;
}

// ==== getters ====
int Battery:: getAmps(){
    return amps;
}

double Battery:: getPrice(){
    return price;
}

string Battery:: toString(){
    string price = to_string(getPrice());
    price.resize(6);
    
    string str = " Amps: " + to_string(getAmps()) +  " | Price: $" + price;
    
    return str;
}


#endif /* Battery_h */
