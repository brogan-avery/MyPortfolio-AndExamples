/**************************************************************
* Title: Unique Pointers
* Author: Brogan Avery
* Created : 2021-03-23
* Email: bmavery@dmacc.edu
* Course: CIS 164- Advanced C++
* OS: macOS Catalina
* IDE: Xcode
* Description : An app that demonstrates the use of unique pointers and working with their scope in relation to different functions. Calls methods to form new point objects as well as scale them
* Copyright : This is my own original work  based on specifications issued by the course instructor
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
***************************************************************/
#include <iostream>
#include <cmath>
#include <memory>
#include <vector>
using namespace std;
 
const int NUM_POINTS = 5;
const double SCALE = 0.5;
 
class Point {
private:
    double x;
    double y;
public:
    Point(double x, double y): x(x), y(y) {}
    Point(): Point(0, 0) {}
    double getX() {return x;}
    double getY() {return y;}
    void setX(double x) {this->x = x;}
    void setY(double y) {this->y = y;}
};
 
unique_ptr<Point> inputPoint() {
    unique_ptr<Point> point = make_unique<Point>(); /// makes new unique pointer of type Point class
    double x;
    double y;
    cout << "First enter the X coordinate of a point and then the Y coordinate. " << endl;
    cout << "Enter X: ";
    cin >> x;
    cout << "Enter Y: ";
    cin >> y;
    point->setX(x); /// sets the value of x and y for the object that is being pointed to
    point->setY(y);
    
    return point;
}
 
void scalePoint(double &scale, unique_ptr<Point> &point){
    /// vars to hold that scaled values of X and Y
    double scaledX;
    double scaledY;
    scaledX = point->getX() * scale;
    scaledY = point->getY() * scale;
    /// updates the point to the scaled value
    point->setX(scaledX);
    point->setY(scaledY);
    
}
 
vector<unique_ptr<Point>> getScaledPoints(double scale, int numPoints) {
    vector<unique_ptr<Point>> points; /// vector of unique pointers to point objects
    
    ///calls functions and adds point pointer to vector
    for (int i=0; i<numPoints; i++) {
        unique_ptr<Point> point = inputPoint();
        scalePoint(scale, point);
        points.push_back(move(point));
    }
    
    return points; /// returns a vector of points
}
 
int main() {
    vector<unique_ptr<Point>> pointsPtr = getScaledPoints(SCALE, NUM_POINTS);
    for (int i=0; i<NUM_POINTS; i++) {
        cout << "X: " << pointsPtr[i]->getX() <<  ", Y: " << pointsPtr[i]->getY();
        cout << endl;
    }
}

