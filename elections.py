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

while True:
    try:
        volbaKraje = int(input('Zvol kraj: '))
        if volbaKraje < 1 or volbaKraje > 14:
            raise ValueError
        break
    except ValueError:
        print("Špatné zadání. Zvol číslo kraje (1 - 14).")

zvoleneOkresy = {}
prefix = KRAJE[volbaKraje]["kod"]
print(ODDELOVAC)

for key in okresy:
  if key.startswith(prefix):
    zvoleneOkresy.update({key : okresy.get(key)})

j = 1
while j <= len(zvoleneOkresy):
    sestavKod = prefix + str(j).zfill(2)
    if prefix == "11":
        print("Hlavní město Praha")
    else:
        print(f"{j} - {zvoleneOkresy.get(sestavKod)}")

    j += 1

if volbaKraje > 1:
    while True:
        try:
            volbaOkresu = int(input('Zvol okres: '))
            if volbaOkresu < 1 or volbaOkresu > len(zvoleneOkresy):
                raise ValueError
            break
        except ValueError:
            print(f"Špatné zadání. Zvol číslo okresu (1 - {len(zvoleneOkresy)}).")

    finalKod = prefix + str(volbaOkresu).zfill(2)
else:
    finalKod = "1100"

print(ODDELOVAC)
jmenoSouboru = input("Zadej název výstupního souboru (bez koncovky .csv): ")
if jmenoSouboru == "":
    print(f"Nezadal jsi žádný název. Název souboru bude {zvoleneOkresy.get(finalKod)}.csv")
    jmenoSouboru = zvoleneOkresy.get(finalKod)

print(ODDELOVAC)
soubor = jmenoSouboru + ".csv"
odkazOkres = funkce.sestav_odkaz(volbaKraje,finalKod)
mestaOdkazy = funkce.get_kody(odkazOkres)
vsechnyVysledky = []
titulky = []

for klic in mestaOdkazy:
    vysledky = funkce.get_vysledky(klic,mestaOdkazy[klic].get("mesto"),mestaOdkazy[klic].get("odkaz"))
    vsechnyVysledky.append(vysledky)

for zaznam in vsechnyVysledky:
    nazvy = list(zaznam.keys())
    titulky.append(nazvy)

result = sum(titulky, [])
nazvySloupcu = list(dict.fromkeys(result))

with open(soubor, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=nazvySloupcu)
    writer.writeheader()
    for data in vsechnyVysledky:
        writer.writerow(data)