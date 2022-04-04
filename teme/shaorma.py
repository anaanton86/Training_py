class Shaorma:
    comanda = None
    tip = ["Lipie", "Farfurie", "In palma"]
    legume = True
    carne = ["pui", "vita"]
    bon = []

    def __init__(self, cerere_tip, cerere_carne):
        if cerere_tip in self.tip:
            self.comanda = cerere_tip
        else:
            print("du-te la vecinu")
        if cerere_carne in self.carne:
            self.carne = cerere_carne
        else:
            print("nu avem, tot la vecinu gasesti")

    def adauga_sos(self, sos):
        self.sos = sos

    def bonfiscal(self, bon):
        self.bon = bon


client1 = Shaorma("Lipie", "pui")
client2 = Shaorma("In palma", "vita")
client3 = Shaorma("Lipie", "curcan")
print(client1.comanda, client1.carne)
print(client2.comanda, client2.carne)
print(client3.comanda, client3.carne)
client1.adauga_sos("mustar")
print(client1.sos)
client1.suc = "fanta"
print(client1.suc)
print(client1.legume)
print(client1.bon)

client1.bonfiscal("pret1")
print(client1.bon)
client2.bonfiscal("pret2")
print(client2.bon)
# print(bon) ??
print(client1)