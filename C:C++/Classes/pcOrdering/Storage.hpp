/*
***************************************************************
* Class Name: Storage
* Author: Brogan Avery
* Created: 2021-02-12
***************************************************************
*/

#ifndef Storage_h
#define Storage_h
#include <stdio.h>
#include <string>
#include <vector>
using namespace std;

// class declaration
class Storage{
    private:
        int size; // TB
        double price;
    public:
        Storage(); // default constructor
        Storage(int, double);
        void setSize(int);
        void setPrice(double);
        int getSize();
        double getPrice();
        string toString();
};

// ==== constructors ====
    // default
Storage::Storage(){
    setSize(0);
    setPrice(0);
}

Storage::Storage(int size, double price){
    setSize(size);
    setPrice(price);
}

// ==== setters ====
void Storage::setSize(int size){
    this->size = size;
}

void Storage::setPrice(double price){
    this->price = price;
}

// ==== getters ====
int Storage:: getSize(){
    return size;
}

double Storage:: getPrice(){
    return price;
}

string Storage:: toString(){
    string price = to_string(getPrice());
    price.resize(6);
    
    string str = " Size: " + to_string(getSize()) +  "TB | Price: $" + price + " | ";
    
    return str;
}

#endif /* Storage_h */
