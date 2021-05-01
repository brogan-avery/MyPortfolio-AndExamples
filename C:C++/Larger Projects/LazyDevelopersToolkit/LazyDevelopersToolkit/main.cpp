/**************************************************************
* Title: The Lazy Developer Tool
* Author: Brogan Avery
* Created : 2021-03-31
* Email: bmavery@dmacc.edu
* Course: CIS 164- Advanced C++
* OS: macOS Catalina
* IDE: Xcode
* Description : This app lets Developers select from a variety of tools that they can use with other projects, to help manage projects, or to help make their life as a developer easier and more efficient.
* Copyright : This is my own original work  based on specifications issued by the course instructor
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
***************************************************************/
#include "DevTool7.hpp"

int main() {
    string userInput = " ";
    DevTool7 myDevTool; /// inherits from all of the other classes to make it easier to access from one place, especially if user does not want to go through many menu screens]
    
    cout << "* * *  Welcome to The Lazy Developer's Toolkit  * * *\n" << endl;
    sleep(1);
    cout << "If you need help or instructions for this product, navigate to the product documentation by entering 6 to be redirected to the the Product Resources. Then select 3 in that menu screen to view the product documentation and user manual.\n" << endl;
    sleep(1);
    
    /// basic navigation menu to select a tool from the dashboard and go to the main menu screen for that tool
    cout << "Developer Tools Dashboard:" << endl;
    while (userInput != "7") {
        cout << "  Select number associated with a developer tool" << endl;
        cout << "     1. Skills Builder" << endl;
        cout << "     2. Arduino Based Tools" << endl;
        cout << "     3. Project Management" << endl;
        cout << "     4. Automated Project Testing" << endl;
        cout << "     5. Relaxation Management" << endl;
        cout << "     6. View Other Resources" << endl;
        cout << "     7. Exit Program" << endl;

        cout << "  Enter Selection: ";
        
        getline(cin, userInput);

        if (userInput == "1"){
            myDevTool.menu1();
        }

        if (userInput == "2"){
            myDevTool.menu2();
        }

        if (userInput == "3"){
            myDevTool.menu3();
        }

        if (userInput == "4"){
            myDevTool.menu4();
        }

        if (userInput == "5"){
            myDevTool.menu5();
        }

        if (userInput == "6"){
            myDevTool.menu6();
        }
    }
    cout << "goodbye" << endl;

    return 0;
}
