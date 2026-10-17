'''#  dependiendo de un color  que se escoge al azar. Si el color de la balota es rojo  el descuento
#  es del 15% sobre el total de la compra, la balota es verde el descuento es del 20%. Si  el color
#  es diferente a los indicados no obtendrá descuento.  Imprimir el valor de la compra, el color
#  de la balota, el descuento y el valor a pagar.'''

compra= float (input("Ingrese el valor de la compra:"))
color= input("Ingrese el color de la balota (rojo/verde):")

if color == "rojo":
    descuento = compra * 0.15
elif color == "verde":
    descuento = compra * 0.20
else:
    descuento = 0

valor_a_pagar = compra - descuento

print("El valor de la compra es:", compra)
print("El color de la balota es:", color)
print("El descuento es:", descuento)
print("El valor a pagar es:", valor_a_pagar)