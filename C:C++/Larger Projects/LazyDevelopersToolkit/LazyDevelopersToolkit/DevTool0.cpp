/**************************************************************
* File Title: Dev Tool  0 Class Body
* Author: Brogan Avery
* Created : 2021-04-01
* File Description : This is meant to act as a base class for short cut functions for common actions preformed in C++ such as file IO, etc
***************************************************************/

#include "DevTool0.hpp"

DevTool0::DevTool0(){} ///constructor

// =============== A - C ===============
///add a work to the Dev Tool Dictionary
void DevTool0::addDefinition(string term, string definition){
    appendLineToEOF("Dictionary.txt", term + "\n" + definition);
}

/// add a website link to a file with other links to useful resources like tutorials, gitHub links, etc
void DevTool0::addWebLink(string title, string link){
    appendLineToEOF("WebLinks.csv", title + "," + link);
}

/// makes a quick and cleaner looking way to add a line to the end of an existing file
void DevTool0::appendLineToEOF(string fileName, string text){
    /// takes lines from existing file, stores them in a vector, then re writes file with the new line
    vector<string> lines = readFile(fileName);
    ofstream fileWriter(fileName);
    for (string i : lines){
        fileWriter << i << "\n";
    }
    fileWriter << text;
    
    fileWriter.close();
}

/// simple function to capitalize a word
string DevTool0::capitalizeWord(string text) {
    for (int x = 0; x < text.length(); x++)
    {
        if (x == 0)
        {
            text[x] = toupper(text[x]);
        }
        else if (text[x - 1] == ' ')
        {
            text[x] = toupper(text[x]);
        }
    }
    return text;
}

/// simple function to create a new file
ofstream DevTool0::createFile(string fileName){
    ofstream fileWriter(fileName);
    fileWriter.close();
    return fileWriter;
}

/// function that  creates a new (basic or generic) class header file to save time typing
void DevTool0::createClassHeaderFile(string fileName){
    string className = " ";
    string varName = " ";
    string dataType = " ";
    string defaultConstructor = " ";
    string nonDefaultConstructor = " ";
    string otherMethod = " ";
    vector<string> vars;
    vector<string> nonDefaultConstructors;
    vector<string> setters;
    vector<string> getters;
    vector<string> otherMethods;
    string toStringMethod  = " ";
    ofstream writeFile(fileName); /// Create and open new file
    
/// ---  get inputs ---
    cout << "Class Name: " << endl; /// get user input for class name
    cin >> className;
    
    while (varName != "q") { /// get user input for variable names
        cout << "Variable Name (q to quit): " << endl;
        cin >> varName;
        if (varName == "q"){
            break;
        }
        cout << "Variable's Data Type: " << endl; /// get user input for variable's data type
        cin >> dataType;

        vars.push_back(dataType); ///adds  the new variable and its data type to a vars vector
        vars.push_back(varName);
   }
 
 /// ---  create the class declaration to write to file ---
    defaultConstructor = className + "()"; /// creates a default constructor
    
    nonDefaultConstructor = className + "("; /// creates a non-default constructor
    for (int i = 0; i < vars.size(); i+=2){
        nonDefaultConstructor = nonDefaultConstructor + vars[i];
        if (i != vars.size()-2){
            nonDefaultConstructor = nonDefaultConstructor + ", ";
        }
    }
    nonDefaultConstructor = nonDefaultConstructor + ")";
    
    writeFile << "/*************************************************************** \n Class Name: " << className << endl;
    writeFile << "* Author: Brogan Avery " << endl;
    writeFile << "* Created: 2021-00-00" << endl;
    writeFile << "* File Description:" << endl;
    writeFile << "***************************************************************/ \n" << endl;
    writeFile << "#ifndef " << className << "_hpp" << endl;
    writeFile << "#define" << className << "_hpp\n" << endl;
    writeFile << "#include <stdio.h> \n#include <string> \n#include <iostream> \n#include <vector> \n#include <iomanip> \n#include <fstream> \n#include<unistd.h> /// for unix sleep \nusing namespace std;\n" << endl;
    
    writeFile << "/// class declaration " << endl; /// writes a comment
    writeFile << "class " << className << "{" << endl; /// writes the class name
    
    writeFile << "   private: " << endl; /// writes the private vars
    for (int i = 0, j = 1; i < vars.size(); i+=2, j+=2){
        writeFile << "       " << vars[i]  << " " << vars[j]<<  ";" << endl;
    }
    
    writeFile << "   public: " << endl; /// writes the public methods
    
    writeFile << "       " << defaultConstructor << "; /// default constructor" << endl; /// writes the default constructor and a comment
    
    writeFile << "       " << nonDefaultConstructor << ";" << endl; /// writes the non-default constructor
    
    for (int i = 1; i < vars.size(); i+=2){ /// writes the setters
        writeFile << "       void set" << capitalizeWord(vars[i])  <<  "(" << vars[i - 1] << ");" << endl;
    }
    
    for (int i = 0; i < vars.size(); i+=2){ /// writes the default getters
        writeFile << "       " << vars[i] << " get" << capitalizeWord(vars[i + 1])  <<  "();" << endl;
    }
    
    writeFile << "       string toString();" << endl; /// writes the to string method
    writeFile << "}; \n" << endl;
    
 /// --- write the class body to file ---
    writeFile << "// == constructors ==" << endl; /// writes the default constructor
    writeFile << className << "::" << className << "(){ // default" << endl;
    for (int i = 1; i < vars.size(); i+=2){
        writeFile << "   set" << capitalizeWord(vars[i])  <<  "(";
        if (vars[i-1] == "string"){
            writeFile << "\" \"";
        }
        else{
            writeFile << "0";
        }
        writeFile << ");" << endl;
    }
    writeFile << "} \n" << endl;
    
    writeFile << className << "::" << className <<   "("; /// writes the non-default constructor
    for (int i = 1; i < vars.size(); i+=2){
        writeFile << vars[i-1] << " " << vars[i];
        if (i != vars.size()  -1){
            writeFile << ", ";
        }
    }
    writeFile << "){" << endl;
    for (int i = 1; i < vars.size(); i+=2){
        writeFile << "   set" << capitalizeWord(vars[i])  <<  "(" << vars[i] << ");" << endl;
    }
    writeFile << "} \n" << endl;
    
    writeFile << "// == setters ==" << endl; /// write setters
    for (int i = 1; i < vars.size(); i+=2){
        writeFile << "void " << className  << "::" << "set" << capitalizeWord(vars[i])  <<  "(" << vars[i-1] << " " << vars[i] << "){" << endl;
        writeFile << "   this->" << vars[i] << " = " << vars[i] << ";" << endl;
        writeFile << "} \n" << endl;
    }
    
    writeFile << "// == getters ==" << endl; ///write getters
    for (int i = 1; i < vars.size(); i+=2){
        writeFile << vars[i-1] << " "<< className  << "::" << "get" << capitalizeWord(vars[i])  <<  "(){" << endl;
        writeFile << "   return " << vars[i] << ";" << endl;
        writeFile << "} \n" << endl;
    }
    
    writeFile << "string " << className << "::toString(){" << endl; /// write to string method
    writeFile << "return \"outString\";" << endl;
    writeFile << "} \n" << endl;
    
    writeFile << "#endif /* " << className << "_hpp */" << endl;
    
    writeFile.close(); /// Close the file
    cout << "Creating File..." << endl;
    sleep(1);
    
    /// this just shows the contents of the file that was created for quick copy and paste if wanted instead
    cout << "Here is the content of the file you just created: " << endl;
    sleep(1);
    vector<string> lines = readFile(fileName);
    for (auto line : lines){
        cout << line << endl;
    }
}

// =============== D - F ===============

// =============== G - I ===============
/// function that gets the number of lines in a file
int DevTool0::getFileLineCount(string fileName){
    string line = " "; ///each line's text
    int lineCount = 0; /// number of lines of text in file
    ifstream fileReader(fileName, ios::in); ///open file to READ from
    
    while(getline(fileReader,line)){/// gets the number of lines of text in the file
        lineCount++;
    }
        fileReader.close(); ///close file
    return lineCount;
}

// =============== J - L ===============
/// function used to look up the definitions of terms that have been added to the Dev Tool Dictionary
void DevTool0::lookUp(string term){
    vector<string> lines = readFile("Dictionary.txt"); /// gathers terms in one line and defs in the next into an a vector
    string msg = "Term Not Found";
    
    /// searches for a matching term to the param val, if found returns the definition as the msg value
    for (int i = 0, j = 1; i< lines.size(); i+=2, j+=2){
        if ( term ==  lines[i]){
            msg = lines[j];
        }
    }
    cout << msg <<endl; ///if not found returns "not found" msg
}

// =============== M - O ===============

// =============== P - R ===============
///function that reads lines in from a file
vector<string> DevTool0::readFile(string fileName){
    string line = " "; ///each line's text
    ifstream fileReader(fileName, ios::in); ///open file to READ from
    
    int lineCount = getFileLineCount(fileName); ///gets line count from other function
    
    vector<string> lines;
    
    for( int i = 0; i < lineCount; i++){ /// stores each line's text to lines vector
        getline(fileReader, line);
        lines.push_back(line);
    }
    return lines; /// returns lines in a vector
}

// =============== S - U ===============

///function that uses the system command function to turn the parameter value into speech
void DevTool0::textToSpeech(string text){
    /// stores param text to a file
    createFile("tempTextToSpeech.txt");
    appendLineToEOF("tempTextToSpeech.txt", text);
    string toClString = "say " + text;
    /// calls command to read out loud what is written on that text file (this would need to be changed to fit someone else's system)
    system("say -f /Users/brogan/Library/Developer/Xcode/DerivedData/LazyDevelopersToolkit-eizgswzshjlxxvebouikjvtdbczc/Build/Products/Debug/tempTextToSpeech.txt");
}
// =============== V - Z ===============
