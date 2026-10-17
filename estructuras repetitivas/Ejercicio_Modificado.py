'''Suponga que se tiene un conjunto de calificaciones de un grupo de 20 alumnos. 
Realizar un algoritmo para calcular el promedio 
 y la calificación más alta y  más baja de todo el grupo.  '''

# Inicializamos las variables
sumaNotas = 0
notaMayor = 0
notaMenor = 0
aprobados = 0
reprobados = 0
notas = []

# Pedimos las notas de los 20 alumnos
for b in range(20):
    nota = float(input(f"Ingrese la nota del alumno {b + 1}: "))

    # MODIFICACION 1: Validamos que la nota este entre 0 y 5
    while nota < 0 or nota > 5:
        print("La nota debe estar entre 0 y 5")
        nota = float(input("Ingrese la nota nuevamente: "))

    # MODIFICACION 2: Guardamos todas las notas en una lista
    notas.append(nota)

    # Sumamos las notas
    sumaNotas = sumaNotas + nota

    # La primera nota sera la mayor y la menor inicialmente
    if b == 0:
        notaMayor = nota
        notaMenor = nota

    else:
        # Buscamos la nota mas alta
        if nota > notaMayor:
            notaMayor = nota

        # MODIFICACION 3: Corregimos el calculo de la nota mas baja
        if nota < notaMenor:
            notaMenor = nota

    # MODIFICACION 4: Contamos aprobados y reprobados
    if nota >= 3:
        aprobados = aprobados + 1
    else:
        reprobados = reprobados + 1

# Calculamos el promedio
promedio = sumaNotas / 20

# Mostramos el menu
while True:
    print("\n--- MENU DE CALIFICACIONES ---")
    print("1. Mostrar promedio")
    print("2. Mostrar nota mas alta")
    print("3. Mostrar nota mas baja")
    print("4. Mostrar todos los resultados")
    print("5. Mostrar aprobados")
    print("6. Mostrar reprobados")
    print("7. Mostrar todas las notas")
    print("8. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        # MODIFICACION 5: Mostramos el promedio con dos decimales
        print("Promedio:", round(promedio, 2))

    elif opcion == "2":
        print("Nota mas alta:", notaMayor)

    elif opcion == "3":
        print("Nota mas baja:", notaMenor)

    elif opcion == "4":
        print("Promedio:", round(promedio, 2))
        print("Nota mas alta:", notaMayor)
        print("Nota mas baja:", notaMenor)
        print("Aprobados:", aprobados)
        print("Reprobados:", reprobados)

    elif opcion == "5":
        print("Cantidad de aprobados:", aprobados)

    elif opcion == "6":
        print("Cantidad de reprobados:", reprobados)

    elif opcion == "7":
        print("Notas ingresadas:", notas)

    elif opcion == "8":
        print("Gracias por utilizar el programa")
        break

    else:
        print("Opcion invalida")