/**************************************************************
* File Title: Dev Tool 1 Class Header
* Author: Brogan Avery
* Created :  2021-04-01
***************************************************************/

#ifndef DevTool1_hpp
#define DevTool1_hpp

#include <stdio.h>
#include <string>
#include <iostream>
#include <vector>
#include <iomanip>
#include<cstdlib>
#include "DevTool0.hpp"

using namespace std;

class DevTool1:virtual public DevTool0{
    public:
        DevTool1(); ///constructor
        void menu1();
        void displayProblems();
        void openUrl(string);
};

#endif /* DevTool1_hpp */
