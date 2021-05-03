import random 
suma = 0
for j in range (5):

    lista = []
    for i in range (10):
        lista.append (random.randint (0,100))
    print ('Se genero un lista de 0 a 100 de 10 numeros')
    respuesta = int(input ('¿Cual es el numero mayor de la lista?'))

    maximo_hasta_ahora = -1
    for n in lista:
        if (n>maximo_hasta_ahora):
            maximo_hasta_ahora = n
    if respuesta == maximo_hasta_ahora:
        print ('Acertaste!')
        puntaje = 100
    else:
        print ('No acertaste. El maximo era', maximo_hasta_ahora)
        dif=abs(maximo_hasta_ahora - respuesta) 
        #abs = valor absoluto
        puntaje = 100 - maximo_hasta_ahora - dif
        if (puntaje<0):
            puntaje = 0
    print ('Tu puntaje es', puntaje)
    suma = suma + puntaje

print ('Puntaje total', suma)


