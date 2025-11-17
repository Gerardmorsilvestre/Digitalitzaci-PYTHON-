#1
capital_pais = {
    "Espanya": "Madrid",
    "França": "París",
    "Itàlia": "Roma",
}
print("Capital d'Espanya és:", capital_pais["Espanya"])
print("Capital d'Espanya és:", capital_pais["França"])
print("Capital d'Espanya és:", capital_pais["Itàlia"])
#2
a = input("Introdueix el nom d'un país: ")
if a in capital_pais:
    print("La capital de", a, "és:", capital_pais[a])
else:
    print("No tinc informació sobre aquest país.")
