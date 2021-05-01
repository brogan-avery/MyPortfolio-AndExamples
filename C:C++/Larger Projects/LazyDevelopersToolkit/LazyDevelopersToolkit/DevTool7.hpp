/**************************************************************
* File Title: Dev Tool 7 Class Header
* Author: Brogan Avery
* Created : 2021-04-01
* File Description : An object that inherits from all of the tools
***************************************************************/
#ifndef DevTool7_hpp
#define DevTool7_hpp

#include <stdio.h>
#include <string>
#include <iostream>
#include <vector>
#include <iomanip>
#include<cstdlib>
#include "DevTool1.hpp"
#include "DevTool2.hpp"
#include "DevTool3.hpp"
#include "DevTool4.hpp"
#include "DevTool5.hpp"
#include "DevTool6.hpp"
using namespace std;

/// this acts as a single tool that inherits from the other tools so the user can stick with one Tool Object
class DevTool7 : public DevTool1, public DevTool2, public DevTool3, public DevTool4, public DevTool5, public DevTool6{
    public:
        DevTool7(); ///constructor
};


#endif /* DevTool7_hpp */
