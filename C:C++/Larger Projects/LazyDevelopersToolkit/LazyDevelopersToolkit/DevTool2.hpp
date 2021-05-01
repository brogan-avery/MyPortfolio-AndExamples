/**************************************************************
* File Title: Dev Tool 2 Class Header
* Author: Brogan Avery
* Created : 2021-04-01
***************************************************************/

#ifndef DevTool2_hpp
#define DevTool2_hpp

#include <stdio.h>
#include <string>
#include <iostream>
#include <vector>
#include <iomanip>
#include<cstdlib>
#include "DevTool0.hpp"

using namespace std;

class DevTool2:virtual public DevTool0{
    public:
        DevTool2(); ///constructor
        void menu2();
        void doNotDisturb();
        void redLED();
        void greenLED();
        void terminateArduino();
};

#endif /* DevTool2_hpp */
