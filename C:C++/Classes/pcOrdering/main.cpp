/**************************************************************
* Title: PC Ordering 
* Author: Brogan Avery
* Created : 2021-02-12
* Email: bmavery@dmacc.edu
* Course: CIS 164- Advanced C++
* OS: macOS Catalina
* IDE: Xcode
* Description : An app that helps a pc store sell custom build pcs by giving the user options for various features . it also includes testing for the classes.
* Copyright : This is my own original work  based on specifications issued by the course instructor
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
***************************************************************/

#include <string>
#include <iostream>
#include <iomanip>
#include <vector>
#include "Desktop.hpp"
#include "Laptop.hpp"
#include "Computer.hpp"
#include "CPU.hpp"
#include "Memory.hpp"
#include "Storage.hpp"
#include "PowerSupply.hpp"
#include "Screen.hpp"
#include "Battery.hpp"
using namespace std;

//prototypes:
string step1();
CPU step2();
Memory step3();
Storage step4();
PowerSupply step5_A();
Battery step5_B();
Screen step6();
void tests(); // added for testing
void runTest(string, string, string); // added for testing


int main() {

// ====== FOR TESTING ======
    // call method to " run tests". I tried to set them up similar to how a unit test would function
    tests();
    
    
    // These are just my templates to refer to:
    //Desktop destopOption1(powerSuppy,computer,price)
    //Laptop laptopOption1(Screen, battery, computer,price)
    //Computer computerOption1(cpu,memory,storage, price)
    //CPU cpuOption1(name, clockSpeed GHz, numofCores, price)
    //Memory memoryOption1(clockSpeed MHz,size GB,price)
    //Storage storageOption1(size TB,price)
    //PowerSupply powerSupplyOption1(watts,price)
    //Screen screenOption1(size,price)
    //Battery batteryOption1(amps,price)
    
    cout << "\n \n \n********************************************" << endl;
// intro/ instructions
    cout << "Here you will choose the options you want in your custom product. You will be presented with a number of steps with two options each. Enter the number of the option you would like. You will be able to view the product you created and the price for it at the end." << endl;
    
    // get users input for each step depending on weather they want a laptop or desk top
    string ui = step1();
    CPU cpu = step2();
    Memory memory = step3();
    Storage storage = step4();
    Computer computer(cpu, memory, storage,10); // craft the computer out of the previous input values for the other objects
    
    double total = cpu.getPrice() + memory.getPrice() + storage.getPrice() + computer.getPrice();
    
    if (ui == "Desktop"){
        PowerSupply powerSupply = step5_A();
        Desktop desktop(powerSupply,computer,50 );// craft the computer out of the previous input values for the other objects
        
        total = total + powerSupply.getPrice() + desktop.getPrice();
        
        cout << "Your final product: " << desktop.toString() << endl;
    }

    else if (ui == "Laptop"){
        Battery battery = step5_B();
        Screen screen = step6();
        Laptop laptop(screen, battery, computer, 80); // craft the computer out of the previous input values for the other objects
        
        total = total + battery.getPrice() + screen.getPrice() + laptop.getPrice();
        
        cout << "Your final product: " << laptop.toString() << endl;
    }
    
    cout << "Your total is: $" << total << endl;

    return 0;
}

string step1(){
    vector<string> options = {"Desktop" , "Laptop"}; // declare vector with options
    int numOptions = 2; // number of options for each part of the computers
    int ui = 0; // user input

// get users input for option
    while (true ){
        cout << "\n Step 1: Choose an option for machine type:" << endl;

        for (int i = 0; i < numOptions; i++){
            cout << "\n Option " << i + 1 << ": " << options[i] << endl;
        }

        cin >> ui;

        if (ui == 1){
            return options[0];
        }

        else if (ui == 2){
                return options[1];
        }

        else{
            cout << "invalid entry" << endl;
        }
    }
}

CPU step2(){
    CPU cpuOption1("AMD..something", 3.5, 6, 400);
    CPU cpuOption2("Intel..something", 2.9, 2, 300);
    vector<CPU> options = {cpuOption1 , cpuOption2}; // declare vector with options
    int numOptions = 2; // number of options for each part of the computers
    int ui = 0; // user input

// get users input for option
    while (true ){
        cout << "\n Step 2: Choose an option for CPU:" << endl;
        for (int i = 0; i < numOptions; i++){
            cout << "\n Option " << i + 1 << ": " << options[i].toString() << endl;
        }

        cin >> ui;

        if (ui == 1){
            return options[0];
        }

        else if (ui == 2){
            return options[1];;
        }

        else{
            cout << "invalid entry" << endl;
        }
    }
}

Memory step3(){
    Memory memoryOption1(2133, 4, 150);
    Memory memoryOption2(2400, 8, 250);
    vector<Memory> options = {memoryOption1 , memoryOption2}; // declare vector with options
    int numOptions = 2; // number of options for each part of the computers
    int ui = 0; // user input

// get users input for option
    while (true ){
        cout << "\n Step 3: Choose an option for Memory:" << endl;
        for (int i = 0; i < numOptions; i++){
            cout << "\n Option " << i + 1 << ": " << options[i].toString() << endl;
        }

        cin >> ui;

        if (ui == 1){
            return options[0];
        }

        else if (ui == 2){
            return options[1];;
        }

        else{
            cout << "invalid entry" << endl;
        }
    }
}

Storage step4(){
    Storage storageOption1(1,300);
    Storage storageOption2(2,500);
    vector<Storage> options = {storageOption1 , storageOption2}; // declare vector with options
    int numOptions = 2; // number of options for each part of the computers
    int ui = 0; // user input

// get users input for option
    while (true ){
        cout << "\n Step 4: Choose an option for Storage:" << endl;
        for (int i = 0; i < numOptions; i++){
            cout << "\n Option " << i + 1 << ": " << options[i].toString() << endl;
        }

        cin >> ui;

        if (ui == 1){
            return options[0];
        }

        else if (ui == 2){
            return options[1];;
        }

        else{
            cout << "invalid entry" << endl;
        }
    }
}

PowerSupply step5_A(){
    PowerSupply powerSupplyOption1(150,40);
    PowerSupply powerSupplyOption2(175,50);
    vector<PowerSupply> options = {powerSupplyOption1 , powerSupplyOption2}; // declare vector with options
    int numOptions = 2; // number of options for each part of the computers
    int ui = 0; // user input

// get users input for option
    while (true ){
        cout << "\n Step 5: Choose an option for Power:" << endl;
        for (int i = 0; i < numOptions; i++){
            cout << "\n Option " << i + 1 << ": " << options[i].toString() << endl;
        }

        cin >> ui;

        if (ui == 1){
            return options[0];
        }

        else if (ui == 2){
            return options[1];;
        }

        else{
            cout << "invalid entry" << endl;
        }
    }
}

Battery step5_B(){
    Battery batteryOption1(2, 30);
    Battery batteryOption2(3, 40);
    vector<Battery> options = {batteryOption1 , batteryOption2}; // declare vector with options
    int numOptions = 2; // number of options for each part of the computers
    int ui = 0; // user input

// get users input for option
    while (true ){
        cout << "\n Step 5: Choose an option for Battery:" << endl;
        for (int i = 0; i < numOptions; i++){
            cout << "\n Option " << i + 1 << ": " << options[i].toString() << endl;
        }

        cin >> ui;

        if (ui == 1){
            return options[0];
        }

        else if (ui == 2){
            return options[1];;
        }

        else{
            cout << "invalid entry" << endl;
        }
    }
}

Screen step6(){
    Screen screenOption1(13,100);
    Screen screenOption2(17,150);
    vector<Screen> options = {screenOption1 , screenOption2}; // declare vector with options
    int numOptions = 2; // number of options for each part of the computers
    int ui = 0; // user input

// get users input for option
    while (true ){
        cout << "\n Step 6: Choose an option for Screen size:" << endl;
        for (int i = 0; i < numOptions; i++){
            cout << "\n Option " << i + 1 << ": " << options[i].toString() << endl;
        }

        cin >> ui;

        if (ui == 1){
            return options[0];
        }

        else if (ui == 2){
            return options[1];;
        }

        else{
            cout << "invalid entry" << endl;
        }
    }
}

void tests(){
    // the out comes may have trailing 0s because in the program that is handled in the print statement in main so when they come from the class directly this is how they have to be tested
    
    // compare actual to expected results for each classes object creation
    Battery battery(5, 5);
    Screen screen(15, 50);
    PowerSupply powerSupply(5, 5);
    Storage storage(128, 50);
    Memory memory(1, 4, 100);
    CPU cpu("intel-i9", 1, 2, 200);
    
    // testing a few different ways to create the objects
    Computer computer(cpu, memory, storage, 300);
    Computer computer2(CPU("Ryzen", 2, 2, 100), Memory(2, 8, 200),Storage(500,300), 500);
    Laptop laptop(screen, battery, computer, 100);
    Laptop laptop2(Screen(17,20), Battery(2,10), computer2, 150);
    Desktop desktop(powerSupply, computer, 50);
    Desktop desktop2(powerSupply, Computer(cpu, Memory(1,2,30), Storage(52, 20), 80), 100);
    
// send an expected known value to test the actual value of the to string print method for each object created
    
    // test battery object
    runTest("Test Battery object creation", " Amps: 5 | Price: $5.0000", battery.toString());
    
    // test screen object
    runTest("Test Screen object creation", " Size: 15in. | Price: $50.000", screen.toString());
    
    // test powerSupply object
    runTest("Test PowerSupply object creation", " Watts: 5 | Price: $5.0000", powerSupply.toString());
    
    // test Storage object
    runTest("Test Storage object creation", " Size: 128TB | Price: $50.000 | ", storage.toString());
    
    // test Memory object
    runTest("Test Memory object creation", "ClockSpeed: 1 MHz | Size: 4GB | Price: $100.00", memory.toString());
    
    // test CPU object
    runTest("Test CPU object creation", "Name: intel-i9 | ClockSpeed: 1 GHz | Cores: 2 | Price: $200.00", cpu.toString());
    
    // test Computer object
    runTest("Test 1st Computer object creation", "CPU: Name: intel-i9 | ClockSpeed: 1 GHz | Cores: 2 | Price: $200.00 | Memory: ClockSpeed: 1 MHz | Size: 4GB | Price: $100.00 | Storage:  Size: 128TB | Price: $50.000 |  | Price: 300.00", computer.toString());
   
    // test Computer object 2
    runTest("Test 2nd Computer object creation", "CPU: Name: Ryzen | ClockSpeed: 2 GHz | Cores: 2 | Price: $100.00 | Memory: ClockSpeed: 2 MHz | Size: 8GB | Price: $200.00 | Storage:  Size: 500TB | Price: $300.00 |  | Price: 500.00", computer2.toString());
    
    // test Laptop object
    runTest("Test 1st Laptop object creation", "Screen:  Size: 15in. | Price: $50.000 | Battery:  Amps: 5 | Price: $5.0000 | Computer: CPU: Name: intel-i9 | ClockSpeed: 1 GHz | Cores: 2 | Price: $200.00 | Memory: ClockSpeed: 1 MHz | Size: 4GB | Price: $100.00 | Storage:  Size: 128TB | Price: $50.000 |  | Price: 300.00 | Price: 100.00", laptop.toString());
    
    // test Laptop object 2
    runTest("Test 2nd Laptop object creation", "Screen:  Size: 17in. | Price: $20.000 | Battery:  Amps: 2 | Price: $10.000 | Computer: CPU: Name: Ryzen | ClockSpeed: 2 GHz | Cores: 2 | Price: $100.00 | Memory: ClockSpeed: 2 MHz | Size: 8GB | Price: $200.00 | Storage:  Size: 500TB | Price: $300.00 |  | Price: 500.00 | Price: 150.00", laptop2.toString());
    
    // test Desktop object
    runTest("Test 1st Desktop object creation", "Power Supply:  Watts: 5 | Price: $5.0000 | Computer: CPU: Name: intel-i9 | ClockSpeed: 1 GHz | Cores: 2 | Price: $200.00 | Memory: ClockSpeed: 1 MHz | Size: 4GB | Price: $100.00 | Storage:  Size: 128TB | Price: $50.000 |  | Price: 300.00 | Price: 50.000", desktop.toString());
    
    // test Desktop object 2
    runTest("Test 2nd Desktop object creation", "Power Supply:  Watts: 5 | Price: $5.0000 | Computer: CPU: Name: intel-i9 | ClockSpeed: 1 GHz | Cores: 2 | Price: $200.00 | Memory: ClockSpeed: 1 MHz | Size: 2GB | Price: $30.000 | Storage:  Size: 52TB | Price: $20.000 |  | Price: 80.000 | Price: 100.00", desktop2.toString());
    
    // test final prices for laptops and desktops
    runTest("Test 1st Laptop object price", "805.000", laptop.getTotal());
    runTest("Test 2nd Laptop object price", "1280.00", laptop2.getTotal());
    runTest("Test 1st Desktop object price", "705.000", desktop.getTotal());
    runTest("Test 2nd Desktop object price", "435.000", desktop2.getTotal());
    
// ====== run tests with expected failures:
    
    // test Laptop object
    runTest("Test 1st Laptop object creation", "Screen:  Size: 0in. | Price: $0 | Battery:  Amps: 0 | Price: 7 | Computer: CPU: Name: none | ClockSpeed: 0 GHz | Cores: 0 | Price: $200.00 | Memory: ClockSpeed: 1 MHz | Size: 0GB | Price: $100.00 | Storage:  Size: 128TB | Price: $50.000 |  | Price: 0 | Price: 100.00", laptop.toString());
    
    // test Laptop object 2
    runTest("Test 2nd Laptop object creation", "Screen:  Size: 17in. | Price: $20.000 | Battery:  Amps: 2 | Price: $10.000 | Computer: CPU: Name: Ryzen | ClockSpeed: 2 GHz | Cores: 2 | Price: $100.00 | Memory: ClockSpeed: 2000000000 MHz | Size: 8GB | Price: $200.00 | Storage:  Size: 500TB | Price: $300.00 |  | Price: 500.00 | Price: 150.00", laptop2.toString());
    
    // test Desktop object
    runTest("Test 1st Desktop object creation", "Power Supply:  Watts: 5000000000000000000 | Price: $5.0000 | Computer: CPU: Name: intel-i9 | ClockSpeed: 1 GHz | Cores: 2 | Price: $200.00 | Memory: ClockSpeed: 1 MHz | Size: 4GB | Price: $100.00 | Storage:  Size: 128TB | Price: $50.000 |  | Price: 300.00 | Price: 50.000", desktop.toString());
    
    // test Desktop object 2
    runTest("Test 2nd Desktop object creation", "Power Supply:  Watts: jakhsdfbjhkq hew fkb | Price: $5.0000 | Computer: CPU: Name: intel-i9 | ClockSpeed: 1 GHz | Cores: 2 | Price: $200.00 | Memory: ClockSpeed: 1 MHz | Size: 2GB | Price: $30.000 | Storage:  Size: 52TB | Price: $20.000 |  | Price: 80.000 | Price: 100.00", desktop2.toString());
    
    // test final prices for laptops and desktops
    runTest("Test 1st Laptop object price", "100.000", laptop.getTotal());
    runTest("Test 2nd Laptop object price", "200.00", laptop2.getTotal());
    runTest("Test 1st Desktop object price", "30", desktop.getTotal());
    runTest("Test 2nd Desktop object price", "400", desktop2.getTotal());
    
    
}

void runTest(string testName, string expected, string actual){
    cout << testName << ":\n------------------------------" << endl;
   // cout << expected << " " << actual << endl;
    if (expected == actual){
        cout << "PASS \n" << endl;
    }
    
    else{
        cout << "FAIL \n" << endl;
    }
    
}
