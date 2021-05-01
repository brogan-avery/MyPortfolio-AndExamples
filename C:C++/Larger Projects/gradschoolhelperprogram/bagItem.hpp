//
//  bagItem.hpp
//  class that creates objects to go into the luggage and gets attributes of those items to calculate space and weight
//
//  Created by Brogan Avery on 7/9/20.
//  bmavery@dmacc.edu


#include <string>
#ifndef bagItem_hpp
#define bagItem_hpp
using namespace std;

class Item{
    private:
        string name;
        string size;
        double weight;
    public:
        Item();
        Item(string, string, double);
        void setName(string);
        void setSize(string);
        void setWeight(double);
        string getName();
        string getSize();
        double getWeight();
};

//constructors
Item::Item(){
    setName(" ");
    setSize(" ");
    setWeight(0);
}

Item::Item(string name, string size, double weight ){
    setName(name);
    setSize(size);
    setWeight(weight);
}

void Item::setName(string name){
    this->name = name;
}

void Item::setSize(string size){
    this->size = size;
}

void Item::setWeight(double weight){
    this->weight = weight;
}

string Item::getName(){
    return name;
}

string Item::getSize(){
    return size;
}

double Item::getWeight(){
    return weight;
}


#endif /* bagItem_hpp */
