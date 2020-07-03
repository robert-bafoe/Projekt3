import re
import requests
from bs4 import BeautifulSoup

def get_seznam_mest():
    URL = 'https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ#1'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    mesta = soup.findAll('td',{"headers" : re.compile('.*sb2')})
    odkazy = soup.findAll('td',{"headers" : re.compile('.*sa3')})
    # print(odkazy)
    nazvyMest = []
    for mesto in mesta:
      nazvyMest.append(mesto.text)

    anchors = [td.find('a') for td in odkazy]

    i = 0;
    okresy = {}
    while i < len(nazvyMest):
      kod = anchors[i]['href'].split('=')[-1]
      okresy.update({kod : nazvyMest[i]})
      i += 1

    return okresy

