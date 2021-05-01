/**************************************************************
* Title: Servers
* Author: Brogan Avery
* Created : 2021-04-18
* Email: bmavery@dmacc.edu
* Course: CIS 164- Advanced C++
* OS: macOS Catalina
* IDE: Xcode
* Description : An app that demos a basic server connection
* Copyright : This is my own original work  based on specifications issued by the course instructor
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
***************************************************************/

#include <string>
#include <iostream>
#include <iomanip>
#include "httplib.h"
#include <iostream>
#include "HttpServer.h"
using namespace httplib;

int main(void) {
      Server svr;
    
      svr.Get("/", [](const Request & /*req*/, Response &res) {
          std::stringstream body;
          body << "<html><h1>Welcome to 1/64 Bank</h1>";
          body << "To view an account balance visit http://localhost:";
          body << "/accounts/x where x is the account number.</p></html>";
          body << "<a href=\"https://github.com/yhirose/cpp-httplib\"";
          res.set_content(body.str(), "text/html");
      });
    
      svr.listen("localhost", 8080);
}
