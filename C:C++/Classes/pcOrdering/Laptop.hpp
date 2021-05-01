/*
***************************************************************
* Class Name: Laptop
* Author: Brogan Avery
* Created: 2021-02-12
***************************************************************
*/

#ifndef Laptop_h
#define Laptop_h
#include <stdio.h>
#include <string>
#include <vector>
#include "Battery.hpp"
#include "Computer.hpp"
#include "Screen.hpp"
using namespace std;

// class declaration
class Laptop{
    private: // objects have a data type of another class
        Screen screen;
        Battery battery;
        Computer computer;
        double price;
    public:
        Laptop(); // default constructor
        Laptop(Screen, Battery, Computer, double);
        void setScreen(Screen);
        void setBattery(Battery);
        void setComputer(Computer);
        void setPrice(double);
        Screen getScreen();
        Battery getBattery();
        Computer getComputer();
        double getPrice();
        string getTotal(); // added for testing
        string toString();
};

// ==== constructors ====
    // default
Laptop::Laptop(){
    setScreen(Screen());
    setBattery(Battery());
    setComputer(Computer());
    setPrice(0);
}

Laptop::Laptop(Screen screen, Battery battery, Computer computer, double price){
    setScreen(screen);
    setBattery(battery);
    setComputer(computer);
    setPrice(price);
}

// ==== setters ====
void Laptop::setScreen(Screen screen){
    this->screen = screen;
}

void Laptop::setBattery(Battery battery){
    this->battery = battery;
}

void Laptop::setComputer(Computer computer){
    this->computer = computer;
}

void Laptop::setPrice(double price){
    this->price = price;
}

// ==== getters ====
Screen Laptop:: getScreen(){
    return screen;
}

Battery Laptop:: getBattery(){
    return battery;
}

Computer Laptop:: getComputer(){
    return computer;
}

double Laptop:: getPrice(){
    return price;
}

// added for testing
string Laptop:: getTotal(){
    double total = getPrice() + getScreen().getPrice() +  getBattery().getPrice() + getComputer().getPrice() + getComputer().getCpu().getPrice() + getComputer().getMemory().getPrice() + getComputer().getStorage().getPrice();
    
    string totalStr = to_string(total);
    
    totalStr.resize(7);
    return totalStr;
}

string Laptop:: toString(){
    string price = to_string(getPrice());
    price.resize(6);
    
    string str = "Screen: " + getScreen().toString() + " | Battery: " + getBattery().toString() + " | Computer: " + getComputer().toString() + " | Price: " + price;
    
    return str;
}


#endif /* Laptop_h */
