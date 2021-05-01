"""
***************************************************
Title: Weather Plotting
Author: Brogan Avery
Created: 2020-10-07
Description : uses weather data from CSV files to make charts and graphs
OS: macOS Catalina
Copyright : This is my own original work based on specifications issued by the course instructor
***************************************************
"""

from matplotlib.pyplot import *
from pandas import *
from numpy import *

#————————————————————————————————————————————————————————————————————————————————————
if __name__ == '__main__':

# simple charts :

# these both show the avg temp of the day on the 1st, the 12th, and the 24th of every month for the year 2015

# Madrid

    madrid = read_csv("madrid.csv", sep=',')

    madrid = madrid[madrid['CET'].str.contains("/1/15|/12/15|/24/15")]

    y = madrid['Mean TemperatureC']
    x = madrid['CET']

    xticks(rotation='vertical')

    plot(x,y)
    show()

# Mount Rainier
    rainier = read_csv("Rainier.csv", sep=',')

    rainier = rainier[rainier['Date'].str.contains("/1/15|/12/15|/24/15")]

    y = rainier['Temperature AVG']
    x = rainier['Date']

    xticks(rotation='vertical')

    plot(x,y)
    show()

# these are ok on their own but cannot be compared since they are backwards (12 - 1 and 1 - 12) and one is in C and the other is in F. And with no lables its not super clear

# more complex charts  :

# Madrid

    y = madrid['Mean TemperatureC']
    x = madrid['CET']

# convert to F
    y = multiply(y,9)
    y = divide(y,5)
    y = add(y,32)

# Rainier

# reordered from 1 to 12
    yR = rainier['Temperature AVG']
    xR = rainier['Date']

    rainier = rainier.reindex(index=rainier.index[::-1])

    print(rainier)

# combining

    fig, ax = subplots()
    ax.plot(x,y, 'red')
    ax.plot(x,yR, 'black')

    ax.set_title('Avg Daily temps for 2015', color='blue')
    ax.legend(['Madrid','Mount Rainier'])
    ax.yaxis.set_label_text('Temp (F)')
    xticks(rotation='vertical')

    show()

# this chart does a better job to compare the two and explains what is going on better





