"""
Pentru toate exercitiile se va folosi notiunea de if in rezolvare.
Indirect veti exersa si operatorii in cadrul conditiilor ramurilor din if
X poate fi initializat direct in cod sau citit de la tastatura, dupa preferinte.
X este un int
"""

# 1.Explica cu cuvintele tale in cadrul unui comentari cum functioneaza un if else
# if else = instructiune care executa un cod in cazul in care conditia este adevarata (if)
# si un alt cod daca conditia este falsa (else)

# 2.Verifica si afiseaza daca x este numar pozitiv sau nu
x = int(input("Numar:"))
if x > 0:
    print("Numarul tau este pozitiv")
else:
    print("Numarul tau nu este pozitiv")

# 3.Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru
if x > 0:
    print("Numarul tau este pozitiv")
elif x == 0:
    print("Numarul tau este neutru")
else:
    print("Numarul tau este negativ")
print("---------------------------------------")

# 4.Verifica si afiseaza daca x este intre -2 si 13
if -2 <= x <= 13:
    print("Nr tau este intre -2 si 13")
else:
    print("Nr tau nu este intre -2 si 13")
print("---------------------------------------")

# 5.Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5
y = int(input("Inca un numar:"))
if x-y < 5:
    print("u la la")
else:
    print("mai incearca")
print("---------------------------------------")

# 6.Verifica daca x NU este intre 5 si 27. (a se folosi ‘not’)
if not x >= 5 and x <= 27:
    print("Nr tau nu este intre 5 si 27")
else:
    print("!!!")
print("---------------------------------------")

# 7. x si y (int)
# Verifica si afiseaza daca sunt egale, daca nu afiseaza care din ele este mai mare
if x == y:
    print("Numerele sunt egale")
else:
    if x > y:
        print(f"{x} > {y}")
    else:
        print(f"{x} < {y}")

# 8. x, y, z - laturile unui triunghi
# Afiseaza daca triunghiul este isoscel, echilateral sau oarecare.
z = int(input("Si inca un numar:"))
if (x == y and x != z) or (x == z and x != y):
    print("Triunghi isoscel")
elif x == y == z:
    print("Triunghi echilateral")
else:
    print("Triunghi oarecare")
print("---------------------------------------")

# 9.Citeste o litera de la tastatura
# Verifica si afiseaza daca este vocala sau nu
litera = str(input("Litera:"))
if litera == "a" or litera == "e" or litera == "i" or litera == "u":
    print("Vocala")
else:
    print("Nu e vocala")
print("---------------------------------------")

# 10.Transforma si printeaza notele din sistem românesc in sistem american dupa cum urmeaza
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F
nota = float(input("Nota:"))
if nota <= 0 or nota > 10:
    print("Nota incorecta")
elif nota > 9:
    print("A")
elif nota > 8:
    print("B")
elif nota > 7:
    print("C")
elif nota > 6:
    print("D")
elif nota > 4:
    print("E")
else:
    print("F")
print("---------------------------------------")

# optionale:
# 11.Verifica daca x are minim 4 cifre (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
nr_cifre = len(str(x))
if nr_cifre >= 4:
    print("nr tau are minim 4 cifre")
else:
    print("nr are mai putin de 4 cifre")

# 12.Verifica daca x are exact 6 cifre !!!!! abs()
if abs(nr_cifre) == 6:
    print("nr tau are exact 6 cifre")
else:
    print("nr nu are 6 cifre")
print("---------------------------------------")

# 13.Verifica daca x este numar par sau impar
if x % 2 == 1:
    print(f"{x} este impar")
else:
    print(f"{x} este par")
print("---------------------------------------")

# 14. x, y, z (int) Afiseaza care este cel mai mare dintre ele?
if x == y == z:
    print("numere egale")
elif x == y or x == z or y == z:
    print("doua numere egale")
elif x > y and x > z:
    print(f"{x} e cel mai mare")
elif y > x and y > z:
    print(f"{y} e cel mai mare")
elif z > x and z > y:
    print(f"{z} e cel mai mare")
print("---------------------------------------")

# 15. a,b,c - reprezinta unghiurile unui triunghi
# Verifica si afiseaza daca triunghiul este valid sau nu
a = int(input("unghi1:"))
b = int(input("unghi2:"))
c = int(input("unghi3:"))
if a + b + c == 180 and a > 0 and b > 0 and c > 0:
    print("Triunghi valid")
else:
    print("Triunghi invalid")
