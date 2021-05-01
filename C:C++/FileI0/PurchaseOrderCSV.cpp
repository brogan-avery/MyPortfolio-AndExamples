/**************************************************************
* Title: purchase order csv
* Author: Brogan Avery
* Created : 2021-02-09
* Email: bmavery@dmacc.edu
* Course: CIS 164- Advanced C++
* OS: macOS Catalina
* IDE: Xcode
* Description : An app that lets users enter in store information that will be saved to a CSV and then lets then view the order total
* Copyright : This is my own original work  based on specifications issued by the course instructor
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
***************************************************************/

#include <string>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>

using namespace std;

int main() {
    string sku = " ";
    int qty = 0;
    double price = 0;
    
//====== WRITING TO FILE ======
    while (sku != "q"){
        
        cout << "Enter the following information in about the product: " << endl;
        
        cout << "SKU (q to quit): " << endl;
        cin >> sku;
        
        if (sku == "q"){
            break;
        }
        
        cout << "Quantity: " << endl;
        cin >> qty;
        
        cout << "Price: " << endl;
        cin >> price;
        
        // open or create file to WRITE to
        ofstream csvWrite("purchaseOrders.csv",ios_base::app);
        
        // Write to file
        csvWrite << sku << "\n " << qty << "\n" << price << "\n";
        
        // Close file
        csvWrite.close();
    }
 
//========= READING FROM FILE ============
    
  //======= step 1 of reading from file =========
    
    string line = " "; // each line's text
    int lineCount = 0; // number of lines of text in file
    
        //open file to READ from
        ifstream csvRead("purchaseOrders.csv", ios::in);
        
        // gets the number of lines of text in the file
        while(getline(csvRead,line)){
            lineCount++;
        }
        
        //close file
        csvRead.close();
        
  //========== step 2 of reading from file ==========

    //open file to READ from
    ifstream csvRead2("purchaseOrders.csv" , ios::in);

    vector<int> qtys; // reads every third line into an vector
    vector<double> prices; // reads every third line into an vector
    double total = 0;

    // reads all lines and stores the values for the lines with price and qty to the respective vector
    for(int i = 2, j = 1; i < lineCount + 2; i++, j++){
        getline(csvRead2,line);
        if (i % 3 == 0){
            int intLine = stoi(line); // cast to int from string
            qtys.push_back(intLine); // adds to end of qtys vector
        }
        
        if (j % 3 == 0){
            double doubleLine = stod(line); // cast to double from string
            prices.push_back(doubleLine); // adds to end of prices vector
        }
    }
    
    //closes file
    csvRead2.close();
    
    // at the sub totals of the sum of the price and quantity to the total price
    for(int i = 0; i < qtys.size(); i++){
        total = total + prices[i] * qtys[i];
    }
    
    cout <<"Order Total: $" << fixed << setprecision(2) << total << endl;
    
    cout << "goodbye" << endl;
    
    return 0;
}
