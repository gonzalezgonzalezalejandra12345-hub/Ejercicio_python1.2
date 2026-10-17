''' Una persona debe realizar un muestreo con 50 personas para determinar el promedio de peso de los niños, jóvenes, 
adultos y ancianos  que existen en su zona. Las categorías se determinar de acuerdo a la siguiente tabla: '''

TOTAL_PERSONAS = 50

# Acumuladores de peso y contadores por categoría
suma_ninos = suma_jovenes = suma_adultos = suma_ancianos = 0
cont_ninos = cont_jovenes = cont_adultos = cont_ancianos = 0
muestreo_hecho = False

opcion = 0
while opcion != 3:
    print("===== MENÚ =====")
    print("1. Realizar muestreo")
    print("2. Ver promedios de peso")
    print("3. Salir")
    opcion = int(input("Elija una opción: "))

    if opcion == 1:
        # Se reinician los datos para empezar un muestreo nuevo
        suma_ninos = suma_jovenes = suma_adultos = suma_ancianos = 0
        cont_ninos = cont_jovenes = cont_adultos = cont_ancianos = 0

        for i in range(1, TOTAL_PERSONAS + 1):
            print(f"\nPersona {i} de {TOTAL_PERSONAS}")
            edad = int(input("Edad: "))
            peso = float(input("Peso (kg): "))

            if edad < 0 or peso <= 0:
                print("Datos no válidos, intente de nuevo.")
                continue

            if edad <= 12:
                suma_ninos += peso
                cont_ninos += 1
            elif edad <= 29:
                suma_jovenes += peso
                cont_jovenes += 1
            elif edad <= 59:
                suma_adultos += peso
                cont_adultos += 1
            else:
                suma_ancianos += peso
                cont_ancianos += 1

        muestreo_hecho = True
        print("Muestreo finalizado.")

    elif opcion == 2:
        if not muestreo_hecho:
            print("Primero debe realizar el muestreo (opción 1).")
        else:
            print("--- Promedio de peso por categoría ---")
            if cont_ninos > 0:
                print(f"Niños: {suma_ninos / cont_ninos:.2f} kg ({cont_ninos} personas)")
            else:
                print("Niños: sin datos")
            if cont_jovenes > 0:
                print(f"Jóvenes: {suma_jovenes / cont_jovenes:.2f} kg ({cont_jovenes} personas)")
            else:
                print("Jóvenes: sin datos")
            if cont_adultos > 0:
                print(f"Adultos: {suma_adultos / cont_adultos:.2f} kg ({cont_adultos} personas)")
            else:
                print("Adultos: sin datos")
            if cont_ancianos > 0:
                print(f"Ancianos: {suma_ancianos / cont_ancianos:.2f} kg ({cont_ancianos} personas)")
            else:
                print("Ancianos: sin datos")

    elif opcion == 3:
        print("Programa finalizado.")

    else:
        print("Opción no válida.")