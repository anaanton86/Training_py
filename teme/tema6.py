#Pentru toate clasele, creati cel putin 2 obiecte cu valori diferite
# si apelati toate metodele clasei
import math

# 1. Clasa Cerc
# Atribute: raza, culoare. Constructor pt ambele atribute
# Metode:
# descrie_cerc() - va PRINTA culoarea si raza
# aria() - va RETURNA aria
# diametru()
# circumferinta()

class Cerc:
    raza = None
    culoare = None

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(f"Raza cerc este: {self.raza}")
        print(f"Culoare cerc este: {self.culoare}")

    def aria(self):
        arie_cerc = math.pi * self.raza * self.raza
        return(f"aria este: {arie_cerc:.2f}")

    def diametru(self):
        diam_cerc = 2 * self.raza
        return(f"diametru este: {diam_cerc}")
    def circumferinta(self):
        circumf_cerc = 2 * math.pi * self.raza
        return (f"circumferinta este: {circumf_cerc:.3f}")

cerc1 = Cerc(3, "verde")
print(cerc1.descrie_cerc())
print(cerc1.aria())
print(cerc1.diametru())
print(cerc1.circumferinta())
print("-----------------------------------------")

# 2.Clasa Dreptunghi
# Atribute: lungime, latime, culoare. Constructor pt toate atributele
# Metode:
# descrie() va PRINTA lungime, latime, culoare
# aria()
# perimetrul()
# schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic.
# Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare.
# Puteti verifica schimbarea culorii prin apelarea metodei descrie().

class Dreptunghi:
    lungime = 1
    latime = 1
    culoare = "verde"

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descriere(self):
        return(f"Dreptunghi de culoare {self.culoare}, L: {self.lungime}, l: {self.latime}")

    def aria(self):
        arie_drept = self.lungime * self.latime
        return(f"aria: {arie_drept}")

    def perimetru(self):
        perim_drept = 2 * (self.lungime + self.latime)
        return(f"perimetru: {perim_drept}")

    def schimba_culoare(self, noua_culoare):
        self.culoare = noua_culoare
        # return(noua_culoare)

dreptunghi1 = Dreptunghi(4, 2, "galben")
print(dreptunghi1.descriere())
print(dreptunghi1.aria())
print(dreptunghi1.perimetru())
print(dreptunghi1.schimba_culoare("gri"))
print(dreptunghi1.descriere())
print("-----------------------------------------")

# 3.Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor() pt toate atributele // constructor reprezinta __init__
# Metode:
# descrie() print nume, prenume, salariu
# nume_complet()
# salariu_lunar()
# salariu_anual()
# marire_salariu(procent)

class Angajat:
    nume = ""
    prenume = ""
    salariu = 1

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descriere(self):
        return(f"Nume: {self.nume}, Prenume: {self.prenume}, salariu: {self.salariu} ron")

    def nume_complet(self):
        numecomplet = self.nume + " " + self.prenume
        return(f"Nume complet: {numecomplet}")

    def salariu_lunar(self):
        return(f"Salariu lunar: {self.salariu} ron")

    def salariu_anual(self):
        salariuan = self.salariu * 12
        return(f"Salariu anual: {salariuan} ron")

    # def marire_salariu(self, procent):
    #     marire = self.salariu + self.salariu * (procent / 100)
    #     self.salariu = marire
    #     return(f"Dupa marire salariul este: {marire}")

angajat1 = Angajat("Marin", "Marinel", "3000")
print(angajat1.descriere())
print(angajat1.nume_complet())
print(angajat1.salariu_lunar())
print(angajat1.salariu_anual())
# print(angajat1.marire_salariu(10))
print("-----------------------------------------")

# 4.Clasa Factura
# Atribute: seria (va fi constanta, nu trebuie constructor, toate facturile vor avea aceeasi serie),
# numar, nume_produs, cantitate, pret_buc
# Constructor: toate atributele, fara serie
# Metode:
# schimba_cantitatea(cantitate)
# schimba_pretul(pret)
# schimba_nume_produs(nume)
# genereaza_factura() - va printa tabelar daca reusiti
# Factura seria x numar y
# Data: generati automat data de azi
# Produs | cantitate | pret bucata | Total “
# Telefon |      7       |       700       | 49000
# Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/

class Factura:
    seria = 123
    numar = 1
    nume_produs = ""
    cantitate = 1
    pret_buc = 1

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate_noua):
        self.cantitate = cantitate_noua

    def schimba_pretul(self, pret_nou):
        self.pret_buc = pret_nou

    def schimba_nume_produs(self, nume_nou):
        self.nume_produs = nume_nou

produs1 = Factura(11, "macaroane", 2, 20)
print(produs1.nume_produs)
print(produs1.schimba_nume_produs("spaghete"))
print(produs1.nume_produs)
print(produs1.seria)
print(produs1.schimba_pretul(25))
print(produs1.pret_buc)


# 5.Clasa Cont
# Atribute: iban, titular_cont, sold. Constructor pentru toate
# Metode:
# afisare_sold() - Titularul x are in contul y suma de n lei
# debitare_cont(suma)
# creditare_cont(suma)
