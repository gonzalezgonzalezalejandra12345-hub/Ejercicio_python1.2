'''un grupo de 23 estudiantes presentan un examen de algoritmia. Hacer un algoritmo que lea por cada estudiante la calificación obtenida. 
Al finalizar calcule e imprima: • La cantidad de estudiantes que obtuvieron una calificación menor a 50.  
• La cantidad de estudiantes que obtuvieron una calificación de 50 o más pero menor que 70. 
• La cantidad de estudiantes que obtuvieron una calificación de 70 o más pero menor que 80. 
 • La cantidad de estudiantes que obtuvieron una calificación de 80 o más.
  La calificación obtenida en el examen de algoritmia debe ser entre 1 y 100. '''

TOTAL_ESTUDIANTES = 23

menor_50 = 0
de_50_a_69 = 0
de_70_a_79 = 0
de_80_o_mas = 0
registrado = False

opcion = 0
while opcion != 3:
    print("\n===== MENÚ =====")
    print("1. Registrar calificaciones")
    print("2. Ver cantidad de estudiantes por rango de calificación")
    print("3. Salir")
    opcion = int(input("Elija una opción: "))

    if opcion == 1:
        menor_50 = de_50_a_69 = de_70_a_79 = de_80_o_mas = 0

        i = 1
        while i <= TOTAL_ESTUDIANTES:
            print("\nEstudiante", i, "de", TOTAL_ESTUDIANTES)
            nota = float(input("Calificación (1 a 100): "))

            if nota < 1 or nota > 100:
                print("Calificación no válida, debe estar entre 1 y 100.")
                continue

            if nota < 50:
                menor_50 += 1
            elif nota < 70:
                de_50_a_69 += 1
            elif nota < 80:
                de_70_a_79 += 1
            else:
                de_80_o_mas += 1
            i += 1

        registrado = True
        print("\nRegistro finalizado.")

    elif opcion == 2:
        if not registrado:
            print("\nPrimero debe registrar las calificaciones (opción 1).")
        else:
            print("\nTotal de estudiantes:", TOTAL_ESTUDIANTES)
            print("Calificación menor a 50:", menor_50)
            print("Calificación de 50 o más, pero menor que 70:", de_50_a_69)
            print("Calificación de 70 o más, pero menor que 80:", de_70_a_79)
            print("Calificación de 80 o más:", de_80_o_mas)

    elif opcion == 3:
        print("\nPrograma finalizado.")

    else:
        print("\nOpción no válida.")