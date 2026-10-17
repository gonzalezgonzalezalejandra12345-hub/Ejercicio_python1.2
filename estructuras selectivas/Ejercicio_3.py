'''Una empresa quiere hacer una compra de varias piezas de la misma clase a una fábrica de 
# bolsos. La empresa, dependiendo del monto total de la compra, decidirá qué hacer para 
# pagar al fabricante: 

# Si el monto total de la compra excede de $500 000 la empresa tendrá la capacidad de invertir
# de su propio dinero un 55% del monto de la compra, pedir prestado al banco un 30% y el resto 
# lo pagará solicitando un crédito al fabricante. 

# Si el monto total de la compra no excede de $500 000 la empresa tendrá capacidad de invertir
#  de su propio dinero un 70% y el restante 30% lo pagará solicitando crédito al fabricante.
#  El fabricante cobra por concepto de intereses un 20% sobre la cantidad que se le pague a crédito.

#Imprimir el valor invertido de su propio dinero, el valor prestado al banco, y el valor del crédito
#solicitado al fabricante, según sea el caso'''


Monto= float (input("Ingrese el monto total de la compra:"))
if Monto > 500000:
    Propio= Monto * 0.55
    Banco= Monto * 0.30
    Credito= Monto - (Propio + Banco)
    Intereses= 0

else:
    Propio= Monto * 0.70
    Banco= 0
    Credito= Monto * 0.30
    Intereses= Credito * 0.20

total_a_pagar= Credito + Intereses

print("El valor invertido de su propio dinero es:",Propio)
print("El valor prestado al banco es:",Banco)
print("El valor del crédito solicitado al fabricante es:",Credito)
print("Los intereses por el crédito son:",Intereses)
print("El valor total a pagar al fabricante es:",total_a_pagar)
