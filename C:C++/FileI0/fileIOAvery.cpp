
/***************************************************
Title: file IO
Author: Brogan Avery
Created: 6/11/20
Description : program reads values from a file, finds the average, and right them back into a new file with the average added to each number
OS: macOS Catalina
* Copyright : This is my own original work  based on specifications issued by the course instructor
***************************************************/

#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;

int main() {
    int score = 0;
    double total = 0;
    double average = 0;
    const int NUM_OF_SCORES = 3; //this is known in this program
    int arrayOfNums[4];
    int arrayLength = sizeof(arrayOfNums)/ sizeof(arrayOfNums[0]);
    
    // Create and open a text file called scores
    ofstream scoresWrite("scores.txt");
    
    // Write to the file to add initial scores
    scoresWrite << 10 << "\n" << 20 << "\n" << 30 << "\n" << -999;
    
    // Close the file
    scoresWrite.close();
    
    //open file to read in
    ifstream scoresRead("scores.txt");
    
    for(int i = 0;score != -999; i++){
        //read in line and display it
        scoresRead >> score;
        arrayOfNums[i] = score;
        
        //so it doesnt also print -999 here or include it in the math
        if (score != -999){
            cout << score << endl;
            
            //get the total for the scores and display the running total each time a score gets added
            total = total + score;
            cout << "Running total: " << total << endl;
        }
    }
    
    //get the average and print it
    average = total/ NUM_OF_SCORES;
    cout <<  "Average of the scores: " << average << endl;
    
    // Close the file again after reading in is done
    scoresRead.close();
    
    // Create and open a text file called scoresOut
    ofstream scoresOutWrite("scoresOut.txt");
    
    // Write to the file
    scoresOutWrite << "The initial scores the were read in from the score file: " << endl;
    
    //writes the original scores (not the -999)
    for(int i = 0 ; i < arrayLength -1; i++){
        scoresOutWrite << arrayOfNums[i] << "\n";
    }
    
    //writes the total of the scores
    scoresOutWrite << "Total of the scores: \n";
    scoresOutWrite << total << "\n";
    
    //writes the average of the scores
    scoresOutWrite << "Average score: \n";
    scoresOutWrite << average << "\n";
    
    //writes out each score + the average
    scoresOutWrite << "Each score plus the average and also the sentinel value: \n";
    for(int i = 0 ; i < arrayLength - 1; i++){
        scoresOutWrite << arrayOfNums[i] + average << "\n";
    }
    scoresOutWrite << arrayOfNums[3];
    
    //close file
    scoresOutWrite.close();

    return 0;
}
