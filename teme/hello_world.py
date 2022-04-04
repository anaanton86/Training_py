# printam in consola un mesaj
print ('Hello World!')

# comentariu shortcut ctrl+/
# ctrl D copiaza
# ctrl Z undo


# draft/incercari

# alte_numere = [7, -4, 3, 9, -6]   #not ok. why?
# i = 1
# for n in alte_numere:
#     if n > alte_numere[i]:
#         interim = alte_numere[i-1]
#         alte_numere[i-1] = alte_numere[i]
#         alte_numere[i] = interim
#     i += 1
# print(alte_numere)

print("----------------------------")

numar = -1
while numar in range(-1, 7):
    print(numar)
    numar += 1

print("----------------------------")

alt_numar = 2
lista = [1, 2, 32, 2, 4]
for numar in lista:
    if alt_numar == numar:
        print(alt_numar)

print("----------------------------")

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 4]

for n1 in lista1:
    for n2 in lista2:
        if n1 == n2:
            print(n1)

print("----------------------------")

lista_numere = []
for n in range(10):
    lista_numere.append(n)
print(lista_numere)

lista_altenumere = [n for n in range(10) if n < 5]    #list comprehension
print(lista_altenumere)

print("----------------------------")

elevi = ["marcel", "maria", "gerula"]
note = [5, 10, 7.5]

# catalog = {}
# for elev in elevi:
#     for nota in note:
#         catalog[elev] = nota    #atribuie 7.5 pt toti elevii
# print(catalog)

catalog = {}     #varianta corecta - facem dict din 2 liste egale
for index in range(len(elevi)):
    catalog[elevi[index]] = note[index]
print(catalog)

# dict comprehension (listele sunt egale)
catalog_nou = {elevi[index]: note[index] for index in range(len(elevi))}
print(catalog_nou)


note = [5, 10, 7.5]
catalog_copii = {
    "marcel": 0,
    "maria": 0,
    "gerula": 0
}
for index, element in enumerate(catalog_copii):
    catalog_copii[element] = note[index]
    print(index, element)
print(catalog_copii)

for index in range(len(note)):
    catalog_copii[index] = note[index]
print(catalog_copii)