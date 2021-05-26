
"""
Created on Fri Mar  6 

@author: Brogan Avery 

title: scraper
"""

import requests
import bs4 as bs

url = 'https://www.dmacc.edu/schedule/Pages/result.aspx?Term=202001&Campus=1&Subject=CIS&CourseNumber=CIS189'
response = requests.get(url)
html = response.content
with open("requestResult.txt","w+") as file:
    file.writelines(str(html))

soup = bs.BeautifulSoup(open("requestResult.txt"), 'html.parser')
print(soup.prettify())
