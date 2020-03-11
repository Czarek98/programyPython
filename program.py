import random


print("kamien\npapier\nnozyce")

gracz1 = input("Gracz 1: ")


rand_num = random.randint(0,2)
if rand_num == 0:
    computer = "kamien"
elif rand_num == 1:
    computer = "papier"
elif rand_num == 2:
    computer = "nozyce"

print("komputer: " + computer)

if gracz1 == "kamien" and computer == "papier":
    print("computer wygrał")
elif gracz1 == "papier" and computer == "nozyce":
    print("computer wygrał")
elif gracz1 == "nozyce" and computer == "kamien":
    print("computer wygrał")
elif gracz1 == "papier" and computer == "kamien":
    print("Gracz 1 wygrał")
elif gracz1 == "nozyce" and computer == "papier":
    print("Gracz 1 wygrał")
elif gracz1 == "kamien" and computer == "nozyce":
    print("Gracz 1 wygrał")
elif gracz1 == computer:
    print("Remis")
