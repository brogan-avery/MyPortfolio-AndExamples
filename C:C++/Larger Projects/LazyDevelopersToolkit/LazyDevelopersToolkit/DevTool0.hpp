/**************************************************************
* File Title: Dev Tool 0 Class Header
* Author: Brogan Avery
* Created : 2021-04-01
***************************************************************/

#ifndef DevTool0_hpp
#define DevTool0_hpp

#include <stdio.h>
#include <map>
#include <string>
#include <iostream>
#include <vector>
#include <iomanip>
#include <fstream>
#include<unistd.h> /// for unix sleep
using namespace std;

class DevTool0{
    public:
        DevTool0(); ///constructor
        ofstream createFile(string);
        void createClassHeaderFile(string);
        string capitalizeWord(string);
        void appendLineToEOF(string, string);
        int getFileLineCount(string);
        vector <string> readFile(string);
        void addDefinition(string, string);
        void lookUp(string);
        void addWebLink(string, string);
        void textToSpeech(string);
};

#endif /* DevTool0_hpp */


