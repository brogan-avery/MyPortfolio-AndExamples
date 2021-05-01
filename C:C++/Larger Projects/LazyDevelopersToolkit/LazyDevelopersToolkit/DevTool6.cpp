/**************************************************************
* File Title: Dev Tool 6 Class Body
* Author: Brogan Avery
* Created : 2021-04-01
* File Description : this class lets the user open or view the contents of various resources such as files for documentation, help, etc.
***************************************************************/

#include "DevTool6.hpp"

DevTool6::DevTool6(){} ///constructor

/// simple main menu navigation function
void DevTool6::menu6(){
    string userInput = " ";
    cout << "\n* Other Resources * " << endl;
    
    while (userInput != "4") {
        cout << "  Select number " << endl;
        cout << "     1. View My Dictionary" << endl;
        cout << "     2. View My Useful Web Links" << endl;
        cout << "     3. View Product Documentation" << endl;
        cout << "     4. Return To Developer Tools Dashboard" << endl;

        cout << "  Enter Selection: " << endl;
        
        getline(cin, userInput);

        if (userInput == "1"){
            displayDictionary();
        }

        if (userInput == "2"){
            displayWebLinks();
        }
        
        if (userInput == "3"){
            openDocumentation();
        }
    }
    cout << "Going back to Dashboard..." << endl;
}

/// function that displays all terms and definitions in the Dev Tool Custom Dictionary
void DevTool6::displayDictionary(){
    cout << "All Dictionary Terms\n" << endl;
    vector<string> lines = readFile("Dictionary.txt");
    
    /// formats lines of file for output
    for (int i = 0, j = 1; i< lines.size(); i+=2, j+=2){
        cout << lines[i] << ":" << endl;
        cout << "    " << lines[j] << endl;
        cout << "----------------\n"<< endl;
    }
    
}

/// function that websites in the Dev Tool Saved Web Links
void DevTool6::displayWebLinks(){
    cout << "All Web Links\n" << endl;
    vector<string> lines = readFile("WebLinks.csv");
    
    /// formats lines of file for output
    for (auto line : lines){
        for (int i = 0; i < line.length(); i++){
            if (line[i] == ','){
                line.replace(i,1,": \n   ");
            }
        }
        
        cout << line << endl;
        cout << "----------------\n"<< endl;
    }
}

/// a function that opens a file that has more detailed information for the user on how to use this product or specific parts of it
void DevTool6::openDocumentation(){
    system ("open /Users/brogan/Library/Developer/Xcode/DerivedData/LazyDevelopersToolkit-eizgswzshjlxxvebouikjvtdbczc/Build/Products/Debug/LazyDeveloperUserManual.docx");
}



   
