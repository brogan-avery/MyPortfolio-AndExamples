
/***************************************************
Title: Cruise Ship
Author: Brogan Avery
Created: 7/8/20
Description : sub class of Ship
OS: macOS Catalina
* Copyright : This is my own original work  based on specifications issued by the course instructor
***************************************************/

#ifndef cruiseShip_hpp
#define cruiseShip_hpp
#include <stdio.h>
#include <string>

//sub class of Ship class
class CruiseShip : public Ship{
    private:
        int maxCap;
    public:
        CruiseShip();
        CruiseShip(string, string, int);
        ~CruiseShip();
        void setMaxCap(int);
        int getMaxCap() const;
        virtual void print(){
            cout << name << ", Max Capacity (passengers): " << maxCap <<  endl;
        }
};

//constructors
CruiseShip::CruiseShip():Ship(){
    
 }

CruiseShip::CruiseShip(string name, string year, int maxCap) : Ship(name, year) {
    setMaxCap(maxCap);
}

CruiseShip::~CruiseShip(){
    
}

//setters
void CruiseShip::setMaxCap(int maxCap){
    this->maxCap = maxCap;
}

//getters
int CruiseShip::getMaxCap() const{
    return maxCap;
}

#endif /* cruiseShip_hpp */
