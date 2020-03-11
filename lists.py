hajs_od_rodzicow = 200
lista_zakupow = ["ser", "mleko", "jaja", "szynka", "awokado", "makarony", hajs_od_rodzicow]
print(lista_zakupow)
print(len(lista_zakupow))

najwazniejsze = lista_zakupow[4]
print(najwazniejsze)

print("makarony" in lista_zakupow)

if hajs_od_rodzicow in lista_zakupow:
    print("Masz wszystko co najważniejsze")

for rzeczy in lista_zakupow:
    print(rzeczy)
    if lista_zakupow[6] == hajs_od_rodzicow:
        print(f" {hajs_od_rodzicow} zł")