print("GRA W WISIELCA")
haslo = input("Podaj słowo dla przeciwnika: ")
haslo=haslo.lower()
lista = list(haslo)
print(f"NIE PODGLĄDAJ !!\n" *20)


for i in range(len(haslo)):
    lista[i] = "_"
zycia = 6
while zycia > 0:
    print("Pozostało ci: ", zycia, " żyć")
    print(" ")
    print(' '.join(lista))
    print(" ")
    litera = input("Podaj litere: ")
    litera = litera.lower()

    if litera in haslo:
        for i in range(len(haslo)):
            if haslo[i] == litera:
                lista[i] = litera
        if "".join(map(str,lista)) == haslo:
            print(f"Wygrałeś ! z {zycia} życiami")
            print("Pozostało ci: ", zycia, " żyć")
            print(" ")
            print("Ukryte słowo to:", ''.join(lista))
            print(" ")
            break


    else:
        zycia -= 1
        if zycia < 1:
            print("Przegrales!")
            print("Pozostało ci: ", zycia, " żyć")
            print("Ukryte słowo to:", haslo)
            print(" ")
            break
