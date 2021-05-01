/*
***************************************************************
* Class Name: Screen
* Author: Brogan Avery
* Created: 2021-02-12
***************************************************************
*/

#ifndef Screen_h
#define Screen_h
#include <stdio.h>
#include <string>
#include <vector>
using namespace std;

// class declaration
class Screen{
    private:
        int size; // inches
        double price;
    public:
        Screen(); // default constructor
        Screen(int, double); 
        void setSize(int);
        void setPrice(double);
        int getSize();
        double getPrice();
        string toString();
};

// ==== constructors ====
    // default
Screen::Screen(){
    setSize(0);
    setPrice(0);
}

Screen::Screen(int size, double price){
    setSize(size);
    setPrice(price);
}

// ==== setters ====
void Screen::setSize(int size){
    this->size = size;
}

void Screen::setPrice(double price){
    this->price = price;
}

// ==== getters ====
int Screen:: getSize(){
    return size;
}

double Screen:: getPrice(){
    return price;
}

string Screen:: toString(){
    string price = to_string(getPrice());
    price.resize(6);
    
    string str = " Size: " + to_string(getSize()) +  "in. | Price: $" + price;
    
    return str;
}



#endif /* Screen_h */
