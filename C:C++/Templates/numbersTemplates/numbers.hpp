/***************************************************
Title: Number class
Author: Brogan Avery
Created: 7/17/20
Description : class file for numbers min and max template assignment
OS: macOS Catalina
* Copyright : This is my own original work  based on specifications issued by the course instructor
***************************************************/

#ifndef numbers_h
#define numbers_h

class Number{
private:
    int someNumber;
public:
    Number(int);
    void setSomeNumber(int);
    int getSomeNumber() const;
};


//constructor
Number::Number(int n){
    setSomeNumber(n);
}

//setter
void Number::setSomeNumber(int someNumber){
    this->someNumber = someNumber;
}

//getter
int Number::getSomeNumber() const{
    return someNumber;
}


#endif /* numbers_h */
