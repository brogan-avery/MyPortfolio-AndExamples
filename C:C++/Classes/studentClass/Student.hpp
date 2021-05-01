/*
***************************************************
Title: Student class
Author: Brogan Avery
Created: 7/3/20
Description : a class to hold student info
OS: macOS Catalina
* Copyright : This is my own original work  based on specifications issued by the course instructor
***************************************************
*/

#ifndef Student_hpp
#define Student_hpp
#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;

class Student {
    private:
        int id;
        static int nextId; //counter-esque attribute
        string name;
        double gpa;
    public:
        Student();
        void setId(int);
        void setName(string);
        void setGpa(double);
        int getId() const;
        string getName() const;
        double getGpa() const;
        void display();
};

// initialize counter
int Student::nextId = 9;

//constructors
Student::Student(){
    nextId++;
    id = nextId;
    setName("");
    setGpa(0);
}

//setters
void Student::setId(int id) {
    this->id = id;
}

void Student::setName(string name) {
    this->name = name;
}

void Student::setGpa(double gpa) {
    this->gpa = gpa;
}

//getters
int Student::getId() const {
    return id;
}

string Student::getName() const {
    return name;
}

double Student::getGpa() const {
    return gpa;
}

//methods

void Student::display() {
    cout << name << endl;
    cout << "--------" << endl;
    cout << "Student ID: " << id << endl;
    cout << "GPA: " << gpa << endl;
    
}

#endif /* Student_hpp */
