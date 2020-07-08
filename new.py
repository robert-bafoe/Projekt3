import funkce

seznam_okresu = funkce.get_seznam_okresu()
#print(seznam_okresu)
seznam_mest = funkce.get_mesta_kody("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8103")
print(seznam_mest)