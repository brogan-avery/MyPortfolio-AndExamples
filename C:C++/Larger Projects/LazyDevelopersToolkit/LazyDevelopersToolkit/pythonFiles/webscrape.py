
"""
***************************************************
Title: Web Scrape
Author: Brogan Avery
Created: 2021-04-01
Description : a file that is meant to run only once to generate helper file(s) to read into C++ rather than writing it all by hand
OS: macOS Catalina
* Copyright : This is my own original work  based on specifications issued by the course instructor
***************************************************
"""
import bs4
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    problems = [] # will store the names/titles of practice problems
    links = [] # will store the web link to the problem in the parallel problem array

    # website pages URLs and directories
    urlBase = "https://www.codechef.com"
    easyUrl = urlBase + "/problems/easy"
    mediumUrl = urlBase + "/problems/medium"
    hardUrl = urlBase + "/problems/hard"

    # call to get the problems from a table with medium difficultly practice problem
    mediumPage = requests.get(mediumUrl)

    # makes the text readable and searches for problems and links
    soup = BeautifulSoup(mediumPage.text, "html.parser")
    problems = soup.tbody.find_all('b')
    divs = soup.tbody.find_all(class_ = 'problemname')
    for div in divs:
        links.append(div.a['href'])

    numOfChoices = 100
    # writes to file to read into C++
    with open('practiceCodeProblems.txt', 'w') as file: # creates a file of problems to read into the C++ program
        for i in range(numOfChoices): # limits so there isn't 900+ options
            file.write(problems[i].text + "\n")

    # writes to file to copy and paste into my C++ code because its a lot to type
    with open('functionBodyForC.txt', 'w') as file:
        for i in range(numOfChoices):
            file.write('if (userInput == "' + str(i+1) + '"){\n')
            file.write('    system("open '+ urlBase + links[i] + '");\n')
            file.write("}\n")
