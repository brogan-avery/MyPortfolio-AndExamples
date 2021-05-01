/*
***************************************************************
* Class Cpu: Computer
* Author: Brogan Avery
* Created: 2021-02-12
***************************************************************
*/

#ifndef Computer_h
#define Computer_h
#include <stdio.h>
#include <string>
#include <vector>
#include "CPU.hpp"
#include "Memory.hpp"
#include "Storage.hpp"
using namespace std;

// class declaration
class Computer{
    private: // objects have a data type of another class
        CPU cpu;
        Memory memory;
        Storage storage;
        double price;
    public:
        Computer(); // default constructor
        Computer(CPU, Memory, Storage, double);
        void setCpu(CPU);
        void setMemory(Memory);
        void setStorage(Storage);
        void setPrice(double);
        CPU getCpu();
        Memory getMemory();
        Storage getStorage();
        double getPrice();
        string toString();
};

// ==== constructors ====
    // default
Computer::Computer(){
    setCpu(CPU());
    setMemory(Memory());
    setStorage(Storage());
    setPrice(0);
}

Computer::Computer(CPU cpu, Memory memory, Storage storage, double price){
    setCpu(cpu);
    setMemory(memory);
    setStorage(storage);
    setPrice(price);
}

// ==== setters ====
void Computer::setCpu(CPU cpu){
    this->cpu = cpu;
}

void Computer::setMemory(Memory memory){
    this->memory = memory;
}

void Computer::setStorage(Storage storage){
    this->storage = storage;
}

void Computer::setPrice(double price){
    this->price = price;
}


// ==== getters ====

CPU Computer:: getCpu(){
    return cpu;
}

Memory Computer:: getMemory(){
    return memory;
}

Storage Computer:: getStorage(){
    return storage;
}

double Computer:: getPrice(){
    return price;
}

string Computer:: toString(){
    string price = to_string(getPrice());
    price.resize(6);
    
    string str = "CPU: " + getCpu().toString() + " | Memory: " + getMemory().toString() + " | Storage: " + getStorage().toString() + " | Price: " + price;
    
    return str;
}

#endif /* Computer_h */
