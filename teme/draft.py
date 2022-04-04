# variabile

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