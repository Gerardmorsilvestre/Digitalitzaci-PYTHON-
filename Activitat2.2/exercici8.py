#10
frase = "Hola mundo, esto es una frase de prueba"

palabras_espacios = frase.split()
print(palabras_espacios)

frequencia = {' '}
for paraula in frase:
    frequencia[paraula] = frequencia.get(paraula, 0)
    frequencia[paraula] += 1
print(frequencia)

