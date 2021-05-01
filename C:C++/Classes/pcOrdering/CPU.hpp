/*
***************************************************************
* Class Name: CPU
* Author: Brogan Avery
* Created: 2021-02-12
***************************************************************
*/

#ifndef CPU_h
#define CPU_h
#include <stdio.h>
#include <string>
#include <vector>
using namespace std;

// class declaration
class CPU{
    private:
        string name;
        int clockSpeed; //GHz
        int numOfCores;
        double price;
    public:
        CPU(); // default constructor
        CPU(string, int, int, double);
        void setName(string);
        void setClockSpeed(int);
        void setNumOfCores(int);
        void setPrice(double);
        string getName();
        int getClockSpeed();
        int getNumOfCores();
        double getPrice();
        string toString();
};

// ==== constructors ====
    // default
CPU::CPU(){
    setName(" " );
    setClockSpeed(0);
    setNumOfCores(0);
    setPrice(0);
}

CPU::CPU(string name, int clockSpeed, int numOfCores, double price){
    setName(name);
    setClockSpeed(clockSpeed);
    setNumOfCores(numOfCores);
    setPrice(price);
}

// ==== setters ====
void CPU::setName(string name){
    this->name = name;
}

void CPU::setClockSpeed(int clockSpeed){
    this->clockSpeed = clockSpeed;
}

void CPU::setNumOfCores(int numOfCores){
    this->numOfCores = numOfCores;
}

void CPU::setPrice(double price){
    this->price = price;
}


// ==== getters ====

string CPU:: getName(){
    return name;
}

int CPU:: getClockSpeed(){
    return clockSpeed;
}

int CPU:: getNumOfCores(){
    return numOfCores;
}

double CPU:: getPrice(){
    return price;
}

string CPU:: toString(){
    string price = to_string(getPrice());
    price.resize(6);
    string str = "Name: " + getName() + " | ClockSpeed: " + to_string(getClockSpeed()) + " GHz | Cores: " + to_string(getNumOfCores()) + " | Price: $" + price;
    
    return str;
}

#endif /* CPU_h */
