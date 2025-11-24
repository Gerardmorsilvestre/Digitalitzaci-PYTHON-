#9
alumnes = {
    'Marta': {'edat': 18, 'nota_final': 8.5},
    'Joan': {'edat': 19, 'nota_final': 6.7}
}
alumenmillornota = {nom: info for nom, info in alumnes.items() if info['nota_final'] > 7}
print(alumenmillornota)