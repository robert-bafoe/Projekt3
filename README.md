# Projekt3
Election scraper

FUNKCE:
- get_seznam_kraju
- get_seznam_okresu
- get_seznam_obci
- get_data_obec
- insert_data

POUŽITÍ:
- uživatel vybere ze seznamu krajů (data získám pomocí funkce get_seznam_kraju) -> KRAJ
  - uloží se do slovníku s klíči id, kraj, cislo
- uživatel vybere ze seznamu okresů (data získám pomocí funkce get_seznam_okresu) -> OKRES
  - uloží se do slovníku s klíči id, okres, cislo
- program si vytvoří list s čísly obcí ve vybraném okresu (pomocí funkce get_seznam_obci)
- vytvoří a otevře se csv soubor
- v cyklu se stáhnou data z dynamicky vytvořeného odkazu s číslem obce z listu
  - zpracují se (rozparsování do jednitlivých objektů)
  - zapíšou se do csv souboru pomocí funkce insert_data
- zavře se csv soubor
