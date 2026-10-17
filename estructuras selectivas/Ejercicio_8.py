'''Tomando como base los resultados obtenidos en un laboratorio de análisis clínicos, 
un médico determina si una persona tiene anemia o no, lo cual depende de su nivel de hemoglobina 
en la sangre, de su edad y de su sexo. Si el nivel de hemoglobina que tiene una persona es menor que el rango que le corresponde, 
se determina su resultado como positivo y en caso contrario como negativo.
 La tabla en la que el médico se basa para obtener el resultado es la siguiente:'''

edad = float (input(" ingrese la edad  de una persona: "))
hemoglobina = float (input(" ingrese el nivel de hemoglobina: "))
sexo = input ("ingrese el sexo: ")

if edad <= 1/12:
    minimo = 13
elif edad <= 0.5:
    minimo = 10
elif edad <= 1:
    minimo = 11
elif edad <= 5:
    minimo = 11.5
elif edad <= 10:
    minimo = 12.6
elif edad <= 15:
    minimo = 13
elif sexo == "femenino":
    minimo = 12
elif sexo == "masculino":
    minimo = 14
else:
    minimo = None

if minimo is None:
    print("Sexo no válido.")
elif hemoglobina < minimo:
    print("Resultado positivo: posible anemia")
else:
    print("Resultado negativo: no presenta anemia según el criterio indicado")

