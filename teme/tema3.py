'''
1.Declara o lista note_muzicale in care sa pui do re mi etc pana la do
Afiseaz-o
Inverseaza ordinea folosind slicing si suprascrie aceasta lista
Printeaza varianta actuala (inversata)
Pe aceasta lista, aplica o metoda care banuiesti ca face acelasi lucru, adica sa ii inverseze ordinea.
(Nu trebuie sa o suprascrii in acest caz, deoarece metoda face asta automat)
Printeaza varianta actuala a listei. Practic ai ajuns inapoi la varianta initiala

Concluzii: slicing e temporar, daca vrei sa pastrezi noua varianta va trebuie sa suprascrii lista
sau sa o salvezi intr-o lista noua.
Metoda gasita de tine, face suprascrierea automat si permanentizeaza aceste modificari.
Ambele variante isi gasesc utilitatea in functie de ce ne dorim in acel moment.
'''
note_muzicale = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
print(note_muzicale)
note_muzicale = note_muzicale[::-1]
print(note_muzicale)
note_muzicale.reverse()
print(note_muzicale)
note_muzicale.append("aaaaa")
print(note_muzicale)
print(note_muzicale[3]) #afiseaza ce e la index 3
print(note_muzicale.index("re")) #afiseaza index-ul lui re
print(note_muzicale[::4]) #afiseaza din 4 in 4
print(note_muzicale[4:]) #afiseaza de la index 4 incolo, inclusiv index 4
print(note_muzicale[:4]) #afiseaza pana la index 4, fara index 4
note_muzicale.insert(3, 3333) #inserare element nou la index 3
print(note_muzicale)
note_muzicale[0:2] = ["tra", "la", "la", "la", "la"] #suprascriere elemente noi peste index 0,1
print(note_muzicale)

# 2.De cate ori apare ‘do’?
print(note_muzicale.count("do"))
print("------------------------------------------")

# 3.Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]
# Gasiti 2 variante sa le uniti intr-o singura lista.
lista_1 = [3, 1, 0, 2]
lista_2 = [6, 5, 4]
print(lista_1 + lista_2)
lista_1.extend(lista_2)
print(lista_1)
# print(lista_1.extend(lista_2)) - not ok, afiseaza None
# lista_1.append(111)
# print(lista_1)
# lista_3 = [5555, 7777]
# lista_1.append(lista_3)
# print(lista_1)

# 4.Sortati si afisati lista generata la ex anterior
# Stergeti numarul 0 folosind o functie
# Afisati iar lista
lista_1.sort()
print(lista_1)
lista_1.remove(0) # remove element
print(lista_1)
lista_1.pop(2) # remove index
print(lista_1)

# 5.Folosind un if verificati lista generata la ex3 si afisati
# Lista este goala
# Lista nu este goala
# 6. Folositi o functie care sa stearga lista de la ex3
# 7. Copy paste la ex 5. Verificati inca o data. Acum ar trebui sa se afiseze ca lista e goala

if lista_1:
    print("lista nu este goala")
else:
    print(("lista este goala"))
lista_1.clear()
if lista_1:
    print("lista nu este goala")
else:
    print(("lista este goala"))
print("------------------------------------------")

# 8.Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folositi o functie ca sa afisati Elevii (cheile)
# 9.Printati cei 3 elevi si notele lor Ex: ‘Ana a luat nota {x}’
# Doar nota o veti lua folosindu-va de cheie
# 10.Dorel a facut contestatie si a primit 6
# Modificati nota lui Dorel in 6. Printati nota dupa modificare

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}

# Python | Accessing Key-value in Dictionary
# Method #1 : Using in operator.
# Method #2 : Using list comprehension.
# Method #3 : Using dict.items()
# Method #4 : Using enumerate()

# You should iterate over keys with: for key in mydictionary:
for key in dict1:
    print("key: %s , value: %s" % (key, dict1[key]))
enumerate(dict1) #???

print(dict1.keys())
print(dict1.values())
print(dict1)
print(*dict1)
print(list(dict1.keys()))
# dict1 = list(dict1.keys())
# print(dict1[1])
print("Ana a luat nota", dict1.get("Ana"), "iar Gigel a luat nota", dict1.get("Gigel"))
print(f"Ana a luat nota {dict1.get('Ana')}, iar Gigel a luat nota {dict1.get('Gigel')}")
print("Dorel a luat nota", dict1["Dorel"])
dict1["Dorel"] = 6
print("Nota Dorel dupa contestatie este", dict1.get("Dorel"))
dict1.update({"Dorel": 6.2})
print("Nota Dorel dupa contestatie este", dict1.get("Dorel"))

# 11.Gigel se transfera din clasa. Cautati o functie care sa il stearga
# Vine un coleg nou. Adaugati Ionica, cu nota 9. Printati dictionarul schimbat
del dict1["Gigel"] # sau dict1.pop('Gigel')
print(dict1)
dict1.update({"Ionica": 9})
print(dict1)
print("------------------------------------------")

# 12.Set
# zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend = {'sambata', 'duminica'}
# Adaugati in zilele_sapt ‘luni’. Afisati zile_sapt

zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
set_new = {'ieri', 'poimaine'}
print(zile_sapt) #afisare random
zile_sapt.add("luni")
print(zile_sapt) #ramane la fel
zile_sapt.add("luniiii")
print(zile_sapt)
sapt_full = zile_sapt.union(set_new)
print(sapt_full)

# 13.Folositi un if si verificati daca Weekend este/ nu este un subset al zilelor din sapt
if weekend.issubset(zile_sapt):
    print(f"{weekend} este un subset al setului : {zile_sapt}")
else:
    print(f"{weekend} nu este un subset")

if weekend < zile_sapt:
    print(f"{weekend} este un subset al setului : {zile_sapt}")
else:
    print(f"{weekend} nu este un subset")

if weekend in zile_sapt: # !!! nu merege in la subset
    print(f"{weekend} este un subset al setului : {zile_sapt}")
else:
    print(f"{weekend} nu este un subset")

# 14.Afisati diferentele dintre aceste 2 seturi (exercitiu 12)
print(zile_sapt.difference(weekend))
difference = zile_sapt - weekend
print(difference)

# 15.Afisati intersectia elementelor din aceste 2 seturi (exercitiu 12)
print(zile_sapt.intersection(weekend))