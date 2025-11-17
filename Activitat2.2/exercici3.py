a = input("Dona'm una paraula:")
frequencia = {}

for paraula in a:
    frequencia[paraula] = frequencia.get(paraula, 0) + 1
print(frequencia)