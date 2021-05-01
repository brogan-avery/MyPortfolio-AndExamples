/**************************************************************
* File Title: Dev Tool 4 Class Header
* Author: Brogan Avery
* Created : 2021-04-01
***************************************************************/

#ifndef DevTool4_hpp
#define DevTool4_hpp

#include <stdio.h>
#include <string>
#include <iostream>
#include <vector>
#include <iomanip>
#include<cstdlib>
#include "DevTool0.hpp"
//#include <fstream>

using namespace std;

class DevTool4:virtual public DevTool0{
    public:
        DevTool4(); ///constructor
        void menu4();
};

#endif /* DevTool4_hpp */
