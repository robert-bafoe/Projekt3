import re
import requests
from bs4 import BeautifulSoup

KRAJE = {1 : {"nazev":"Hlavní město Praha","kod":"11"},
         2 : {"nazev":"Středočeský kraj","kod":"21"},
         3 : {"nazev":"Jihočeský kraj","kod":"31"},
         4 : {"nazev":"Plzeňský kraj","kod":"32"},
         5 : {"nazev":"Karlovarský kraj","kod":"41"},
         6 : {"nazev":"Ústecký kraj","kod":"42"},
         7 : {"nazev":"Liberecký kraj","kod":"51"},
         8 : {"nazev":"Královéhradecký kraj","kod":"52"},
         9 : {"nazev":"Pardubický kraj","kod":"53"},
         10 : {"nazev":"Kraj Vysočina","kod":"61"},
         11 : {"nazev":"Jihomoravský kraj","kod":"62"},
         12 : {"nazev":"Olomoucký kraj","kod":"71"},
         13 : {"nazev":"Zlínský kraj","kod":"72"},
         14 : {"nazev":"Moravskoslezský kraj","kod":"81"}
         }
ODDELOVAC = "=" * 65

def get_seznam_okresu():
    URL = 'https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ#1'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    okresy_data = soup.findAll('td',{"headers" : re.compile('.*sb2')})
    odkazy_data = soup.findAll('td',{"headers" : re.compile('.*sa3')})
    nazvyOkresu = []
    for okres in okresy_data:
      nazvyOkresu.append(okres.text)

    anchors = [td.find('a') for td in odkazy_data]

    i = 0;
    okresy = {}
    while i < len(nazvyOkresu):
      kod = anchors[i]['href'].split('=')[-1]
      okresy.update({kod : nazvyOkresu[i]})
      i += 1

    return okresy

def sestav_odkaz(kraj,okres):
    odkaz = "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj="+ str(kraj) +"&xnumnuts=" + str(okres)
    return odkaz


def get_kody(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    kody_data = soup.findAll('td', {"headers": re.compile('.t*sa1.*sb1')})
    mesta_data = soup.findAll('td', {"headers": re.compile('.*sb2')})
    nazvyMest = []
    kody = []
    odkazy = []
    for mesto in mesta_data:
        if len(mesto.text) > 1:
            nazvyMest.append(mesto.text)

    tagy = [td.find('a') for td in kody_data]

    for tag in tagy:
      if tag != None:
        kody.append(tag.text)
        odkazy.append(tag.get("href"))

    i = 0
    mesta_kody = {}
    while i < len(nazvyMest):
        mesta_kody.update({kody[i]: {"mesto" : nazvyMest[i],"odkaz" : odkazy[i]}})
        i += 1

    return mesta_kody

def get_vysledky(kod,mesto,finalUrl):
    URL = 'https://volby.cz/pls/ps2017nss/' + finalUrl
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    volici_data = soup.findAll('td', {"headers": "sa2"})
    vydane_data = soup.findAll('td', {"headers": "sa3"})
    platne_data = soup.findAll('td', {"headers": "sa6"})
    strany_data = soup.findAll('td', {"headers": re.compile('.t*sa1.*sb2')})
    hlasy_data = soup.findAll('td', {"headers": re.compile('.t*sa2.*sb3')})
    souhrn = {}
    souhrn.update({"kód obce" : kod})
    souhrn.update({"název obce" : mesto})
    for x in volici_data:
        volici = x.text
        souhrn.update({"voliči v seznamu" : volici.replace('\xa0', '')})

    for x in vydane_data:
        souhrn.update({"vydané obálky" : x.text.replace('\xa0', '')})

    for x in platne_data:
        souhrn.update({"platné hlasy" : x.text.replace('\xa0', '')})

    for strana,hlas in zip(strany_data,hlasy_data):
      souhrn.update({strana.text:hlas.text.replace('\xa0', '')})

    return souhrn


def get_title():
    URL = 'https://volby.cz/pls/ps2017nss/ps2?xjazyk=CZ'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    strany_data = soup.findAll('td',{"headers" : re.compile('.t*sa1.*sb2')})
    title = ["kód obce", "název obce", "voliči v seznamu", "vydané obálky", "platné hlasy"]
    for x in strany_data:
      strana = x.text
      title.append(strana)

    return title