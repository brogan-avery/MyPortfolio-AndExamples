/*
***************************************************
Title: Students
Author: Brogan Avery
Created: 7/3/20
Description : tester for Student class
OS: macOS Catalina
* Copyright : This is my own original work  based on specifications issued by the course instructor
***************************************************
*/

#include "Student.hpp"
#include <string>
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    const int NUM_OF_STUDENTS = 5;
    string name = " ";
    double gpa = 0;
    Student studentList[NUM_OF_STUDENTS];
    
    for(int i = 0; i < NUM_OF_STUDENTS; i++){
        cout << " Enter name of student " << i +1 << ": " << endl;
        cin >> name;
        studentList[i].setName(name);
        
        cout << " Enter gpa of student " << i+1 << ": "<< endl;
        cin >> gpa;
        studentList[i].setGpa(gpa);
    }
    
    for(int i = 0; i < NUM_OF_STUDENTS; i++){
        studentList[i].display();
        cout << "\n" <<endl;
    }
    
    return 0;
}
