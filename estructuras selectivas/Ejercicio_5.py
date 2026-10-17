'''Calcular el número de pulsaciones que debe tener una persona por cada 10 segundos de ejercicio aeróbico;
 la fórmula que se aplica es:  cuando el sexo es femenino : núm. pulsaciones
  = (220 - edad)/10  y si el sexo es masculino : núm. pulsaciones = (210 - edad)/10 '''

Sexo = input (" ingrese el sexo: ")
edad= int (input ("ingrese la edad: "))

if Sexo == "femenino":
    pulsaciones =(220- edad) / 10
elif Sexo == "masculino":
    pulsaciones =(210 - edad)/ 10
else:
    pulsaciones = 0
print (" Las pulsaciones  calculadas por cada 10 segundos son:", pulsaciones )

