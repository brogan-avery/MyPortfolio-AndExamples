/**************************************************************
* File Title: Dev Tool 3 Class Header
* Author: Brogan Avery
* Created : 2021-04-01
***************************************************************/

#ifndef DevTool3_hpp
#define DevTool3_hpp

#include <stdio.h>
#include <string>
#include <iostream>
#include <vector>
#include <iomanip>
#include<cstdlib>
#include "DevTool0.hpp"
#include "httplib.h"
#include "Project.hpp"

using namespace std;


class DevTool3:virtual public DevTool0{
    public:
        DevTool3(); ///constructor
        void menu3();
        void startNewProject();
        void wireFrameTool();
        void stringifyHtml(Project);
        void viewProjectGuide();
};

#endif /* DevTool3_hpp */
