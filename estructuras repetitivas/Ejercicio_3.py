'''Suponga que se tiene un conjunto de calificaciones de un grupo de 20 alumnos.
 Realizar un algoritmo para calcular el promedio  y la calificación más alta y  más baja de todo el grupo.'''  

sumaNotas = 0
notaMayor = 0
notaMenor = 0
for  b in range (20):
    nota= float (input(f" ingrese nota  del alumno {b + 1}:"))
    sumaNotas += nota
     
    if b == 0:
        notaMayor = nota
        notaMenor =nota
    
    elif nota > notaMayor:
        notaMayor = nota
    else:
     nota > notaMenor
    notaMenor = nota
       
promedio = sumaNotas /20
while True:
    print( "--- MENU DE  CALIFICACIONES ---")
    print("1. mostrar promedio")
    print("2. Mostrar nota mas alta")
    print("3. Mostra nota  baja")
    print("4. Mostrar todos los resultados")
    print("5. Salir")
    opcion = input ("Selecione una opcion:")

    if opcion == "1":
        print("Promedio:", promedio)

    elif opcion == "2":
        print("Nota mas alta:", notaMayor)

    elif opcion == "3":
        print("Nota mas baja:", notaMenor)

    elif opcion == "4":
        print("Promedio:", promedio)
        print("Nota mas alta:", notaMayor)
        print("Nota mas baja:", notaMenor)

    elif opcion == "5":
        print("Gracias por utilizar el programa")
        break

    else:
        print("Opcion invalida")