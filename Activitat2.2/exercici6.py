#8
preus = {'motxilla': 45, 'llapis': 1, 'calculadora': 25}

preusCars = {clau: preu for clau, preu in preus.items() if preu > 20}
print(preusCars)
