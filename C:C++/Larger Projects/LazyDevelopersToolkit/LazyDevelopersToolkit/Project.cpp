/**************************************************************
* File Title: Project
* Author: Brogan Avery
* Created : 2021-04-16
* File Description : A class that helps a user to stay on top of project management and lets them add to back logs and time logs quickly while in the middle of working on projects.
***************************************************************/

#include "Project.hpp"


vector<string> emptyVector; /// empty and default vector to use as the init val for all the vector variables

Project::Project(){ /// default constructor
    setTitle(" ");
    setCustomerGoals(emptyVector);
    setUserGoals(emptyVector);
    setProposal(" ");
    setDetailedDescription(" ");
    setOutline(" ");
    setPseudocode(" ");
    setWireframe(" ");
    setFiles(emptyVector);
    setProgressReports(emptyVector);
    setDeadLines(emptyVector);
    setBackLog(emptyVector);
    setTimeLog(emptyVector);
    setUserManual(" ");
    setProductDocumentation(" ");
}

// == setters ==
void Project::setTitle(string title){
   this->title = title;
}

void Project::setProposal(string proposal){
   this->proposal = proposal;
}

void Project::setDetailedDescription(string detailedDescription){
   this->detailedDescription = detailedDescription;
}

void Project::setCustomerGoals(vector<string> customerGoals){
   this->customerGoals = customerGoals;
}

void Project::setUserGoals(vector<string> userGoals){
   this->userGoals = userGoals;
}

void Project::setPseudocode(string pseudocode){
   this->pseudocode = pseudocode;
}

void Project::setProgressReports(vector<string> progressReports){
   this->progressReports = progressReports;
}

void Project::setDeadLines(vector<string> deadLines){
   this->deadLines = deadLines;
}

void Project::setBackLog(vector<string> backLog){
   this->backLog = backLog;
}

void Project::setTimeLog(vector<string> timeLog){
   this->timeLog = timeLog;
}

void Project::setUserManual(string userManual){
   this->userManual = userManual;
}

void Project::setProductDocumentation(string productDocumentation){
   this->productDocumentation = productDocumentation;
}

void Project::setOutline(string outline){
   this->outline = outline;
}

void Project::setWireframe(string wireframe){
   this->wireframe = wireframe;
}

void Project::setFiles(vector<string> files){
   this->files = files;
}

// == getters ==
string Project::getTitle(){
   return title;
}

string Project::getProposal(){
   return proposal;
}

string Project::getDetailedDescription(){
   return detailedDescription;
}

vector<string> Project::getCustomerGoals(){
   return customerGoals;
}

vector<string> Project::getUserGoals(){
   return userGoals;
}

string Project::getPseudocode(){
   return pseudocode;
}

vector<string> Project::getProgressReports(){
   return progressReports;
}

vector<string> Project::getDeadLines(){
   return deadLines;
}

vector<string> Project::getBackLog(){
   return backLog;
}

vector<string> Project::getTimeLog(){
   return timeLog;
}

string Project::getUserManual(){
   return userManual;
}

string Project::getProductDocumentation(){
   return productDocumentation;
}

string Project::getOutline(){
   return outline;
}

string Project::getWireframe(){
   return wireframe;
}

vector<string> Project::getFiles(){
   return files;
}


// == helper functions to add lines to and update vectors ==
void Project::addToCustomerGoals(string goal){
    vector<string> updatedVector = getCustomerGoals();
    updatedVector.push_back(goal);
    setCustomerGoals(updatedVector);
}
void Project::addToUserGoals(string goal){
    vector<string> updatedVector = getUserGoals();
    updatedVector.push_back(goal);
    setUserGoals(updatedVector);
}
void Project::addToProgressReports(string report){
    vector<string> updatedVector = getProgressReports();
    updatedVector.push_back(report);
    setProgressReports(updatedVector);
}
void Project::addToDeadLines(string deadLine){
    vector<string> updatedVector = getDeadLines();
    updatedVector.push_back(deadLine);
    setDeadLines(updatedVector);
}
void Project::addToBackLog(string logItem){
    vector<string> updatedVector = getBackLog();
    updatedVector.push_back(logItem);
    setBackLog(updatedVector);
}
void Project::addToTimeLog(string logItem){
    vector<string> updatedVector = getTimeLog();
    updatedVector.push_back(logItem);
    setTimeLog(updatedVector);
}
void Project::addToFiles(string file){
    vector<string> updatedVector = getFiles();
    updatedVector.push_back(file);
    setFiles(updatedVector);
}

