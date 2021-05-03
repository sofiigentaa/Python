#Generar una lista de 10 números al azar, de 0 a 100.
#Preguntarle al usuario cuál es el mayor número de la lista.
#Si el usuario acierta, se le otorgan 100 puntos.
#Si no acierta, se le otorgan (100 - la respuesta correcta - la diferencia a la respuesta correcta)
#En ningún caso el puntaje puede ser negativo.
#Repetir el juego 5 veces, e indicar cuántos puntos obtuvo al final.
#Ejemplos: - Si el máximo número era 90, y acierta; se otorgan 100 puntos. - Si dice que el máximo era 92, se le otorgan 100 - 90 - 2 = 8 puntos. - Si dice que el máximo era 60, se le otorgan 100 - 90 - 40 = -30 puntos. Pero como no puede ser negativo, se otorgan 0 puntos. - Si el máximo era 30 y el usuario responde 40, se le otorgan 100 - 30 - 40 = 30 puntos.
import random

lista = []

for i in range (20):
 lista.append (random.randint (0,100))
print (lista)

pares = []
impares = []

for numero in lista:
    if numero % 2 == 0: #es par
        pares.append (numero)
    else:
        impares.append (numero)
print ("Lista original")
print (lista)
print ("Lista pares")
print (pares)
print ("Lista impares")
print (impares)