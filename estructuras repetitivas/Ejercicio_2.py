'''Leer 10 números negativos y convertirlos a positivos e imprimir la suma de dichos números.'''

suma = 0
for i in range(10):
    num = float(input("Ingrese un número negativo: "))
    if num < 0:
        num = -num
    suma += num
print("La suma de los números positivos es:", suma)