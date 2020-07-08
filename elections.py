import funkce
import csv
from funkce import KRAJE,ODDELOVAC

okresy = funkce.get_seznam_okresu()

print("Vítej v mini scrapping app!")
print(ODDELOVAC)
print("Seznam krajů:")
for kraj in KRAJE:
    print(f"{kraj} - {KRAJE.get(kraj).get('nazev')}")

print(ODDELOVAC)

volbaKraje = int(input("Zvol kraj: "))
zvoleneOkresy = {}
prefix = KRAJE[volbaKraje]["kod"]
print(ODDELOVAC)

for key in okresy:
  if key.startswith(prefix):
    zvoleneOkresy.update({key : okresy.get(key)})

j = 1
while j <= len(zvoleneOkresy):
    sestavKod = prefix + str(j).zfill(2)
    print(f"{j} - {zvoleneOkresy.get(sestavKod)}")
    j += 1

if volbaKraje > 1:
    volbaOkresu = input("Zvol okres: ")
    finalKod = prefix + volbaOkresu.zfill(2)
else:
    finalKod = "1100"

jmenoSouboru = input("Zadej název výstupního souboru (bez koncovky .csv): ")
soubor = jmenoSouboru + ".csv"
odkazOkres = funkce.sestav_odkaz(volbaKraje,finalKod)
mestaOdkazy = funkce.get_kody(odkazOkres)
nazvySloupcu = funkce.get_title()

with open(soubor, 'w', newline='') as myfile:
    wr = csv.writer(myfile,delimiter=';')
    wr.writerow(nazvySloupcu)
    for klic in mestaOdkazy:
        vysledky = funkce.get_vysledky(klic,mestaOdkazy[klic].get("mesto"),mestaOdkazy[klic].get("odkaz"))
        wr.writerow(vysledky)
        print(vysledky)