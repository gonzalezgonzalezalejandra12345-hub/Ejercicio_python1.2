'''Se ha establecido un programa para estimular a los alumnos, el cual consiste en lo siguiente:
 si el promedio obtenido por un alumno en el último
 periodo es mayor o igual que 4.0, se le hará un descuento del 30% sobre la pensión; si el promedio obtenido
 es menor que 4.0 deberá pagar la pensión completa, la cual incluye el 10% de IVA. Obtener cuanto debe pagar un alumno. '''

promedio = float (input(" pormedio de las notas: "))

pension= float (input(" ingrese el valor de la pension:  "))

if promedio >= 4.0:
    descuento * 0.30
    pagar = promedio - descuento 
else:
    iva =  pension * 0.10
    pagar = pension + iva

print ("El promedio del alumno es:", promedio)
print ("El Valor de la pension es: $ ",pension )

if promedio >=4.0:
    print("Descuento de 30%: $  ",descuento)
else:
    print("Iva del 10%:  $",iva)


print ("Total que debe pagar:  $",pagar)



