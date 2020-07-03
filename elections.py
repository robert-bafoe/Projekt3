import funkce

ODDELOVAC = "=" * 65
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

okresy = funkce.get_seznam_mest()

print("Vítej v mini scrapping app!")
print(ODDELOVAC)
print("Seznam krajů:")
for kraj in KRAJE:
    print(f"{kraj} - {KRAJE.get(kraj).get('nazev')}")

print(ODDELOVAC)

volba = int(input("Zvol kraj: "))
zvoleneOkresy = {}
prefix = KRAJE[volba]["kod"]
print(ODDELOVAC)

for key in okresy:
  if key.startswith(prefix):
    zvoleneOkresy.update({key : okresy.get(key)})

j = 1
while j < len(zvoleneOkresy):
    sestavKod = prefix + "0" + str(j)
    print(f"{j} - {zvoleneOkresy.get(sestavKod)}")
    j += 1

volba2 = input("Zvol okres: ")
finalKod = prefix + "0" + volba2

print(finalKod)