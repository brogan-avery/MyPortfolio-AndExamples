/***************************************************
Title: Student Info Entry
Author: Brogan Avery
Created: 6/29/20
Description : This program demonstrates a function that uses a pointer to a structure variable as a parameter.
OS: macOS Catalina
* Copyright : This is my own original work  based on specifications issued by the course instructor
***************************************************/

#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

// Struct declaration
struct Student{
    string name;          // Student's name
    int idNum;            // Student ID number
    int creditHours;      // Credit hours enrolled
    double gpa;           // Current GPA
    string major;
    int SATscore;
};

// prototypes
void getData(Student *);
void displayInfo(Student *);

int main(){
    
    Student freshman; // struct object

    // Get the student data.
    cout << "Enter the following student data:\n";
    getData(&freshman);    // Pass by reference the address of freshman.
    
    cout << "\nHere is the student data you entered:\n";
    displayInfo(&freshman); // Pass by reference the address of freshman.

    return 0;
}

// gets all of the info to go into struct object
void getData(Student *s){
    // Get the student name.
    cout << "Student name: ";
    getline(cin, s->name);

    // Get the student ID number.
    cout << "Student ID Number: ";
    cin >> s->idNum;

    // Get the credit hours enrolled.
    cout << "Credit Hours Enrolled: ";
    cin >> s->creditHours;

    // Get the GPA.
    cout << "Current GPA: ";
    cin >> s->gpa;
    
    // Get the major.
    cout << "Student's major:";
    cin >> s->major;
    
    // Get the SAT score.
    cout << "Student's SAT score:";
    cin >> s->SATscore;
}

// displays the data stored in the struct object
void displayInfo(Student *s){
    cout << setprecision(3);
    cout << "Name: " << s->name << endl;
    cout << "ID Number: " << s->idNum << endl;
    cout << "Credit Hours: " << s->creditHours << endl;
    cout << "GPA: " << s->gpa << endl;
    cout << "Major: " << s->major << endl;
    cout << "SAT score: " << s->SATscore << endl;
}
