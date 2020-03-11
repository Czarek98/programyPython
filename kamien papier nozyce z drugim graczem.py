print("kamien\npapier\nnozyce")

gracz1 = input("Gracz 1: ")
print("NIE PODGLADAJ\n" *50)
gracz2 = input("Gracz 2: ")

if gracz1 == "kamien" and gracz2 == "papier":
    print("Gracz 2 wygrał")
elif gracz1 == "papier" and gracz2 == "nozyce":
    print("Gracz 2 wygrał")
elif gracz1 == "nozyce" and gracz2 == "kamien":
    print("Gracz 2 wygrał")
elif gracz1 == "papier" and gracz2 == "kamien":
    print("Gracz 1 wygrał")
elif gracz1 == "nozyce" and gracz2 == "papier":
    print("Gracz 1 wygrał")
elif gracz1 == "kamien" and gracz2 == "nozyce":
    print("Gracz 1 wygrał")
elif gracz1 == gracz2:
    print("Remis")
