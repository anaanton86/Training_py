# 1. Functie care sa calculeze si sa returneze suma a 2 numere
def suma(a,b):
    return(a+b)
raspuns = suma(3,5)
print(f"Suma este: {raspuns}")

def suma(a,b):
    return f"suma dintre {a} si {b} este: {a+b}"
print(suma(3,5))
print("-----------------------------------------")

# 2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar
def numar(x):
    if x % 2 == 0:
        return ("nr este par")
    else:
        return ("nr este impar")
rezultat = numar(11)
print(rezultat)
print("-----------------------------------------")

# 3. Functie care returneaza numarul total de caractere din numele tau complet.
# (nume, prenume, nume_mijlociu)
def nume(user):
    return len(user)
rezultat = nume("Ana banana portocala")
print(f"Lungime nume este: {rezultat}")

def nume_fara_spatii(user):
    spatii = 0
    for index in range(len(user)):
        if user[index] == " ":
            spatii += 1
    return len(user) - spatii
rezultat = nume_fara_spatii("Ana banana portocala")
print(f"Lungime nume fara spatii este: {rezultat}")

# sau asa:
def nume_faraspatii(nume):
	faraspatii = " ".join(nume).split()
	return f"Lungime fara spatii: {len(faraspatii)}"
print(nume_faraspatii("Ana banana portocala"))

print("-----------------------------------------")

# 4. Functie care returneaza aria dreptunghiului
# l = int(input("latime:"))
# L = int(input("lungime:"))
# def arie(l, L):
#     if l > 0 and L > 0:
#         return l * L
#     else:
#         print ("Nu este dreprunghi")
# print(f'Arie dreptunghi este: {arie(l, L)}')
print("-----------------------------------------")

# 5. Functie care returneaza aria cercului
import math            #from math import pi
def arie_cerc(r):
    if r > 0:
        arie = math.pi * r * r
        return arie
    else:
        return "Nu este cerc"
print(f"Arie cerc este: {arie_cerc(3)} m2")   # "{0:.2f}".format(pi) sau f"{pi:.2f}" --> "3.14"
print("-----------------------------------------")

# 6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. Fasle daca nu
def gaseste_c(caracter, string):
    c = 0
    for x in range(len(string)):
        if string[x] == caracter:
            c += 1
    if c > 1:
        return True
    else:
        return False
print(gaseste_c("j", "Ahjsklf jlds"))
print(gaseste_c("J", "Ahjsklf jlds"))

# sau asa
def gaseste(x):
    string = "Ahjsklf jlds"
    if x.lower() in string.lower():   #indif daca e j mic sau mare
        return True
    else:
        return False
print(gaseste("J"))
print(gaseste("?"))

# # sau asa
# def find(y, text):
#     if y in text:
#         return True
#     else:
#         return False
# yy = input("Caracter cautat:")
# textt = input("in textul:")
# print(find(yy, textt))

print("-----------------------------------------")

# 7. Functie fara return, primeste un string si printeaza pe ecran:
# Nr de caractere lower case este x
# Nr de caractere upper case exte y



print("-----------------------------------------")

# 8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive

# 9. Functie care nu retunraza nimic. Primeste 2 numere si PRINTEAZA
# Primul numar x este mai mare decat al doilea nr y
# Al doilea nr y este mai mare decat primul nr x
# Numerele sunt egale.

# 10. Functie care primeste un numar si un set de numere.
# Printeaza ‘am adaugat numarul nou in set’ + returneaza True
# Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False
