'''Calcular el promedio de edades de hombres, mujeres y de todo un grupo de alumnos.  '''

registrado = False

while True:
    print("\n===== MENU PROMEDIO DE EDADES =====")
    print("1. Ingresar edades de los alumnos")
    print("2. Mostrar promedios")
    print("3. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        sumaH = 0
        sumaM = 0
        contH = 0
        contM = 0

        N = int(input("Digite la cantidad de alumnos: "))

        while N <= 0:
            print("Error. Debe ingresar al menos un alumno.")
            N = int(input("Digite nuevamente la cantidad de alumnos: "))

        for i in range(1, N + 1):
            sexo = input("Digite el sexo del alumno "  )

            while sexo != "M" and sexo != "F":
                print("Error. Digite M o F.")
                sexo = input("Digite nuevamente el sexo (M/F): ")

            edad = int(input("Digite la edad del alumno " ))

            while edad <= 0:
                print("Error. La edad debe ser mayor que cero.")
                edad = int(input("Digite nuevamente la edad: "))

            if sexo == "M":
                sumaH = sumaH + edad
                contH = contH + 1
            else:
                sumaM = sumaM + edad
                contM = contM + 1

        promG = (sumaH + sumaM) / N

        if contH > 0:
            promH = sumaH / contH

        if contM > 0:
            promM = sumaM / contM

        registrado = True
        print("Edades registradas correctamente.")

    elif opcion == 2:
        if registrado == True:
            if contH > 0:
                print("Promedio de hombres:", promH)
            else:
                print("No hay hombres registrados.")

            if contM > 0:
                print("Promedio de mujeres:", promM)
            else:
                print("No hay mujeres registradas.")

            print("Promedio general:", promG)
        else:
            print("Primero debe ingresar las edades.")

    elif opcion == 3:
        print("Gracias por utilizar el programa.")
        break

    else:
        print("Opción no válida. Intente nuevamente.")