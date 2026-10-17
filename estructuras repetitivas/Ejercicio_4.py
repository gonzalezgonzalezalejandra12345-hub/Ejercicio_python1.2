'''Calcular e imprimir la tabla de multiplicar de un número cualquiera,
 el cual se digitará por teclado. Imprimir el multiplicando, el multiplicador y el producto. '''

numero = int (input(" ingrese un numero:  "))
for b in range (1, 11):
    multiplicado= numero
    multiplicador= b
    Resultado = multiplicado * multiplicador
    print (multiplicado, "x", multiplicador, "=" ,Resultado)
