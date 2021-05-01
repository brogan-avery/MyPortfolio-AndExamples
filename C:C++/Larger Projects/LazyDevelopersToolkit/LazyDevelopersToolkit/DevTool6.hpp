/**************************************************************
* File Title: Dev Tool 6 Class Header
* Author: Brogan Avery
* Created : 2021-04-01
***************************************************************/

#ifndef DevTool6_hpp
#define DevTool6_hpp

#include <stdio.h>
#include <string>
#include <iostream>
#include <vector>
#include <iomanip>
#include<cstdlib>
#include "DevTool0.hpp"
//#include <fstream>

using namespace std;

class DevTool6:virtual public DevTool0{
    public:
        DevTool6(); ///constructor
        void menu6();
        void displayDictionary();
        void displayWebLinks();
        void openDocumentation();
       
};

#endif /* DevTool6_hpp */
