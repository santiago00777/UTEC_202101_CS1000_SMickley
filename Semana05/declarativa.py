print("Ejercicio 1")
print("-"*40)
numeros = [1, 3, 5, 10]
#Programación Imperativa
suma = 0
for i in numeros:
    suma += i*2
print(suma)

#Programación declarativa
suma = sum(numero*2 for numero in numeros)
print(suma)

print()
print("Ejercicio 2")
print("-"*40)
nombres = ["JUAN", "KARLA", "MANUEL", "FIORELLA"]
nombres_minus = []
for nom in nombres:
    nom = nom.lower()
    nombres_minus.append(nom)
print(nombres_minus)

#Programación declarativa
nombres = ["JUAN", "KARLA", "MANUEL", "FIORELLA"]
nom_minus = [nombre.lower() for nombre in nombres]
print(nom_minus)

print()
print("Ejercicio 3")
print("-"*40)
# lee 5 números enteros
# desde teclado y almacénalos en una lista
lista = []
for i in range(5):
    n = int(input())
    lista.append(n)
print(lista)
print(lista)

#Programación declarativa
lista = [int(input("")) for i in range(5)]
print(lista)
print(lista)

print()
print("Ejercicio 4")
print("-"*40)
numeros = [1,2,3,4,5]
pares = []
for i in numeros:
    if i%2 == 0:
        pares.append(i)
print(pares)
#Programación declarativa
numeros = [1, 2, 3, 4, 5]
pares = []
pares = [i for i in numeros if i % 2 == 0]
print(pares)