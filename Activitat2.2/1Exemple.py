# Crear un diccionari amb clau-valor
alumne = {
    "nom": "Maria",
    "edat": 21,
    "curs": "Bioinformàtica"
}
# Accedir a un valor pel seu nom de clau
print(alumne["nom"])# Sortida: Maria
print(alumne["edat"])# Sortida: 21

alumne["edat"] = 22# Canviar l'edat de 21 a 22
print(alumne["edat"])# Sortida: 22

alumne["nota"] = 9.5
# Eliminar una clau-valor
del alumne["curs"]

print(alumne)
# Sortida: {'nom': 'Maria', 'edat': 22, 'nota': 9.5}

for clau, valor in alumne.items():
    print(f"{clau}: {valor}")
# Sortida:
# nom: Maria
# edat: 22
# nota: 9.5

if "edat" in alumne:
    print("La clau 'edat' existeix en el diccionari.")

# Si la clau 'nom' existeix, retorna el seu valor; sinó, retorna "Desconegut"
nom = alumne.get("nom", "Desconegut")
print(nom)  # Sortida: Maria
