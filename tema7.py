#recapitulare
class Chef:    #clasa parinte/baza  #un copil poate avea mai multi parinti
    cutite = 2
    sort = 1

    def make_salad(self):
        print("salad")

    def make_fries(self):
        print("fries")

class ItalianChef(Chef):   #clasa copil  #un copil poate avea si el copii
    sucitor = True

    def make_pizza(self):
        return "pizza"

class JapanesseChef(Chef):   #clasa copil
    def make_sushi(self):
        print("sushi")

bucatar = Chef()
bucatar.make_salad()
bucatar.make_fries()

bucatarMario = ItalianChef()
bucatarMario.make_salad()
bucatarMario.make_fries()
print(f"Mario stie sa faca si {bucatarMario.make_pizza()}")
print(bucatarMario.sucitor)

bucatarLee = JapanesseChef()
bucatarLee.make_sushi()
print(bucatarLee.sort)
print("--------------------------")

#polimorfism - def language
class Romania:
    def language(self):
        print("romanian")

class USA:
    def language(self):
        print("english")

obj_ro = Romania()
obj_usa = USA()
for country in (obj_ro, obj_usa):
    country.language()
print("--------------------------")


#TEMA7
# ABSTRACTION
# Clasa abstracta FormaGeometrica
# Contine un field PI=3.14
# Contine o metoda abstracta aria
# Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi’

from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    pi = 3.14
    @abstractmethod
    def aria(self):
        pass
        #raise NotImplementedError

    def descrie(self):
        print("cel mai probab am colturi")

# INHERITANCE
# Clasa Patrat - mosteneste FormaGeometrica
# constructor pt latura
# ENCAPSULATION
# latura este proprietate privata
# Implementati getter, setter, deleter pt latura
# Implementati metoda ceruta de clasa abstracta

class Patrat(FormaGeometrica):
    latura = 1

# Clasa Cerc - mosteneste FormaGeometrica
# constructor pt raza
# raza este proprietate privata
# Implementati getter, setter, deleter pt raza
# Implementati metoda ceruta de interfata - in calcul folositi field PI mostenit din clasa parinte
# POLYMORPHISM
# Definiti o noua metoda descrie() - printati ‘Eu nu am colturi’

# Creati un obiect de tip Patrat si jucati-va cu metodele lui
# Creati un obiect de tip Cerc si jucati-va cu metodele lui
