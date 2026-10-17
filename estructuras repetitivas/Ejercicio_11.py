'''Pedir los datos de los alumnos, estos son: sexo, edad y altura. Al final del programa se deberá mostrar la cantidad de hombres,
 la cantidad de mujeres, la altura promedio ,la cantidad de alumnos que tienen una altura mayor a 1.70 cm, 
 la cantidad de alumnos que tiene una altura  menor o igual a 1.50 cm. El programa debe finalizar cuando la edad sea igual a 0. '''

hombres = 0
mujeres = 0
total = 0
suma_alturas = 0
mayor_170 = 0
menor_igual_150 = 0
registrado = False

opcion = 0
while opcion != 3:
    print("\n===== MENÚ =====")
    print("1. Registrar alumnos")
    print("2. Ver resultados")
    print("3. Salir")
    opcion = int(input("Elija una opción: "))

    if opcion == 1:
        hombres = 0
        mujeres = 0
        total = 0
        suma_alturas = 0
        mayor_170 = 0
        menor_igual_150 = 0

        print("\n(Digite edad 0 para terminar el registro)")
        while True:
            edad = int(input("\nEdad: "))
            if edad == 0:
                break
            if edad < 0:
                print("Edad no válida.")
                continue

            sexo = input("Sexo (H o M): ").upper()
            if sexo != "H" and sexo != "M":
                print("Sexo no válido, digite H o M. Vuelva a ingresar el alumno.")
                continue

            altura = float(input("Altura en metros (ejemplo 1.65): "))
            if altura <= 0:
                print("Altura no válida. Vuelva a ingresar el alumno.")
                continue

            if sexo == "H":
                hombres += 1
            else:
                mujeres += 1

            total += 1
            suma_alturas += altura

            if altura > 1.70:
                mayor_170 += 1
            if altura <= 1.50:
                menor_igual_150 += 1

        registrado = True
        print("\nRegistro finalizado.")

    elif opcion == 2:
        if not registrado:
            print("\nPrimero debe registrar los alumnos (opción 1).")
        elif total == 0:
            print("\nNo se registró ningún alumno.")
        else:
            print("\nTotal de alumnos:", total)
            print("Cantidad de hombres:", hombres)
            print("Cantidad de mujeres:", mujeres)
            print("Altura promedio:", round(suma_alturas / total, 2), "m")
            print("Alumnos con altura mayor a 1.70:", mayor_170)
            print("Alumnos con altura menor o igual a 1.50:", menor_igual_150)

    elif opcion == 3:
        print("\nPrograma finalizado.")

    else:
        print("\nOpción no válida.")