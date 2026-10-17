''' Calcular el total a pagar por la compra de zapatillas. Si se compran tres  o más zapatillas 
# se aplica un descuento del 20% sobre el total de la compra  y si son menos de tres zapatillas un
# descuento del 10%. Mostrar en pantalla, el valor de la compra, el valor del descuento y el 
# valor a pagar una vez aplicado el descuento'''

Cantidad= int (input("Ingrese la cantidad de zapatillas a comprar:"))
Precio= float (input("Ingrese el valor de las zapatillas:"))

Total= Cantidad * Precio

if Cantidad >= 3:
    Descuento= Total * 0.20
else:
    Descuento= Total * 0.10

Pagar= Total - Descuento

print("El valor de la compra es:",Total)
print("El valor del descuento es:",Descuento)
print("El valor a pagar es:",Pagar)