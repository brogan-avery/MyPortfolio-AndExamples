/**************************************************************
* File Title: Dev Tool 4 Class Body
* Author: Brogan Avery
* Created : 2021-04-01
* File Description : This Dev Tool in still in development 
***************************************************************/

#include "DevTool4.hpp"

DevTool4::DevTool4(){} ///constructor

void DevTool4::menu4(){
    string userInput = " ";
    cout << "\n* Project Testing and Debugging * " << endl;
    
    while (userInput != "3") {
        cout << "  Select number " << endl;
        cout << "     1. coming soon" << endl;
        cout << "     2. coming soon" << endl;
        cout << "     3. Return To Developer Tools Dashboard" << endl;

        cout << "  Enter Selection: " << endl;
        getline(cin, userInput);
    }
    cout << "Going back to Dashboard..." << endl;
}
