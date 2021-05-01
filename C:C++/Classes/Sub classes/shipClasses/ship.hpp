
/***************************************************
Title:  Ship
Author: Brogan Avery
Created: 7/8/20
Description : Class Ship
OS: macOS Catalina
* Copyright : This is my own original work  based on specifications issued by the course instructor
***************************************************/

#ifndef ship_hpp
#define ship_hpp
#include <stdio.h>

#include <iostream>
#include <string>
using namespace std;
//base class
class Ship {
    protected:
        string name;
        string yearBuilt;
    public:
        Ship();
        Ship(string, string);
        void setName(string);
        void setYearBuilt(string);
        string getName() const;
        string getYearBuilt() const;
        virtual void print(){
            cout << name << ": " << yearBuilt <<  endl;
        }
};


//constructors
Ship::Ship(){
}

Ship::Ship(string name, string yearBuilt){
    setName(name);
    setYearBuilt(yearBuilt);
}

//setters
void Ship::setName(string name) {
    this->name = name;
}

void Ship::setYearBuilt(string yearBuilt){
    this->yearBuilt = yearBuilt;
}

//getters
string Ship::getName() const {
    return name;
}

string Ship::getYearBuilt() const {
    return yearBuilt;
}


#endif /* ship_hpp */
