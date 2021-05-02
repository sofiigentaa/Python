suma = 0
precio = int (input ('Indique el precio del producto o 0 para finalizar'))
while precio != 0:
    suma += precio
    print (f"Subtotal ${suma}")
    precio = int (input ('Indique el precio del producto o 0 para finalizar'))
if suma > 1000:
    descuento = suma * 10 / 100
else: 
    descuento = 0
pf = suma - descuento
print('El total es', suma , 'Descuento' , descuento , 'Precio final ' , pf)