# variabile
import json
import os

marca = 'Volvo'
model = 'XC60'

print (f'Am cumparat o masina marca: {marca}')
print (f'Este modelul: {model}')

# draft incercari

class Cerc:
    raza= 1
    color= "mov"
    def __init__(self, raza, color):
        self.raza = raza
        self.color = color
    def descriere_cerc(self):
        print(f"culoarea este: {self.color}")

cerc_1 = Cerc(8,'alb')
print(cerc_1.descriere_cerc())
cerc_1.descriere_cerc()

print("---------------------------")

# # interactiune cu fisiere (txt, json)
#
# def citeste_din_fisier(cale_fisier):
#     with open(cale_fisier, 'r') as file:
#         return file.readline()
#
# def citeste_din_fisier_json(cale_fisier):
#     with open(cale_fisier, 'r') as file:
#         return json.load(file)
#
# def scrie_in_fisier(cale_fisier, randuri_informatii):
#     with open(cale_fisier, 'w') as file:
#         file.writelines(randuri_informatii)
#
# def scrie_in_fisier_json(cale_fisier, randuri_informatii):
#     with open(cale_fisier, 'w') as file:
#         json.dump(randuri_informatii, file)
#
# # interactiune cu fisiere (excel, csv)
#
# import pandas as pd
# file_location = "path_to_excel.xlsx"
# df = pd.read_excel(file_location, sheet_name="Sheet1")
# print(df)
#
# import csv
# with open("path_to_csv.csv", "r") as read_csv:
#     csv.reader(read_csv)
#
# if __name__ == '__main__':
#     calea_curenta_de_pe_disc = os.getcwd()
#     calea_catre_fisierul_json = Path(calea_curenta_de_pe_disc, "test.json")
#     print(citeste_din_fisier_json(calea_catre_fisierul_json))
#
# from pprint import pprint

print("---------------------------")