'''Leer 20 números e imprimir cuantos son  positivos,
 cuantos negativos y cuantos neutros. '''
 
positivo = 0
negativo = 0 
neutro = 0
y= 0
while y <20:
 num =   int(input(" ingrese numeros positivos, negativos o neutros:" ))
 if num >0:
    positivo += 1
 elif num <0:
    negativo += 1
 else:
    neutro += 1
 y += 1

print (" mostrar  todo los numeros positivos: ",positivo)
print (" mostrar  todo los numeros negativos:  ", negativo)   
print (" mostrar  todo los numeros neutros:  ",neutro) 
