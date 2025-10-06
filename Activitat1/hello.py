print ("hello world")

a = 5 #Es un entero
b = 3.5 #Es un float
c = "Hola" #Es un string
d = True #Es un booleano
e = [1, 2, 3, 4, 5] #Es una lista
f = (1, 2, 3, 4, 5) #Es una tupla
g = { "nombre": "Juan", "edad": 30 } #Es un diccionario
h = {1, 2, 3, 4, 5} #Es un conjunto (set)
print(type(a)) #Tipo de dato
print(type(b)) 
print(type(c))
print(type(d)) 
print(type(e))
print(type(f))
print(type(g))
print(type(h))

int #Entero
float #Decimal
str #Cadena de texto
bool #Booleano
list #Lista
tuple #Tupla
dict #Diccionario
set #Conjunto
range #Rango
len #Longitud


s="hola"
print(s)
print(s[0]) #Primer caracter
print(s[1:3]) #Subcadena
print(s.upper()) #Mayusculas
print(s.lower()) #Minusculas
print(s.replace("h", "H")) #Reemplazar
print(len(s)) #Longitud
print(s.split("o")) #Dividir
print(s + " mundo") #Concatenar
print(s * 3) #Repetir
print("El valor de a és:", a) #Imprimir amb text
print(f"El valor de b és: {b}") #Imprimir amb f-string
print("a és major que b") if a > b else print("a no és major que b") #Condicional en una linia
print("a és igual a b") if a == b else print("a no és igual a b") #Condicional en una linia
print("a és menor que b") if a < b else print("a no és menor que b") #Condicional en una linia 
print("a és major o igual que b") if a >= b else print("a no és major o igual que b") #Condicional en una linia
print("a és menor o igual que b") if a <= b else print("a no és menor o igual que b") #Condicional en una linia
print("a és diferent de b") if a != b else print("a no és diferent de b") #Condicional en una linia
print(a + b) #Suma
print(a - b) #Resta
print(a * b) #Multiplicació
print(a / b) #Divisió
print(a // b) #Divisió entera
print(a % b) #Mòdul
print(a ** b) #Potència
print(a > b and d) #I lògic
print(a > b or d) #O lògic
print(not d) #No lògic
print(a in e) #Pertinença
print(a not in e) #No pertinença
print(isinstance(a, int)) #Tipus
print(isinstance(b, float)) #Tipus
print(isinstance(c, str)) #Tipus
print(isinstance(d, bool)) #Tipus
print(isinstance(e, list)) #Tipus
print(isinstance(f, tuple)) #Tipus
print(isinstance(g, dict)) #Tipus
print(isinstance(h, set)) #Tipus
print(id(a)) #ID de l'objecte
print(id(b)) #ID de l'objecte
print(id(c)) #ID de l'objecte
print(id(d)) #ID de l'objecte
print(id(e)) #ID de l'objecte
print(id(f)) #ID de l'objecte
print(id(g)) #ID de l'objecte
print(id(h)) #ID de l'objecte

a = input("Dona'm un numero: ")
b = input("Dona'm un altre numero: ")
a = int(a) #Convertir a enter
b = int(b) #Convertir a enter 
print("La suma és:", a + b)
print("La resta és:", a - b)  
print("La multiplicació és:", a * b)
print("La divisió és:", a / b)
print("La divisió entera és:", a // b)
print("El mòdul és:", a % b)
print("La potència és:", a ** b)

#Comentario d'una linia
"""
Comentari d'un bloc
de varies linies
"""
'''print("Aquest és un comentari dins d'una cadena de text")
print("Aquest codi s'executarà")
'''

if a > 0:
    print("a és positiu")
else:
    print("a és negatiu o zero")
for i in range(5):# De 0 a 4
    print(i)
while a > 0:
    print(a)
    a -= 1 #Decrementa a en 1
def suma(x, y):
    return x + y
print(suma(3, 5))
class Persona:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat
    def presentar(self):
        print(f"Hola, em dic {self.nom} i tinc {self.edat} anys.")
p = Persona("Anna", 25)
p.presentar()

import math
print(math.sqrt(16)) #Arrel quadrada de 16
import random
print(random.randint(1, 10)) #Nombre aleatori entre 1 i 10
import datetime
print(datetime.datetime.now()) #Data i hora actuals
import os
print(os.getcwd()) #Directori de treball actual
import sys
print(sys.version) #Versió de Python
import json
data = {'nom': 'Joan', 'edat': 28}
json_data = json.dumps(data) #Convertir a JSON
print(json_data)
parsed_data = json.loads(json_data) #Convertir de JSON
print(parsed_data)
print(parsed_data['nom'], parsed_data['edat'])
#Fi del programa
#Aquest és un comentari final