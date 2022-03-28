# https://www.python.org/dev/peps/pep-0020/
# https://docs.python.org/3/library/stdtypes.html#string-methods
# https://stackoverflow.com/

'''
1. In cadrul unui comentariu, explicati cu cuvintele voastre ce este o variabila
variabila = cutiuta din memorie care stocheaza date
'''

'''
2. Declarati si initializati cate o variabila din fiecare din urmatoarele tipuri:
string, int, float, bool
5. folositi print() si printati in consola 4 propozitii folosind cele 4 variabile. 
(rezolvati nepotrivirile de tip prin ce modalitate doriti)
'''
# variabile
fructe = "mere"
fructe2 = "capsuni"
nr_fructe = 3
greutate_fructe = 1.2
imi_plac_fructele = True

# printuri
print(f"Am cules {nr_fructe} {fructe} care cantaresc {greutate_fructe} kg ")
print(f"Imi plac fructele? {imi_plac_fructele}")
print(f"Imi plac {fructe.upper()}le.")
print(f"Maine culeg {fructe2}.")
print("Bine pa")

'''
3. Utilizat functia type pentru a verifica daca au tipul de date asteptat
4. Rotunjiti float-ul folosind functia round() si salvati aceasta modificare in aceeasi variabila (suprascriere)
Verificati tipul acesteia
'''
# functia type
print(type(fructe), type(fructe2))
print(type(nr_fructe))
print(type(greutate_fructe))
print(type(imi_plac_fructele))

# rotunjire & suprascriere
print(round(greutate_fructe))
print(greutate_fructe)
greutate_fructe = round(greutate_fructe)
print(greutate_fructe)
print(type(greutate_fructe))
print("-------------------------------------------")

''' 
6. citeste de la tastatura numele, prenumele
afiseaza 'Numele complet are x caractere'
'''
nume = "Python"
prenume = "Serpisor"
print(nume, prenume)
nume = input("Alege alt nume")
prenume = input("Alege alt prenume")
print(nume, prenume)
int(input("parola:"))
nume_complet = nume + " " + prenume
print(nume_complet)
x = len(nume_complet)
print(f"{nume_complet} are {x} caractere")
print(len(nume_complet))
print(f"{nume_complet} are" + " " + str(len(nume_complet)) + " " + "caractere")
print(f"{nume} {prenume} are {len(nume_complet)} caractere")
print("-------------------------------------------")

'''
7. citeste de la tastatura lungimea, latimea
afiseaza 'Aria dreptunghiului este x'
'''
lungime = int(input("Lungime:"))
latime = int(input("Latime:"))
arie = lungime * latime
print(f"Aria este:" + " " + str(arie))
print(f"Aria este:" + " " + str(lungime * latime))
print("-------------------------------------------")
'''
8. Avand stringul: 'Coral is either the stupidest animal or the smartest rock'
cititi de la tastatura un int x
afiseaza stringul fara ultimele x caractere
ex: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'
9. declara un string nou care sa fie format din primele 5 caractere + ultimele 5
'''
stringg = "Coral is either the stupidest animal or the smartest rock"
intt = int(input("NR:"))
print(stringg[3])
print(stringg[0:3])
print(stringg[intt])
print(stringg.upper())
print(stringg[::-1])
# afisare fara ultimele x caractere
print(f"Stringg fara ultimele {intt} caractere--> {stringg[:len(stringg) - intt]}")
print(stringg[:len(stringg) - intt])
print(stringg[:-intt])
# afisare primele si ultimele 5 caractere
print(stringg[:5], stringg[-5:])
print(f"{stringg[:5]} {stringg[-5:]}")
print(f"{stringg[:intt]} ... {stringg[-intt:]}")
stringg_cut = stringg[:5] + stringg[-5:]
print(stringg_cut)
print(f"{stringg[:intt] + stringg[-intt:]}")

'''
10.afisati de cate ori apare cuvantul 'the'
11.inlocuieste the cu THE peste tot
'''
count = stringg.count('the')
print(f"Cuvantul 'the' apare de {count} ori")
print(stringg.replace('the', 'THE'))

'''
12.salveaza intr-o variabila si afiseaza indexul de start al cuvantului rock
(hint: este o functie care te ajuta sa faci asta)
folosind aceasta variabila + slicing, afiseaza tot stringul pana la acest cuvant
output: 'Coral is either the stupidest animal or the smartest' 
'''
index = stringg.index('rock')
print(index)
print(stringg[:index])
print("-------------------------------------------")

'''
13.Folosind variabilele definite la exercitiul numarl 2 (cele 4 variabile declarate de tip str, int, float, bool), 
declarati o alta variabila de tip string in care sa le adaugati folosind tehnica de formatare a unui string.
Printeaza rezultatul
'''
# fructe = "mere"
# nr_fructe = 3
# greutate_fructe = 1.2 --a fost suprascrisa
# imi_plac_fructele = True
print(f"{fructe}, {nr_fructe}, {greutate_fructe}, {imi_plac_fructele}")
stringg_all = fructe + str(" ") + str(nr_fructe) + str(" ") + str(greutate_fructe) + str(imi_plac_fructele)
print(stringg_all)
print("-------------------------------------------")

'''
14.avand stringul '0123456789'
afisati doar numerele pare 
acum afisati doar numerele impare
(hint: folositi slicing, controlati din pas)
'''
sir_numere = '0123456789'
print(f"Nr pare: {sir_numere[0::2]}")
print(f"Nr impare: {sir_numere[1::2]}")
print("-------------------------------------------")

''' optionale:
16.citeste de la tastatura un string de dimensiune impara
afiseaza caracterul din mijloc
'''
string_impar = input("String de dimensiune impara:")
print(f"Caracterul din mijloc este: {string_impar[int(len(string_impar) / 2)]}")
print("-------------------------------------------")

'''
17.folosind o singura linie de cod citeste un string de la tastatura (ex: 'alabala portocala')
si salveaza fiecare cuvant intr-o variabila
acum printeaza ambele variabile pentru verificare
'''
cuvant1, cuvant2 = input("Scrie 2 cuvinte:").split()
print(cuvant1)
print(cuvant2)
cuvant1, cuvant2 = "ala", "bala"
print(cuvant1)
print("-------------------------------------------")

'''
18.citeste un string de la tastatura (eg: alabala portocala)
salveaza primul caracter intr-o variabila (indiferent care este el, incearca cu 2 stringuri diferite) 
capitalizeaza acest caracter peste tot, mai putin pentru primul si ultimul caracter
=> alAbAlA portocAla
'''
text = input("Scrie text:")
text1 = text[0]
print(text[0] + text[1:-1].replace(text1, text1.capitalize()) + text[-1])
print("-------------------------------------------")

'''
19.citeste un user de la tastatura
citeste o parola
afiseaza: 'Parola pt user x este ***** si are x caractere'
***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie sa afiseze corect
eg: parola abc => ***
parola abcd => ****
'''
user = input("User:")
parola = input("Parola:")
lungime_parola = len(parola)
parola_steluta = "*" * len(parola)
print(f"Parola pentru user {user} este {parola_steluta} si are {lungime_parola} caractere")
