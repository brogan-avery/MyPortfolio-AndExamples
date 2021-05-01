/*
 ***************************************************
 Title: budgeting app header / class file
 Author: Brogan Avery
 Created: 7/1/20
 ***************************************************
 */

#ifndef budgetAvery_hpp
#define budgetAvery_hpp
#include <stdio.h>
#include <string>
#include <iostream>
#include <iomanip>
using namespace std;

//declare class/ class template
class Budget{
    private:
        int rent;
        int water;
        int trash;
    public:
        Budget(); //default constructor
        Budget(int,int,int); //non-default
        void setRent(int);
        void setWater(int);
        void setTrash(int);
        int getRent() const;
        int getWater() const;
        int getTrash() const;
        int total() const;
};

//default constructor
Budget:: Budget(){
    this->rent = 0;
    this->water = 0;
    this->trash = 0;
}

//non-default
Budget:: Budget(int rent,int water, int trash){
    this->rent = rent;
    this->water = water;
    this->trash = trash;
}

//setters
void Budget:: setRent(int rent){
    this->rent = rent;
}

void Budget:: setWater(int water){
    this->water = water;
}

void Budget:: setTrash(int trash){
    this->trash = trash;
}

//getters
int Budget:: getRent() const{
    return rent;
}

int Budget:: getWater() const{
    return water;
}

int Budget:: getTrash() const{
    return trash;
}

// other methods

int Budget:: total() const{
    int total = this->rent + this->water + this->trash; //maybe you don't need "this->" but it makes more sense to see it this way
    return total;
}


#endif /* budgetAvery_hpp */
