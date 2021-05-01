/**************************************************************
* Class: HttpServer
* Author: Brogan Avery
* Created : 2021-04-18
***************************************************************/
#include "httplib.h"
#include <string>
#include <iostream>
#include <iomanip>
#include "account.h"
#include <vector>

using namespace httplib;

class HttpServer {
private:
    char* domain = "localhost";
    int port = 8080;
    std::vector<Account> accounts;
public:
    void startServer() {
        Server svr;
 
        svr.Get("/", [this](const Request&, Response& res) {
            std::stringstream body;
            body << "<html><h1>Welcome to 1/64 Bank</h1>";
            body << "To view an account balance visit http://localhost:" << this->port;
            body << "/accounts/x where x is the account number.</p></html>";
            res.set_content(body.str(), "text/html");
        });
 
        svr.Get(R"(/accounts/(\d+))", [&](const Request& req, Response& res) {

            std::stringstream body;
            body << "<html>";
           
            for (int i = 0; i< accounts.size(); i++){
                if(stoi(std::string(req.matches[accounts[i].getId()])) ){
                    body << "<p>" << accounts[i].getId() << " " << accounts[i].getBalance() << "</p>";
                }
            }
 
            body << "</html>";
            res.set_content(body.str(), "text/html");
        });
 
        std::cout << "Starting server at http://" << domain << ":" << port << std::endl;
        svr.listen(domain, port);
    }
    
    void populateVector(){///  create 3 tests accounts and adds them to the array
        Account acc1(1);
        Account acc2(2);
        Account acc3(3);
        
        acc1.setBalance(300);
        acc2.setBalance(800);
        acc3.setBalance(450);
        
        this->accounts.push_back(acc1);
        this->accounts.push_back(acc2);
        this->accounts.push_back(acc3);
    }
};
