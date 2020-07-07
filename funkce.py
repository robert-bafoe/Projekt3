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

def sestav_odkaz(kraj,okres):
    odkaz = "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj="+ str(kraj) +"&xnumnuts=" + str(okres)
    return odkaz

def get_mesta_kody(url):
    novaURL = url
    page = requests.get(novaURL)
    soup = BeautifulSoup(page.content, 'html.parser')
    mesta = soup.findAll('td', {"headers": re.compile('.*sb2')})
    odkazy = soup.findAll('td', {"class": "cislo"})
    nazvyMest = []
    for mesto in mesta:
        nazvyMest.append(mesto.text)

    anchors = [td.find('a') for td in odkazy]
    i = 0
    mesta_kody = {}
    while i < len(anchors):
        kod = anchors[i]['href']
        mesta_kody.update({nazvyMest[i] : kod})
        i += 1

    return mesta_kody


def get_vysledky(finalUrl,mesto):
    URL = 'https://volby.cz/pls/ps2017nss/' + finalUrl
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    volici_data = soup.findAll('td', {"headers": "sa2"})
    vydane_data = soup.findAll('td', {"headers": "sa3"})
    platne_data = soup.findAll('td', {"headers": "sa6"})
    tabulka1 = soup.findAll('td', {"headers": "t1sb3"})
    tabulka2 = soup.findAll('td', {"headers": "t2sb3"})
    souhrn = []
    souhrn.append(mesto)
    for x in volici_data:
        volici = x.text
        souhrn.append(volici.replace('\xa0', ''))

    for x in vydane_data:
        souhrn.append(x.text.replace('\xa0', ''))

    for x in platne_data:
        souhrn.append(x.text.replace('\xa0', ''))

    for x in tabulka1:
        souhrn.append(x.text.replace('\xa0', ''))

    for x in tabulka2:
        souhrn.append(x.text.replace('\xa0', ''))

    return souhrn