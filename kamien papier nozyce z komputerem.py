import random

wynik_komputera = 0
wynik_gracza = 0
rundy = input("Podaj ilość rund: ")

wynik_gracza = int(wynik_gracza)
wynik_komputera = int(wynik_komputera)
rundy = int(rundy)

while wynik_gracza < rundy and wynik_komputera < rundy:

    print("kamien\npapier\nnozyce")
    print(f"wynik gracza: {wynik_gracza} , Wynik komputera: {wynik_komputera}")
    gracz1 = input("Gracz 1: ")

    rand_num = random.randint(0, 2)
    if rand_num == 0:
        computer = "kamien"
    elif rand_num == 1:
        computer = "papier"
    elif rand_num == 2:
        computer = "nozyce"

    print("komputer: " + computer)

    if gracz1 == "kamien" and computer == "papier":
        print("computer wygrał")
        wynik_komputera += 1

    elif gracz1 == "papier" and computer == "nozyce":
        print("computer wygrał")
        wynik_komputera += 1

    elif gracz1 == "nozyce" and computer == "kamien":
        print("computer wygrał")
        wynik_komputera += 1

    elif gracz1 == "papier" and computer == "kamien":
        print("Gracz 1 wygrał")
        wynik_gracza += 1

    elif gracz1 == "nozyce" and computer == "papier":
        print("Gracz 1 wygrał")
        wynik_gracza += 1

    elif gracz1 == "kamien" and computer == "nozyce":
        print("Gracz 1 wygrał")
        wynik_gracza += 1

    elif gracz1 == computer:
        print("Remis")

if wynik_gracza > wynik_komputera:
    print(
        f"GRATULACJE, WYGRAŁEŚ ZJEBIE Z WYNIKIEM: {wynik_gracza} do {wynik_komputera} :)... ale i tak jesteś przegrywem zyciowym.")
elif wynik_komputera > wynik_gracza:
    print(
        f"NO TY DEBILU POJEBANY PRZEGRALES KURWA WSZYSTKIE PIENIADZE NA CIEBIE POSTAWIŁEM, JAKIŚ KOMPUTER CIE ROZJEBAŁ {wynik_komputera} do {wynik_gracza}")
else:
    print("REMIS ZJEBÓW JEBANYCH DEBILI")
