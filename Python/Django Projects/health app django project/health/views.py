from django.shortcuts import render
from django.http import HttpResponse
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# this scrapes a website for health news and pulls the urls from the section of the website where new stories are displayed.
def index(request):
    template = "health/index.html"

    url = 'https://www.everydayhealth.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    links = []
    linkTexts = []
    for a in soup.find_all('a', class_='homepage-hero__article-link'):
        # print(a.get('href'))
        links.append(a.get('href'))
        linkTexts.append(a.text)

    i = 0
    linksList = []
    for item in links:
        linkDict = {'link' : links[i], 'linkText' : linkTexts[i]}
        i = i + 1
        linksList.append(linkDict)

    return render(request,template, {'linksList' : linksList })
