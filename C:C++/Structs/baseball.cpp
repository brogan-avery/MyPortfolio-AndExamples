/***************************************************
Title: baseball player stats Struct
Author: Brogan Avery
Created: 6/23/20
Description : program that displays stats for baseball players
OS: macOS Catalina
* Copyright : This is my own original work  based on specifications issued by the course instructor
***************************************************/

#include <string>
#include <iostream>
#include <iomanip>
using namespace std;

int main() {

// player stat struct
    struct player{
        string name;
        double battingAverage;
        int homeRuns;
        int RBIs;
        int runsScored;
        int stollenBases;
        float currentSalary;
        string currantTeam;
    };

// player struct objects
    player Babe;
    player Jackie;
    player Barry;

// set values for players
    Babe.name = "Babe Ruth";
    Babe.battingAverage = 0.342;
    Babe. homeRuns = 714;
    Babe.RBIs = 2174;
    Babe.runsScored = 100;
    Babe.stollenBases = 123;
    Babe.currentSalary = 500.00;
    Babe.currantTeam = "Red Sox";
    
    Jackie.name = "Jackie Robinson";
    Jackie.battingAverage = 0.311;
    Jackie. homeRuns = 137;
    Jackie.RBIs = 734;
    Jackie.runsScored = 200;
    Jackie.stollenBases = 123;
    Jackie.currentSalary = 600.00;
    Jackie.currantTeam = "Dodgers";
    
    Barry.name = "Barry Bonds";
    Barry.battingAverage = 0.298;
    Barry. homeRuns = 762;
    Barry.RBIs = 1996;
    Barry.runsScored = 300;
    Barry.stollenBases = 514;
    Barry.currentSalary = 700.00;
    Barry.currantTeam = "Giants";
    
// print Player 1 stats
    cout << Babe.name << endl;
    cout << "--------------" << endl;
    cout << "Batting Average: " << fixed << setprecision(3)<< Babe.battingAverage << endl;
    cout << "Home runs: " <<Babe.homeRuns << endl;
    cout << "RBIs: " <<Babe.RBIs << endl;
    cout << "Runs scored: " <<Babe.runsScored << endl;
    cout << "Stollen Bases: " <<Babe.stollenBases<< endl;
    cout << "Current Salary: $" << fixed << setprecision(2) << Babe.currentSalary << endl;
    cout << "Current team: " <<Babe.currantTeam << endl;
    cout << "\n" << endl;
    
// print Player 2 stats
    cout << Jackie.name << endl;
    cout << "--------------" << endl;
    cout << "Batting Average: " << fixed << setprecision(3)<< Jackie.battingAverage << endl;
    cout << "Home runs: " <<Jackie.homeRuns << endl;
    cout << "RBIs: " <<Jackie.RBIs << endl;
    cout << "Runs scored: " <<Jackie.runsScored << endl;
    cout << "Stollen Bases: " <<Jackie.stollenBases<< endl;
    cout << "Current Salary: $" <<  setprecision(2)<<Jackie.currentSalary << endl;
    cout << "Current team: " <<Jackie.currantTeam << endl;
    cout << "\n" << endl;
    
// print Player 3 stats
    cout << Barry.name << endl;
    cout << "--------------" << endl;
    cout << "Batting Average: " << fixed << setprecision(3)<< Barry.battingAverage << endl;
    cout << "Home runs: " <<Barry.homeRuns << endl;
    cout << "RBIs: " <<Barry.RBIs << endl;
    cout << "Runs scored: " <<Barry.runsScored << endl;
    cout << "Stollen Bases: " <<Barry.stollenBases<< endl;
    cout << "Current Salary: $" << fixed << setprecision(2)<<Barry.currentSalary << endl;
    cout << "Current team: " <<Barry.currantTeam << endl;
    
    return 0;
}
