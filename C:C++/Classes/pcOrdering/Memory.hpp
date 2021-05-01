/*
***************************************************************
* Class Name: Memory
* Author: Brogan Avery
* Created: 2021-02-12
***************************************************************
*/

#ifndef Memory_h
#define Memory_h
#include <stdio.h>
#include <string>
#include <vector>
using namespace std;

// class declaration
class Memory{
    private:
        int clockSpeed; //MHz
        int size; // GB
        double price;
    public:
        Memory(); // default constructor
        Memory(int, int, double);
        void setClockSpeed(int);
        void setSize(int);
        void setPrice(double);
        int getClockSpeed();
        int getSize();
        double getPrice();
        string toString();
};

// ==== constructors ====
    // default
Memory::Memory(){
    setClockSpeed(0);
    setSize(0);
    setPrice(0);
}

Memory::Memory(int clockSpeed, int size, double price){
    setClockSpeed(clockSpeed);
    setSize(size);
    setPrice(price);
}

// ==== setters ====
void Memory::setClockSpeed(int clockSpeed){
    this->clockSpeed = clockSpeed;
}

void Memory::setSize(int size){
    this->size = size;
}

void Memory::setPrice(double price){
    this->price = price;
}

// ==== getters ====
int Memory:: getClockSpeed(){
    return clockSpeed;
}

int Memory:: getSize(){
    return size;
}

double Memory:: getPrice(){
    return price;
}

string Memory:: toString(){
    string price = to_string(getPrice());
    price.resize(6);
    
    string str = "ClockSpeed: " + to_string(getClockSpeed()) + " MHz | Size: " + to_string(getSize()) +  "GB | Price: $" + price;
    
    return str;
}

#endif /* Memory_h */
