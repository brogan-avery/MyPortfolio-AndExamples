/**************************************************************
* Title: Output Parameters
* Author: Brogan Avery
* Created : 2021-03-23
* Email: bmavery@dmacc.edu
* Course: CIS 164- Advanced C++
* OS: macOS Catalina
* IDE: Xcode
* Description : creates point objects like graph coordinates and then scales them. Demonstrates passing by reference and working with scopes
* Copyright : This is my own original work  based on specifications issued by the course instructor
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
***************************************************************/

#include <iostream>
#include <cmath>
using namespace std;
 
const int NUM_POINTS = 5;
const double SCALE = 0.5;
 
class Point {
    private:
        double x;
        double y;
    public:
        Point() : x(0), y(0) {}
        double getX() {return x;}
        double getY() {return y;}
        void setX(double x) {this->x = x;}
        void setY(double y) {this->y = y;}
};
 
void inputPoint(Point &point){
    double x;
    double y;
    cout << "First enter the X coordinate of a point and then the Y coordinate. " << endl;
    cout << "Enter X: ";
    cin >> x;
    cout << "Enter Y: ";
    cin >> y;
    point.setX(x);
    point.setY(y);
}
 
void scalePoint(Point &point){
    /// vars to hold that scaled values of X and Y
    double scaledX;
    double scaledY;
    scaledX = point.getX() * SCALE;
    scaledY = point.getY() * SCALE;
    /// updates the point to the scaled value
    point.setX(scaledX);
    point.setY(scaledY);
}

void getScaledPoints(double scale, int size, Point points[]){
    for (int i=0; i<NUM_POINTS; i++) {
        Point newPoint; /// point object that is passed to other functions by reference to fill the array
        inputPoint(newPoint);
        scalePoint(newPoint);
        points[i] = newPoint; /// adds pointer to point object in array
    }
}
 
int main() {
    Point points[NUM_POINTS]; /// declares array of 5 objects from point class
    getScaledPoints(SCALE, NUM_POINTS, points); ///0.5, 5, points array
    for (int i=0; i<NUM_POINTS; i++) {
        cout << "X: " << points[i].getX() <<  ", Y: " << points[i].getY() << endl;
    }
}
