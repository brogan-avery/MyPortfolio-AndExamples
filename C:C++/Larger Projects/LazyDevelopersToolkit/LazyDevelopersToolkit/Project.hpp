/**************************************************************
* File Title: Project
* Author: Brogan Avery
* Created : 2021-04-16
***************************************************************/
#ifndef Project_hpp
#define Project_hpp

#include <stdio.h>
#include <string>
#include <iostream>
#include <vector>
#include <iomanip>
#include<cstdlib>
#include "DevTool0.hpp"

using namespace std;

class Project{
    private:
        string title;
        vector<string> customerGoals;
        vector<string> userGoals;
        string proposal;
        string detailedDescription;
        string outline;
        string pseudocode;
        string wireframe;
        vector<string> files;
        vector<string> progressReports;
        vector<string> deadLines;
        vector<string> backLog;
        vector<string> timeLog;
        string userManual;
        string productDocumentation;
    
public:
    Project(); /// default constructor
    Project(string, string, string, vector<string>, vector<string>, string, vector<string>, vector<string>, vector<string>, vector<string>, string, string);
    void setTitle(string);
    void setProposal(string);
    void setDetailedDescription(string);
    void setCustomerGoals(vector<string>);
    void setUserGoals(vector<string>);
    void setPseudocode(string);
    void setProgressReports(vector<string>);
    void setDeadLines(vector<string>);
    void setBackLog(vector<string>);
    void setTimeLog(vector<string>);
    void setUserManual(string);
    void setProductDocumentation(string);
    void setOutline(string);
    void setWireframe(string);
    void setFiles(vector<string>);
    string getOutline();
    string getWireframe();
    vector<string> getFiles();
    string getTitle();
    string getProposal();
    string getDetailedDescription();
    vector<string> getCustomerGoals();
    vector<string> getUserGoals();
    string getPseudocode();
    vector<string> getProgressReports();
    vector<string> getDeadLines();
    vector<string> getBackLog();
    vector<string> getTimeLog();
    string getUserManual();
    string getProductDocumentation();
    string toString();
    void addToCustomerGoals(string);
    void addToUserGoals(string);
    void addToProgressReports(string);
    void addToDeadLines(string);
    void addToBackLog(string);
    void addToTimeLog(string);
    void addToFiles(string);
};
#endif /* Project_hpp */
