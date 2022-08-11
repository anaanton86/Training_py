"""

Produsele ar trebui sa aiba structura:
("id_produs": {
    "nume_produs": "NumeleProdusului" - string,
    "pret": "Pret" - intreg/float,
    "data_inregistrare": "DataInregistrare" - string,
})

"""
import hashlib
from datetime import datetime

from pytz import country_timezones, timezone

from marketplace.baza_de_date.functii import citeste_datele_din_baza_de_date, scrie_datele_in_baza_de_date


def genereaza_id_produs(nume_produs, pret):
    hash_object = hashlib.md5(bytes(nume_produs + pret, encoding='UTF-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig


def adauga_un_produs():
    nume_produs = ""
    pret = ""
    while len(nume_produs) < 1 or len(nume_produs) > 50:
        nume_produs = input('\nIntroduceti numele produsului de adaugat: ')
        if len(nume_produs) < 1 or len(nume_produs) > 50:
            print("Nume Invalid - Lungimea numelui trebuie sa fie intre 1 si 50 de caractere")
    while len(pret) < 1:
        pret = input('\nIntroduceti pretului produsului de adaugat: ')
    id_produs = genereaza_id_produs(nume_produs, pret)
    data_inregistrare = datetime.now(tz=timezone(country_timezones.get("RO")[0]))
    datele = citeste_datele_din_baza_de_date()
    datele["produse"][id_produs] = {
        'nume_produs': nume_produs,
        'pret': pret,
        'data_inregistrare': data_inregistrare.isoformat()
    }

    scrie_datele_in_baza_de_date(datele)


def listeaza_toate_produsele():
    """
    Functia trebuie sa afiseze toate produsele prezente in baza de date.
    Afisarea ar trebui sa contina toate informatiile produselor
    """
    baza_de_date = citeste_datele_din_baza_de_date()
    chei_unice_produse = baza_de_date["produse"]

    print("{}\t{}\t{}".format("Produs", "Pret", "Data inregistrare"))
    print("{}\t{}\t{}".format("Produs", "Pret", "Data inregistrare"))
    for i in chei_unice_produse:
        temp = list(baza_de_date["produse"][i].values())
        print("{}\t{}\t\t{}".format(temp[0], temp[1], temp[2]))


def sterge_produs():
    nume_produs = input("\nNume produs: ")
    baza_de_date = citeste_datele_din_baza_de_date()
    for i in baza_de_date["produse"].keys():
        if nume_produs in list(baza_de_date["produse"][i].values()):
            print("Produsul {} cu id-ul {} a fost sters".format(nume_produs, i))
            baza_de_date["produse"].pop(i, None)  # None este inclus pentru a evita exceptia KeyError
            scrie_datele_in_baza_de_date(baza_de_date)
            break
