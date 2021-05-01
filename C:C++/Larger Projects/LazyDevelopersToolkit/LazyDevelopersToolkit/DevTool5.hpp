/**************************************************************
* File Title: Dev Tool 5 Class Header
* Author: Brogan Avery
* Created : 2021-04-01
***************************************************************/

#ifndef DEVTOOL5_HPP
#define DEVTOOL5_HPP

#include <string>
#include <iostream>
#include <vector>
#include <iomanip>
#include<cstdlib>
#include "DevTool0.hpp"
#include <array>

using namespace std;

class DevTool5:virtual public DevTool0{
    public:
        DevTool5(); ///constructor
        void menu5();
        void listSongs();
        void listGames();
        void tellJoke();
        void listAnimals();
        void playHangman();
        void playCandyLand();
        string drawCard();
};

#endif // DEVTOOL5_HPP
