list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]
a = input("Dona'm un numero i et dire si esta en la llista o no!: ")
num = int(a)
if num in list_num:
        print(f"{num} està en la llista")
else:
        print(f"{num} no esta en la llista")
        print("Torna a reinicar el programa i posar un altre numero")
        