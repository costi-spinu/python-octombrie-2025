# # class Masina:
# #     def __init__(self, marca, model):
# #         self.marca = marca      # atribut
# #         self.model = model      # atribut

# #     def porneste(self):         # metodă
# #         print(f"{self.marca} {self.model} pornește...")

# # # Creăm un obiect (instanță)
# # m1 = Masina("Dacia", "Logan")

# # # Accesăm atribute și metode
# # print(m1.marca)      # -> Dacia
# # m1.porneste()        # -> Dacia Logan pornește...


# # Clasa de bază
# class Masina:
#     def __init__(self, marca, model):
#         self.marca = marca
#         self.model = model

#     def porneste(self):
#         print(f"{self.marca} {self.model} pornește...")

#     def opreste(self):
#         print(f"{self.marca} {self.model} se oprește.")


# # Clasa derivată (moștenește din Masina)
# class MasinaElectrica(Masina):


#     def __init__(self, marca, model, baterie):
#         # apelăm constructorul din clasa părinte
#         super().__init__(marca, model)
#         self.baterie = baterie

#     def incarca(self):
#         print(f"{self.marca} {self.model} se încarcă (baterie: {self.baterie} kWh).")

#     # putem și suprascrie metode
#     def porneste(self):
#         print(f"{self.marca} {self.model} pornește silențios — e electrică!")


# # Folosim clasele
# m1 = Masina("Dacia", "Logan")
# m1.porneste()
# m1.opreste()

# m2 = MasinaElectrica("Tesla", "Model 3", 75)
# m2.porneste()
# m2.incarca()

# github
