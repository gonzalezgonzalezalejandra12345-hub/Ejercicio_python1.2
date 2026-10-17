'''Escribir un programa que multiplique los 20 primeros números naturales. Ejemplo: (1*2*3*4*5…). '''

producto_total = 1
for numero in range (1,21):
    producto_total *= numero
print(f"el producto de los 10 primeros {producto_total}")
    