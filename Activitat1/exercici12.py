text = "Hello World"
text2 = "Hola mon!!!"

coincidencies = 0
for i in range(min(len(text), len(text2))):
    if text[i] == text2[i]:
        coincidencies += 1

print(f"Nombre de coincidències: {coincidencies}")
