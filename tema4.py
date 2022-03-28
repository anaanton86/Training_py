# 1.Avand lista
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# Folositi un for ca sa iterati prin toata lista si sa afisati ‘Masina mea preferata este x’
# Faceti acelasi lucru cu range-ul listei
# Faceti acelasi lucru cu un while

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    print(f"Masina mea preferata este {masina}")
for index in range(len(masini)):
    print(f"Masina mea preferata esteeee {masini[index]}")

i = 0
while i < len(masini):
     print(f"Masina mea preferata este {masini[i]}")
     i += 1
else:
    print("gata")

ii = 0
while ii in range(len(masini)):
    print(ii)
    print(f"Masina mea preferata este {masini[ii]}")
    ii += 1
else:
    print("gata gata")

print("-----------------------------------------------")

# 2.Aceeasi lista Folositi un for else
# In for -Modificati elementele din lista astfel incat sa fie scrie cu majuscule,exceptand primul si ultimul
# In else -Printati lista
masini = ['Audi', 'Volvo', 'Bmw', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

for x in range(len(masini)-1):
    if x >= 1:
        print(masini[x].upper())
else:
    print(masini)

for y in range(len(masini)-1):
    if y >= 1:
        masini[y] = masini[y].upper()
else:
    print(masini)

lung=len(masini)-1
for xx in range(len(masini)):
    if xx == 0:
        continue
    if xx == lung:
        continue
    masini[xx] = masini[xx].upper()
print(masini)

for x in range(1, len(masini) - 1):
	masini[x] = masini[x].upper()
print(masini)
# List comprehension.
print([masini[0]] + [masini[x].upper() for x in range(1, len(masini) - 1)] + [masini[-1]])

print("-----------------------------------------------")

# 3.Aceeasi lista, Vine un cumparator care doreste sa cumpere un Mercedes
# Iterati prin ea prin modalitatea aleasa de voi
# Daca masina e mercedes, Printam ‘am gasit masina dorita de dvs’
# Iesim din ciclu folosind un cuvant cheie care face acest lucru
# Altfel, Printam NU Am gasit masina X. Mai cautam

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for m in masini:
    if m == "Mercedes":
        print(f"Am gasit {m}")
        break
else:
    print("Nu am gasit Mercedes")   #cu else pt for

for masina in masini:
    if masina == 'Mercedes':
        print('Gasit')
        break
    else:
        print(f'Am gasit masina {masina}, mai cautam.')   #cu else pt if

for x in range(len(masini)):   #doar daca M si F exista in lista #not musai ok
    if x == masini.index("Mercedes"):
        print("Am gasit masina dorita de dvs, M")
    elif x == masini.index("Fiat"):
        print("Am gasit masina dorita de dvs, F")
        break
    else:
        print(f"Nu am gasit masina.Mai cautam")

print("-----------------------------------------------")

# 4 si 5.Aceasi lista
# Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun.
# Daca masina e Trabant sau Lastun
# Folositi un cuvant cheie care sa dea skip la ce urmeaza (nu trebuie else)
# Printati S-ar putea sa va placa masina x
# Modernizati parcul de masini. Creati o lista goala, masini_vechi
# Iterati prin masini. Cand gasiti Lastun sau Trabant:
# Salvati aceste masini in masini_vechi
# Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
# Printati Modele vechi: x
# Modele noi: x
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for m in masini:
    if m != "Trabant" and m != "Lastun":
        print (f"Va prezentam masina {m}")
    else:
        print (f"S-ar putea sa va placa {m}")

masini_vechi = []
for m in masini:
    if  m == "Trabant" or m == "Lastun":
        masini_vechi.append(m)
        print(masini_vechi)
        masini.remove(m)
        print(masini)

masini.append("Tesla")
print(f"Modele noi: {masini}")
print(f"Modele vechi: {masini_vechi}")
print("-----------------------------------------------")

# 6.Avand dict pret_masini = {
#     'Dacia': 6800,
#     'Lastun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000}
# Vine un client cu un buget de 15000 euro
# Prezentati doar masinile care se incadreaza in acest buget
# Iterati prin dict.items() si accesati masina si pretul
# Printati Pentru un buget de sub 15000 euro puteti alege masina xLastun
# Iterati prin lista
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
buget = 15000
preturi = list(pret_masini.values())
print(preturi)

for p in pret_masini.values():   #sau p in preturi
    if p <= buget:
        print(f"Va prezentam masina cu pretul {p}")

i = 0
for masina in pret_masini.keys():   #se poate si cu masina in pret_masini
    if preturi[i] <= buget:
        print(f"Pentru bugetul de {buget} euro puteti alege masina {masina} care costa {preturi[i]}")
        i += 1

for item in pret_masini.items():
    print(item)
    if item == ('Lastun', 500):
        print(f"Pentru bugetul d-voastra puteti alege {item}")
    else:
        print("cucurigu")

print("-----------------------------------------------")

# 7.Avand lista numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# Iterati prin ea. Afisati de cate ori apare 3 (nu aveti voie sa folositi count)
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

i = 0
for n in numere:
    print(n)
    if n == 3:
        i += 1
print(f"3 apare de {i} ori")

lista_3 = []
for n in numere:
    if n == 3:
        lista_3.append(n)
print(lista_3)
lennn = len(lista_3)
print(f"3 apare de {lennn} ori")

# 8.Aceeasi lista. Iterati prin ea
# Calculati si afisati suma numerelor (nu aveti voie sa folositi sum)
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

i = 0
for n in numere:
    i = i + n
    print(f"Suma este {i}")

# 9.Aceeasi lista. Iterati prin ea
# Afisati cel mai mare numar (nu aveti voie sa folositi max)
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

big = 0
for n in numere:
    if n > big:
        big = n
print(f"{big} este cel mai mare")

i = 0
for n in numere:
    if n > numere[i]:
        numere[i] = n
print(f"{numere[i]} este cel mai mare")
print("-----------------------------------------------")

# 10.Aceeasi lista. Iterati prin ea
# Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa Ex: daca e 3, sa devina -3
# Afisati noua lista
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

negative = []
for n in numere:
    if n > 0:
        n = n - n - n          #sau negative.append(-n)
        negative.append(n)
    else:
        negative.append(n)
print(negative)

# for i in range(len(numere)):
# 	if numere[i] > 0:
# 		numere[i] *= (-1)
# print(numere)

pozitive = []
for n in numere:
    if n < 0:
        n = abs(n)
        pozitive.append(n)
    else:
        pozitive.append(n)
print(pozitive)

print("-----------------------------------------------")

# 11.alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# Iterati prin lista alte_numere. Populati corect celelalte liste si afisati-le.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

for n in alte_numere:
    if n % 2 == 0:
        numere_pare.append(n)
    else:
        numere_impare.append(n)
print(f"nr pare: {numere_pare}")
print(f"nr impare: {numere_impare}")

for n in alte_numere:
    if n >= 0:
        numere_pozitive.append(n)
    else:
        numere_negative.append(n)
print(f"pozitive: {numere_pozitive}")
print(f"negative: {numere_negative}")
print("-----------------------------------------------")

# 12.Aceeasi lista
# Ordonati crescator lista fara sa folositi sort
# Va puteti inspira de aici https://www.youtube.com/watch?v=lyZQPjUT5B4

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
for i in range(len(alte_numere)):
	for k in range(i + 1, len(alte_numere)):
		if alte_numere[i] > alte_numere[k]:
			alte_numere[i], alte_numere[k] = alte_numere[k], alte_numere[i]
print(alte_numere)

# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# lista = []
# for i in range(len(alte_numere)):
#     x = min(alte_numere)
#     lista.append(x)
#     alte_numere.remove(x)
# print(lista)

# numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# for a in range(len(numere)):
#     for b in range(a + 1, len(numere)):
#         if(numere[a] > numere[b]):
#             interim = numere[a]
#             numere[a] = numere[b]
#             numere[b] = interim
# print(f" Ordinea este {numere}")

print("-----------------------------------------------")

# 13.Ghicitoare de numar
# numar_secret = Generati un numar random intre 1 si 30
# Numar_ghicit = None
# Folosind un while
#    User alege un numar
#    Programul ii spune:
# Nr secret e mai mare
# Nr secret e mai mic
# Felicitari! Ai ghicit!

import random
numar_secret = random.randint(1, 30)
print(numar_secret)
numar_ghicit = None
while numar_ghicit != numar_secret:
    numar_ghicit = int(input("alege un nr"))
    if numar_ghicit > numar_secret:
        print("nr secret este mai mic")
    elif numar_ghicit < numar_secret:
        print("nr secret este mai mare")
else:
    print(f"Felicitari, ai ghicit! {numar_secret}")

print("-----------------------------------------------")

# 14.Alegeti un numar de la tastatura
# Ex:7 Scrieti un program care sa genereze in consola urmatoarea piramida
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777

piramida = int(input("alege un nr:"))
i = 1
for i in range(piramida+1):
    print(f"{i}" * i)

print("-----------------------------------------------")

# 15.tastatura_telefon = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9],
#   [0]
# ]
# Iterati prin lista 2d. Printati ‘Cifra curenta este x’
# (hint: nested for - adica for in for)

