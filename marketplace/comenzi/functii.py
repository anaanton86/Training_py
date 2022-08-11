"""
Comenzile ar trebui sa aiba structura:
("id_comanda": {
    "id_comanda": "Idcomanda" - string,
    "detalii_comanda":
        [{"IdProdus": CantitateProdus}]
        - lista de dictionare de forma IdProdus (string): CantitateProdus (numar intreg),
    "data_inregistrare": "DataInregistrare" - string,
})
"""
import hashlib
import json
from datetime import datetime
from pprint import pprint
from baza_de_date.functii import citeste_datele_din_baza_de_date, scrie_datele_in_baza_de_date
from pytz import country_timezones, timezone


def genereaza_id_comanda(detalii_comanda):
    hash_object = hashlib.md5(bytes(json.dumps(detalii_comanda), encoding='UTF-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig


def adauga_o_comanda():
    """
    Introdu de la tastatura cu textul: "Introduceti produsele din comanda. Pentru a termina, introduceti 'stop':\n"
    Ca prim input dam Produsul, apoi Cantitatea
    Generam ID-ul unic comenzii
    Generam data inregistrarii
    Citim din baza de date
    Generam structura dictionarului
    Scriem in baza de date
    """
    comanda = ""    # ar tb sa fie cu produsele existente
    while comanda != "stop":
        produse = input("Introduceti produsele din comanda:\n")
        cantitate = float(input("Introduceti cantitatea:\n"))
        comanda = input("Pentru a termina introduceti 'stop', altfel continuati cu 'enter'\n")
        detalii_comanda = [{produse: cantitate}]
        id_comanda = genereaza_id_comanda(detalii_comanda)
        data_inregistrare = datetime.now(tz=timezone(country_timezones.get("RO")[0]))
        datele_noastre = citeste_datele_din_baza_de_date()
        datele_noastre["comenzi"][id_comanda] = {
            "id_comanda": id_comanda,
            "detalii_comanda": detalii_comanda,
            "data_inregistrare": data_inregistrare.isoformat()
        }
        scrie_datele_in_baza_de_date(datele_noastre)
    else:
        print("scrie exit")

def modifica_comanda():
    """
    Introduceti de la tastatura textul: "Introduceți identificatorul comenzii care se modifica: "
    Creeam o logica care sa primeasca ca input de la tastatura 4 variante de actiune:
        "Alegeti actiunea ('a' - adaugare produs; 'm ' - modificare cantitate; 's'-sterge produs, 'e'-exit \n")
        Creeam logica pentru cele 4 variante
        Ca input trebuie sa dam produsul si cantitatea pentru 'a' si 'm', pentru 's' dam identificatorul
        Din nou, Citim, Actionam, Scriem
    """
    datele_noastre = citeste_datele_din_baza_de_date()
    data_inregistrare = datetime.now(tz=timezone(country_timezones.get("RO")[0]))
    id_modifica = input("Introduceți id-ul comenzii care se modifica:\n")
    if id_modifica in datele_noastre["comenzi"]:
        print ("Alegeti actiunea ('a' - adaugare produs; 'm ' - schimba cantitate; 's'-sterge produs, 'e'-exit \n")
        actiune = ""
        nume_produs = ""
        # cantitate_produs = ""
        while actiune != 'e':
            actiune = input("a, m, s sau e? \n")
            if actiune == 'e':
                pass # print exit
            elif actiune == 'a':
                while len(nume_produs) < 1 or len(nume_produs) > 50:
                    nume_produs = input("Introduceti numele produsului de adaugat:\n")
                    if len(nume_produs) < 1 or len(nume_produs) > 50:
                        print("Nume Invalid - Lungimea trebuie sa fie intre 1 si 50 de caractere")
                cantitate_produs = abs(int(input('Introduceti cantitatea produsului de adaugat: \n')))
                detalii_comanda = [{nume_produs: cantitate_produs}]
                datele_noastre["comenzi"][id_modifica] = {
                    "id_comanda": id_modifica,
                    "detalii_comanda": detalii_comanda,
                    "data_inregistrare": data_inregistrare.isoformat()
                }
                print("alegeti actiunea")
            elif actiune == 'm': #produs tb sa existe
                while len(nume_produs) < 1 or len(nume_produs) > 50:
                    nume_produs = input("Introduceti numele produsului de modificat:\n")
                    if len(nume_produs) < 1 or len(nume_produs) > 50:
                        print("Nume Invalid - Lungimea trebuie sa fie intre 1 si 50 de caractere")
                cantitate_produs = abs(int(input('Introduceti cantitatea produsului din comanda: \n')))
                detalii_comanda = [{nume_produs: cantitate_produs}]
                if nume_produs in datele_noastre["comenzi"][id_modifica]["detalii_comanda"]:
                    datele_noastre["comenzi"][id_modifica] = {
                        "id_comanda": id_modifica,
                        "detalii_comanda": detalii_comanda,
                        "data_inregistrare": data_inregistrare.isoformat()
                    }
                else:
                    print(f"produsul {nume_produs} nu este in comanda")
                print("alegeti actiunea")
            elif actiune == 's':
                datele_noastre["comenzi"].pop(id_modifica)
                print("alegeti actiunea")
            else:
                actiune = input("a, m, s sau e?\n")
    else:
        print("id gresit")
    scrie_datele_in_baza_de_date(datele_noastre)

# def modifica_comanda():     ## varianta mai scurta
#     datele = citeste_datele_din_baza_de_date()
#     identificator_de_sters = input("Introduceți identificatorul comenzii care se modifica: ")
#     while True:
#         actiune = input(
#             "Alegeti actiunea ('a' - adaugare produs; 'm ' - modificare cantitate; 's'-sterge produs, 'e'-exit \n")
#         detalii_comanda = datele["comenzi"][identificator_de_sters]["detalii_comanda"]
#         if actiune == 'a':
#             add_prod = input("Introduceti produsul:")
#             add_cant = input("Introduceti cantitatea:")
#             detalii_comanda[add_prod] = add_cant
#         elif actiune == 'm':
#             add_prod = input("Introduceti produsul:")
#             add_cant_noua = input("Introduceti cantitatea noua la acest produs")
#             detalii_comanda[add_prod] = add_cant_noua
#         elif actiune == 's':
#             sterge_prod = input("Stergeti produsul:")
#             detalii_comanda.pop(sterge_prod)
#         else:
#             print("Nu ati ales nici o actiune!")
#             break

def listeaza_toate_comenzile():
    """
    Functia trebuie sa afiseze toate comenzile prezente in baza de date.
    Afisarea ar trebui sa contina toate informatiile comenzilor
    """
    datele_noastre = citeste_datele_din_baza_de_date()
    comenzi = datele_noastre["comenzi"]
    if comenzi:
        pprint(comenzi)
    else:
        print("Nu exista comenzi")

def sterge_o_comanda():
    """
    Introdu de la tastatura cu textul  "Introduceți identificatorul comenzii de sters: "
    Cititi, stergeti, Scrieti

    """
    comanda_de_sters = input("introdu id comanda de sters\n")
    toate_datele = citeste_datele_din_baza_de_date()
    if comanda_de_sters in toate_datele["comenzi"]:
        toate_datele["comenzi"].pop(comanda_de_sters)
    else:
        print("id nu exista")
    scrie_datele_in_baza_de_date(toate_datele)
