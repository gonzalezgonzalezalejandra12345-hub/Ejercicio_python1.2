'''Calcular la cantidad de hombres y mujeres presentes 
en un salón de clases con un total de n personas. '''

hombres = 0
mujeres = 0
total = 0
registrado = False

opcion = 0
while opcion != 3:
    print("===== MENÚ =====")
    print("1. Registrar personas del salón")
    print("2. Ver cantidad de hombres y mujeres")
    print("3. Salir")
    opcion = int(input("Elija una opción: "))

    if opcion == 1:
        hombres = 0
        mujeres = 0
        total = int(input("Total de personas en el salón (n): "))

        i = 1
        while i <= total:
            sexo = input("Persona {} - Digite H (hombre) o M (mujer): ")
            if sexo == "H":
                hombres += 1
                i += 1
            elif sexo == "M":
                mujeres += 1
                i += 1
            else:
                print("Dato no válido, digite H o M.")
                continue

        registrado = True
        print("Registro finalizado.")

    elif opcion == 2:
        if not registrado:
            print("Primero debe registrar las personas (opción 1).")
        else:
            print("Total de personas:", total)
            print("Hombres:", hombres)
            print("Mujeres:", mujeres)

    elif opcion == 3:
        print("Programa finalizado.")

    else:
        print("Opción no válida.")
        