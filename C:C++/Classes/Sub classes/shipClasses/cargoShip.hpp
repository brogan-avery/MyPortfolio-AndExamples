/***************************************************
Title: Cargo Ship
Author: Brogan Avery
Created: 7/8/20
Description : sub class of Ship
OS: macOS Catalina
* Copyright : This is my own original work  based on specifications issued by the course instructor
***************************************************/

#ifndef cargoShip_hpp
#define cargoShip_hpp
#include <stdio.h>
#include <string>

//sub class of Ship class
class CargoShip : public Ship{
    private:
        int maxCap;
    public:
        CargoShip();
        CargoShip(string, string, int);
        ~CargoShip();
        void setMaxCap(int);
        int getMaxCap() const;
    virtual void print(){
        cout << name << ", Max Capacity (weight): " << maxCap <<  endl;
    }
};

//constructors
CargoShip::CargoShip():Ship(){
    
 }

CargoShip::CargoShip(string name, string year, int maxCap) : Ship(name, year) {
    setMaxCap(maxCap);
}

CargoShip::~CargoShip(){
    
}

//setters
void CargoShip::setMaxCap(int maxCap){
    this->maxCap = maxCap;
}

//getters
int CargoShip::getMaxCap() const{
    return maxCap;
}

#endif /* cargoShip_hpp */
