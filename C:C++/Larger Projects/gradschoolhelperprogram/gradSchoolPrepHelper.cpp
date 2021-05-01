//
//  gradSchoolPrepHelper.cpp
//  program that contains "sub-programs" to help me prepare for grad school
//
//  Created by Brogan Avery on 6/29/20.
//  bmavery@dmacc.edu

#include <string>
#include <iostream>
#include <iomanip>
#include <unistd.h> // specific to unix based systems, need for sleep() function
#include <fstream>
#include "bagItem.hpp" // class file

using namespace std;

//prototypes and other relevant declarations (broken up by parts)

void mainMenu();

void expenseTracker();
void expenseTrackerDescription();
void addExpense();
void viewExpenses();

void scholarshipTracker();
struct Award{
    string award;
    string link;
    string amount;
    string dueDate;
    string fit;
    int entryNum;
};
void scholarshipTrackerDescription();
void addScholarship();
void viewScholarships();
void editScholarships(Award[] , int, int);

void toDoList();
void toDoListDescription();
void addToDoItem();
void viewToDoList();

void luggageCalculator();
void luggageCalculatorDescription();
void addBagItem();
void viewBagItems();

int commandLine(int);
void instructions();
void screenDiv(); // simulates a top of screen division

int main() {
    bool isOption = false; // can be reused to check if a value is in a list/array (container/collection)
    string response = " "; // response for bool isOption
    
//intro screen
    screenDiv();
    cout << "+*+*+*+*+*+*+*+*+*               *+*+*+*+*+*+*+*+*+*+*+*+*+*" << endl;
    cout << "\n" << endl;
    cout << "******** Welcome to the grad school preparer 400! ******** " << endl;
    cout << "\n" << endl;
    cout << "+*+*+*+*+*+*+*+*+*               *+*+*+*+*+*+*+*+*+*+*+*+*+*" << endl;

    sleep(2);

//option to see instructions for overall program
    screenDiv();
    while(isOption == false){
        cout << "Would you like instructions on how to use this program? " << endl;
        cout << "[y/n]: " << endl;

        cin >> response;

        if(response == "y" || response == "n"){
            isOption = true;
        }
    }

    if(response == "y"){
        instructions();
    }

//call to start of program
    mainMenu();
    
    return 0;
}//===========================

//MAIN MENU SCREEN
void mainMenu(){
// array that displays options and controls the options sent to the command line function
    const int NUM_OF_OPTIONS = 5;
    string selectionOptions[NUM_OF_OPTIONS] {"Expense Tracker", "Scholarship tracker", "To do list","Luggage Calculator", "Sign out" }; // menu options
    
//displays main menu screen with array options
    screenDiv();
    cout << "MAIN MENU" << endl;
    cout << "------------" << endl;
    
    for(int i = 0; i < NUM_OF_OPTIONS; i++){
        cout << i+1 << ") " << selectionOptions[i] << endl;
    }
    cout << "\n" << endl;

// calls command line functions and executes the following if/else statements accordingly
    int selection = commandLine(NUM_OF_OPTIONS);
    
    if(selection == 1){
        expenseTracker();
    }
    else if(selection == 2){
        scholarshipTracker();
    }
    else if(selection == 3){
        toDoList();
    }
    else if(selection == 4){
        luggageCalculator();
    }
    else if(selection == 5){
        cout << "You are now signed out." << endl;
        exit(0); // prevents the return to any functions (this was my mistake for coding it that way) but not the less, it is a fail-safe to make sure the program exits incase I forgot to fix anything else somewhere to properly prevent something weird from happening. basically forces the program to end even if something else were to be called after it
    }
    else{
        mainMenu();
    }
    // nothing will happen here if -999 is returned
    
}//================================================================================

//the main menu screen of each sub program is set up exactly as the main menu screen is and will function the exact same.

void expenseTracker(){
    const int NUM_OF_OPTIONS = 3;
    string selectionOptions[NUM_OF_OPTIONS] {"How to use program", "Add expense", "View expenses"}; // menu options
    
// output
    screenDiv();
    cout << "EXPENSE TRACKER" << endl;
    cout << "------------" << endl;
    
    for(int i = 0; i < NUM_OF_OPTIONS; i++){
        cout << i+1 << ") " << selectionOptions[i] << endl;
    }
    cout << "\n" << endl;

// call to command line and if/else options for its return value
    int selection = commandLine(NUM_OF_OPTIONS);
    
    if(selection == 1){
        expenseTrackerDescription();
    }
    else if(selection == 2){
        addExpense();
        
    }
    else if(selection == 3){
        viewExpenses();
    }
    else{
        mainMenu();
    }
    
}//================================================================================

// function the displays the description of this sub program
void expenseTrackerDescription(){
    const int NUM_OF_OPTIONS = 0; // no options to send to command line (only option is to use -999 to break and return to previous screen)
    
    screenDiv();
    cout << "This program lets you keep a running total of any expenses you plan to encounter in preparation for grad school and during the two years while in school. \n" << endl;
    
    cout << "To add a new expense to your budget, return to the previous screen and select option 2. Follow the program prompts as directed. \n " << endl;
    
    cout << "To view all of the expenses you have already added as well as a running total, return to the previous screen and select option 3." << endl;

// call command line to go back to previous screen
    commandLine(NUM_OF_OPTIONS);

// goes back to previous screen ( expense tracker main menu)
    expenseTracker();
    
}//========================================================================

// function to add a new expense to the list
void addExpense(){
    string expenseName = " "; //name of expense
    double amount = 0; // dollar amount of the expense

// prompts for input of the expense and the amount
    screenDiv();
    cout << "To add a new expense, enter the name of the item and the cost associated with it on the lines below \n" <<endl;
    
    cout << "Expense Name: ";
    cin.ignore();
    getline(cin, expenseName);
    
    cout << "Cost/ Amount: $";
    cin >> amount;
   
    //prevents negative money and only allows for numbers
    while(amount < 0.01){
        if(cin.fail()){
            cin.clear();
            cin.ignore();
        }

        cout << "You must enter a number above 0" << endl;
        sleep(1);
        
        cout << "Cost/ Amount: $";
        cin >> amount;
    }

// stores the new expense and amount to a file
    
    // open or create file to WRITE to
    ofstream expenseWrite("expense.csv",ios_base::app);
    
    // Write to file
    expenseWrite << expenseName << "\n " << amount << "\n";
    
    // Close file
    expenseWrite.close();

// returns to sub program's main menu automatically after completing the entry
    expenseTracker();
} //=============================================================

// function that allow for viewing the expenses and the total amounts
void viewExpenses(){
    string line = " "; // each line's text
    int lineCount = 0; // number of lines of text in file
    int halfOfLineCount = 0; // half of the lines in file ( expense and amount)
    double runningTotal = 0; // total amounts
    const int NUM_OF_OPTIONS = 0; // no options to send to command line (only option is to use -999 to break and return to previous screen)
 
// step 1 of reading from file
    
    //open file to READ from
    ifstream expenseRead("expense.csv" , ios::in);
    
    // gets the number of lines of text in the file
    while(getline(expenseRead,line)){
        lineCount++;
    }
    
    //close file
    expenseRead.close();
    
// step 2 of reading from file
    
    halfOfLineCount = lineCount / 2;
    string expenseAndAmount[lineCount]; // basically will tokenize all the lines of text in file.
    string expenseName[halfOfLineCount]; // will split the expense name tokens off from the array with all lines of text and stores to this array
    double amount[halfOfLineCount]; // will split the amount tokens off from the array with all lines of text and stores to this array
    
    //open file to READ from
    ifstream expenseRead2("expense.csv" , ios::in);

    // reads all lines in and stores each line as an element in an array
    for(int i = 0; i < lineCount; i++){
        getline(expenseRead2,line);
        expenseAndAmount[i] = line;
       }
    
    //closes file
    expenseRead2.close();
    
    //splits the expense names and amounts into parallel arrays from the expenseAndAmount array
    for(int i = 0, j = 0, k = 1; i < halfOfLineCount; i++, j+=2 , k+=2){
        expenseName[i] = expenseAndAmount[j];
        amount[i] = stod(expenseAndAmount[k]); // converts from string to double
        runningTotal+= amount[i]; // gets running total of amounts
    }
    
// formatting and outputs to look nice in the display
    screenDiv();
    cout << "  Expense                          Amount ($)" << endl;
    cout << " ---------                        -----------" << endl;
    
    for(int i = 0; i < halfOfLineCount; i++){
        cout << left << setw(35) << expenseName[i] << right << setw(10) << fixed << setprecision(2) << amount[i] << endl;
    }
    cout << "---------------------------------------------" << endl;
    cout << left << setw(35) << "Runnning Total" << right << setw(10) << fixed << setprecision(2) << runningTotal << endl;
    
//calls the command line to go back to previous screen
    commandLine(NUM_OF_OPTIONS);
    
    expenseTracker();
} //=============================================================

// function to display main menu of scholarship tracker, functions the same as all main menus
void scholarshipTracker(){
    const int NUM_OF_OPTIONS = 3;
    string selectionOptions[NUM_OF_OPTIONS] {"How to use program", "Add new scholarship", "View or edit existing scholarships"}; // menu options
 
// output
    screenDiv();
    cout << "SCHOLARSHIP TRACKER" << endl;
    cout << "------------" << endl;
    
    for(int i = 0; i < NUM_OF_OPTIONS; i++){
        cout << i+1 << ") " << selectionOptions[i] << endl;
    }
    cout << "\n" << endl;
 
// call to command line and if/else options for its return value
    int selection = commandLine(NUM_OF_OPTIONS);
    
    if(selection == 1){
        scholarshipTrackerDescription();
    }
    else if(selection == 2){
        addScholarship();
        
    }
    else if(selection == 3){
        viewScholarships();
    }
    else{
        mainMenu();
    }
} //===============================================================

// function to display description for this subprogram
void scholarshipTrackerDescription(){
    const int NUM_OF_OPTIONS = 0; // no options to send to command line (only option is to use -999 to break and return to previous screen)
    
    screenDiv();
    cout << "This program lets you keep a quick list of scholarships that you may want to apply for as well as a link to the application and description of the scholarship. It also allows you to enter an amount of the scholarship and the date the application if due by if you wish. Finally, it gives an option for you to mark if it is a good fit for you or not once you have read the description on the scholarship's website. \n" << endl;
    
    cout << "To add a new scholarship to the list, return to the previous screen and select option 2. Follow the program prompts as directed. \n " << endl;
    
    cout << "To view a list of the scholarships and corresponding information or if you wish to fill out the optional fields (award amount, due date, or fit/ applicableness) , return to the previous screen and select option 3. Follow the program prompts as directed." << endl;
    
// command line to return to previous screen
    commandLine(NUM_OF_OPTIONS);
    
    scholarshipTracker();
    
} //===============================================================

void addScholarship(){
    string award = " "; //scholarship name
    string link = " "; //website
    string dueDate = " - "; //date it is due
    string amount = " - "; // the award amount
    string fit = " - "; // eligibility notes
    bool isOption = false; // can be reused to check if a value is in a list/array (container/collection)
    string response = " "; // for bool isOption

// prompts for inputs
    screenDiv();
    cout << "To add a new scholarship, enter the name of the award and follow the prompts as directed.  \n" <<endl;
    
    cout << "Award: ";
    cin.ignore();
    getline(cin, award);
    
    cout << "Hyper-link/ website: ";
    getline(cin, link);

// prompt to enter optional info or not with input validation
    while(isOption == false){
            cout << "Would you like to enter additional information for this scholarship? ";
            cout << "[y/n]: " << endl;
    
            cin >> response;
    
            if(response == "y" || response == "n"){
                isOption = true;
            }
        }
    
        if(response == "y"){
            cout << "Fill out the following information with values or in any form you would like as this is for your own personal use and can be changed later on." << endl;
            
            cout << "Award Amount: ($)";
            cin.ignore();
            getline(cin, amount);
            
            cout << "Due Date: ";
            getline(cin, dueDate);
            
            cout << "Describe award fit/eligibility: ";
            getline(cin, fit);
        }
    
// storing the entered information to a file
    // open or create file to WRITE to
    ofstream scholarshipWrite("scholarship.csv",ios_base::app);
    
    // Write to file
    scholarshipWrite << award << "\n" << link << "\n" << amount << "\n" << dueDate <<  "\n" << fit << "\n";
    
    // Close file
    scholarshipWrite.close();

// return to the sub program main menu after entry is completed
    scholarshipTracker();
    
} //===============================================================

// function to view and edit the current entries in the scholarship file
// all though my data is not actually stored in a normal table format, it is easier to think of it as if it were a table with 5 columns and then each entry or struct object would be a row
void viewScholarships(){
    string line = " "; // line of text
    int lineCount = 0; // number of all the lines in file
    int fifthOfLineCount = 0; // line count divided by the 5 categories/ cols of data
    int totalEntries = 0; // total of rows or struct objects
    int *ptr = &totalEntries; // pointer that points to totalEntries
    
// step 1 in reading from file
    //open or create file to READ from
    ifstream scholarshipRead("scholarship.csv" , ios::in);
       
    while(getline(scholarshipRead,line)){
        lineCount++; // get the number of lines of text
    }
    
    const int NUM_OF_OPTIONS = lineCount; // used to edit an entry
    
    //array of structs
    Award entry[lineCount];
    
    // close file
    scholarshipRead.close();
       
// step 2 of reading from file
       
    fifthOfLineCount = lineCount / 5; // 5 columns of data
    string allCols[lineCount]; // all lines from file
       
    //open file to READ from
    ifstream scholarshipRead2("scholarship.csv" , ios::in);
    
    // "tokenizes" lines into elements and stores all in this array
    for(int i = 0; i < lineCount; i++){
        getline(scholarshipRead2,line);
        allCols[i] = line;
        }
       
    //close file
    scholarshipRead2.close();
    
    // splits the tokens from the array which contains every line into the appropriate variable of different struct objects (similar concept as used in the viewExpenses function but with struct objects and variable vs parallel arrays.)
    for(int i = 0, j = 0, k = 1, l=2, m = 3, n = 4; i < fifthOfLineCount; i++, j+=5 , k+=5 , l+=5 , m+=5 , n+=5){
        entry[i].award = allCols[j];
        entry[i].link = allCols[k];
        entry[i].amount = allCols[l];
        entry[i].dueDate = allCols[m];
        entry[i].fit = allCols[n];
        entry[i].entryNum = i+1;
        totalEntries++; // total of struct objects or rows in an imaginary table.
    }
     
// formatting and outputs in a nice way
    screenDiv();
    cout << "  Award                               Info " << endl;
    cout << " ---------                         ----------" << endl;
    
    for(int i = 0; i < fifthOfLineCount; i++){
        cout << entry[i].entryNum << ") " << left << setw(35) << entry[i].award << left << setw(35) << "\n        Web link: " << right << setw(10) << entry[i].link << left << setw(35) << "\n        Amount: " << right << setw(10) << entry[i].amount << left << setw(35) << "\n        Due by:  " << right << setw(10) << entry[i].dueDate << left << setw(36) << " \n        Eligibility: " << right << setw(10) << entry[i].fit << endl;
    }
 
// gives option to edit the information of any row of data
    cout << "\n To edit any of the awards, enter the number associated with the award." << endl;
       
    int selection = commandLine(NUM_OF_OPTIONS);
   
    // if the command does not say to return to the previous page, it calls the edit scholarship function
    if(selection != -999){
        editScholarships(entry, selection, *ptr);
    }
    else{
        scholarshipTracker();
    }
    
} //===============================================================

// function to edit existing scholarships (takes in the array of struct objects and the scholarship number that the user wishes to edit and lists the attributes in a numbered list)
void editScholarships(Award entry[], int selectionNumber, int totalEntries){
    int i = selectionNumber - 1; // to start at 0
 
// prompt to see which column in the row he user wishes to edit
    screenDiv();
    cout << " To edit a field for the following scholarship, enter the number associated with it and follow the prompts as directed. \n " << endl;
    cout << entry[i].award << endl;
    cout << "------------------- \n" << endl;
    
    cout << left << setw(35) << "1) web link: " << right << setw(15) << entry[i].link << left << setw(35) << "\n2) Amount: " << right << setw(15) << entry[i].amount << left << setw(35) << "\n3) Due by:  " << right << setw(15) << entry[i].dueDate << left << setw(36) << " \n4) Eligibility: " << right << setw(15) << entry[i].fit << endl;
    
    const int NUM_OF_OPTIONS = 4; // number of struct variables that can be edited ( not the name of the award) so the name of the scholarship is like a primary key that cannot be changed but the other columns of data for the row can be
    
    int selection = commandLine(NUM_OF_OPTIONS);

// unless user wants to return to previous page, program uses a switch statement to edit the variable of the struct object associated with the number the user enters
    if(selection != -999){
        switch(selection){
             case 1 :
                cout << "Curent weblink: " << entry[i].link << endl;
                cout << "Enter new weblink: ";
                cin.ignore();
                getline(cin, entry[i].link);
                break;
             case 2 :
                cout << "Curent amount: " << entry[i].amount << endl;
                cout << "Enter new amount: ";
                cin.ignore();
                getline(cin, entry[i].amount);
                break;
             case 3 :
                cout << "Curent due date: " << entry[i].dueDate << endl;
                cout << "Enter new due date: ";
                cin.ignore();
                getline(cin, entry[i].dueDate);
                break;
             case 4 :
                cout << "Curent eligibility: " << entry[i].fit << endl;
                cout << "Enter new eligibility: ";
                cin.ignore();
                getline(cin, entry[i].fit);
                break;
          }
        // after they edit one column value for the row they are given the option to edit more within that same scholarship/row, it will keep returning to this option to edit the same row until the user selects -999 to leave the editing screen of that scholarship
        editScholarships(entry, selectionNumber, totalEntries);
    }
    
//writes over file to include the new information
    // open file to WRITE to
    ofstream scholarshipWrite("scholarship.csv");
    
    // Write to file
    for(int i = 0; i < totalEntries; i++){
        scholarshipWrite << entry[i].award << "\n " << entry[i].link << "\n" << entry[i].amount << "\n" << entry[i].dueDate <<  "\n" << entry[i].fit << "\n";
    }
    // Close file
    scholarshipWrite.close();
    
    // shows the updated information and current list of all scholarships with the call to the view function
    viewScholarships();
    
} //===============================================================

// function to display the main menu screen of this sub program
void toDoList(){
    const int NUM_OF_OPTIONS = 3;
    string selectionOptions[NUM_OF_OPTIONS] {"How to use program", "Add new to do item", "View or edit existing to do list"}; // menu options
    
// output
    screenDiv();
    cout << "TO DO LIST" << endl;
    cout << "------------" << endl;
    
    for(int i = 0; i < NUM_OF_OPTIONS; i++){
        cout << i+1 << ") " << selectionOptions[i] << endl;
    }
    cout << "\n" << endl;
    
// call to command line and if/else options for its return value
    int selection = commandLine(NUM_OF_OPTIONS);
    
    if(selection == 1){
        toDoListDescription();
    }
    else if(selection == 2){
        addToDoItem();
        
    }
    else if(selection == 3){
        viewToDoList();
    }
    else{
        mainMenu();
    }
    
} //===============================================================

// function that displays the description for this sub program
void toDoListDescription(){
    const int NUM_OF_OPTIONS = 0; // no options to send to command line (only option is to use -999 to break and return to previous screen)
    
    screenDiv();
    cout << "This program is a simple to do list. You can add anything that you want to remember. \n" << endl;
    
    cout << "To add a new item to the list, return to the previous screen and select option 2. Follow the program prompts as directed. \n " << endl;
    
    cout << "To view the list return to the previous screen and select 3." << endl;
    
    commandLine(NUM_OF_OPTIONS);
    
    toDoList();
    
} //===============================================================

// function to add to do list items
void addToDoItem(){
    string item = " "; // name of to do item
 
// prompts for info
    screenDiv();
    cout << "To add a new item, enter it below. \n" <<endl;
    
    cout << "List item: ";
    cin.ignore();
    getline(cin, item);

//Writes item to a file
    // open file to WRITE to
    ofstream toDoListWrite("toDoList.csv",ios_base::app);
    
    // Write to file
    toDoListWrite << item << "\n";
    
    // Close file
    toDoListWrite.close();
    
    toDoList();
    
} //===============================================================

// function to view to do list items
void viewToDoList(){
    string line = " "; // line of text
    int lineCount = 0; // number of lines in file
    const int NUM_OF_OPTIONS = 0; // no options to send to command line (only option is to use -999 to break and return to previous screen)
    
// step 1 of reading
    //open file to READ from
    ifstream toDoListRead("toDoList.csv" , ios::in);
       
    while(getline(toDoListRead,line)){
        lineCount++; //get the number of lines in the file
    }
    
    //close file
    toDoListRead.close();
       
// step 2 of reading from file
       
    string items[lineCount]; // array for lines in file
    
    //open file to READ from
    ifstream toDoListRead2("toDoList.csv" , ios::in);
    
    // stores all lines to an array
    for(int i = 0; i < lineCount; i++){
        getline(toDoListRead2,line);
        items[i] = line;
        }
    
    //close file
    toDoListRead2.close();

// formating and outputs
    screenDiv();
    cout << "  To Do " << endl;
    cout << " --------- " << endl;
    
    for(int i = 0; i < lineCount; i++){
        cout << i + 1 << ") " << items[i] << endl;
    }
    
// call to command line to return to previous screen
    commandLine(NUM_OF_OPTIONS);
    
    expenseTracker();
} //===============================================================

// function that displays the main menu for this sub program
void luggageCalculator(){
    const int NUM_OF_OPTIONS = 3;
    string selectionOptions[NUM_OF_OPTIONS] {"How to use program", "Add new item to bag", "View items in bag"}; //menu options

//output
    screenDiv();
    cout << "LUGGAGE PACKING LIST" << endl;
    cout << "------------" << endl;
    
    for(int i = 0; i < NUM_OF_OPTIONS; i++){
        cout << i+1 << ") " << selectionOptions[i] << endl;
    }
    cout << "\n" << endl;
    
// call to command line and if/else options for its return value
    int selection = commandLine(NUM_OF_OPTIONS);
    
    if(selection == 1){
        luggageCalculatorDescription();
    }
    else if(selection == 2){
        addBagItem();
        
    }
    else if(selection == 3){
        viewBagItems();
    }
    else{
        mainMenu();
    }
    
    
} //==============================================================

//function that shows the description for this sub program
void luggageCalculatorDescription(){
    const int NUM_OF_OPTIONS = 0; // no options to send to command line (only option is to use -999 to break and return to previous screen)
    
    screenDiv();
    cout << "This program helps you plan what to pack by getting a weight for all of the items you enter and comparing it to the maximum weight allowed for a check bag based on the standard weight limit which is 70lbs.  \n" << endl;
    
    cout << "To add a new item to the luggage, return to the previous screen and select option 2. Follow the program prompts as directed. \n " << endl;
    
    cout << "To view the items, return to the previous screen and select 3. Follow the prompts. " << endl;
    
    commandLine(NUM_OF_OPTIONS);
    
    luggageCalculator();
    
} //===============================================================

// function that lets user add an item to their bag and uses its weight to calculate the total weight of the bag
void addBagItem(){
    Item item; // an object from the Item class
    string name = " "; // name of the object
    string size = " "; // some note for the size of the object
    double weight = 0; // weight in kg
    double maxWeight = 32; // standard weight limit for checked bags is usually between 23-32 kg
    double oneGram = 0.001; // kg - g conversion (seems like a reasonable lower limit)

// prompts for input
    screenDiv();
    cout << "You are allowed to pack up to 32 kg worth of items in you checked bag. To enter a new item follow the prompts bellow. " << endl;
    
    cout << "Item: ";
    cin.ignore();
    getline(cin, name);
    
    cout << "What is the approximate size of the item? (you can enter something like small or bulky, or can fit in a breadbox. It is for your reference.): ";
    getline(cin, size);
    
    cout << "bag weight in kilograms (you may enter decimal values): ";
    cin >> weight;
    
    //limits input to a number in the given range
    while(weight < oneGram || weight > maxWeight){
        if(cin.fail()){
            cin.clear();
            cin.ignore();
        }
        
        cout << "You many only enter a number between 0.001 kg (one gram) and the max weight limit of 32 kg.)" << endl;
        cin >> weight;
    }
    
 // uses the input from user to set the objects attributes
    item.setName(name);
    item.setSize(size);
    item.setWeight(weight);
    
//Write to a file
    // open or create file to WRITE to
    ofstream bagItemsWrite("bagItems.csv",ios_base::app);
    
    // Write to file
    bagItemsWrite << item.getName() << "\n" << item.getSize() << "\n" << item.getWeight() << "\n";
    
    // Close file
    bagItemsWrite.close();
    
    // returns to previous screen once the entry is completed
    luggageCalculator();
}//===============================================================

// function that shows user what items are in the bag and how close they are to the weight limit or if they are over the limit
void viewBagItems(){
    string line = " "; // line of text
    int lineCount = 0; // number of lines in file
    int thirdOfLineCount = 0; // for each attribute of an object
    double roomLeft = 32; // max weight limit
    const int NUM_OF_OPTIONS = 0; // no options to send to command line (only option is to use -999 to break and return to previous screen)
    
// step 1 in reading from the file
       
    //open file to READ from
    ifstream bagItemsRead("bagItems.csv" , ios::in);
       
    while(getline(bagItemsRead,line)){
        lineCount++; // number of lines in file
    }
    
    // close the file
    bagItemsRead.close();
       
// step 2 in reading from the file
       
    thirdOfLineCount = lineCount / 3; // 3 columns of data
    string allLines[lineCount]; // every line in the file
    string item[thirdOfLineCount]; // just the lines with the item name
    string size[thirdOfLineCount]; // just the lines with the size of items
    double weight[thirdOfLineCount]; // just the lines with the weights of items
       
    //open file to READ from
    ifstream bagItemsRead2("bagItems.csv" , ios::in);
     
    // makes every line in the file an element of an array
    for(int i = 0; i < lineCount; i++){
        getline(bagItemsRead2,line);
        allLines[i] = line;
    }
    
    //close the file
    bagItemsRead2.close();

// splits the array containing all lines of data into 3 parallel arrays which are like the different column of data
    for(int i = 0, j = 0, k = 1, l = 2; i < thirdOfLineCount; i++, j+=3 , k+=3, l+=3){
        item[i] = allLines[j];
        size[i] = allLines[k];
        weight[i] = stod(allLines[l]); // coverts from string to double
        roomLeft = roomLeft - weight[i];
    }
    
 // formating and outputs
       
    screenDiv();
    cout << "  Item               size             weight(kg)" << endl;
    cout << "---------          ---------         ---------" << endl;
       
    for(int i = 0; i < thirdOfLineCount; i++){
        cout << left << setw(20) << item[i]  << setw(20) << size[i] << right << setw(7) << weight[i] << endl;
    }
    cout << "--------------------------------------------------" << endl;
    
    if(roomLeft >= 0){
        cout << "You are able to fix " <<  setprecision(5) << roomLeft << " kilograms worth of items in you bag until it is at the max weight." << endl;
    }
    else{
       cout << "Your bag is currently " <<  setprecision(5) << -(roomLeft) << " kilograms over the max weight and you will likely encounter extra fees." << endl;
    }
       
    commandLine(NUM_OF_OPTIONS);
       
    luggageCalculator();
    
}//===============================================================

// this function is what gives the user the option to select menu numbers and be taken into different screens based on their selection. It is set up to only accept a user input that is a number. It works by taking in the number of options a user can select on a given menu screen. If the only option a user has is to return to a previous screen, the number of options sent to this function will be 0. This limits the only option that they can select to -999 which triggers a break in the loop and then lets the function that called the command line function continue to the next function call which is a call to the function that displays the screen that they saw privous to the one that they entered.
int commandLine(int NUM_OF_OPTIONS){
    int selection = 0; // the number the user types in
    int returnButton = -999; // the sentinel value that lets the user return to the previous screen

// prompts for input
    cout << "\nSelection or command. To return to the previous menu or screen enter -999" << endl;
    cout << "===> ";
    
    cin >> selection ;

// prevents user from entering a non- number, a number that is not a selection option, and handles if the user enters -999
    while(selection < 1 || selection > NUM_OF_OPTIONS){
        if(cin.fail()){
            cin.clear();
            cin.ignore();
        }
        if(selection == returnButton){
            break;
        }
        cout << "\nThat is an invalide selection option. " << endl;
        
        cout << "\nEnter selection. To return to the previous menu or screen enter -999" << endl;
        cout << "===> ";
        
        cin >> selection ;
    }

// returns the number they selected to direct the function that called the command line which function to call next
    return selection;
} //==============================================================

// this function displays the instructions for the overall program if the user wishes to see them.
void instructions(){
    string continueProgram = " ";
    screenDiv();
    cout <<"New user information" << endl;
    cout << "------------" << endl;
    
    cout << "The goal of this program is to make preparing for grad school in Edinburgh as an American student easier. This program has many features designed to help you plan for expenses, keep track of all of your to-do lists, make a list of scholarships, and plan your packing. " << endl;
    cout << "\n" << endl;
    
    cout << "Instructions for navigating through this program:" << endl;
    cout << "------------" << endl;
    
    cout << "When the program starts you will see the main menu screen. It contains a list of sub-programs or options which you can enter into. You do this by entering in the number associated with the option you want. This will lead you to another screen with options, you select these options the same way. \n" << endl;
    
    cout << "To continue to program press any key and press enter: " << endl;
    
    cin >> continueProgram;
} //==============================================================

// the imaginary boundary of top of a screen
void screenDiv(){
    cout << "\n\n\n+++=========================================================+++\n" << endl;
}



