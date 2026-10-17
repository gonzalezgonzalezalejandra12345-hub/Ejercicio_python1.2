'''La oficina de tránsito de Ibagué desea saber, de los n autos que entran a la ciudad de Ibagué,  
cuantos entran con calcomanía de cada color. Conociendo el ultimo dígito de la placa de cada carro, 
se puede determinar el color de la calcomanía utilizando la siguiente relación: '''

while True:
    print("\n===== MENU CARROS IBAGUE =====")
    print("1. Registrar vehículos")
    print("2. Mostrar resultados")
    print("3. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        amarillo = 0
        rosa = 0
        roja = 0
        verde = 0
        azul = 0

        N = int(input("Digite la cantidad de vehículos: "))

        for i in range(1, N + 1):
            digito = int(input("Digite el último dígito de la placa del vehículo "  ))

            while digito < 0 or digito > 9:
                print("Error. Digite un número entre 0 y 9.")
                digito = int(input("Digite nuevamente el último dígito: "))

            if digito == 1 or digito == 2:
                amarillo = amarillo + 1
            elif digito == 3 or digito == 4:
                rosa = rosa + 1
            elif digito == 5 or digito == 6:
                roja = roja + 1
            elif digito == 7 or digito == 8:
                verde = verde + 1
            elif digito == 0 or digito == 9:
                azul = azul + 1

        print("\nVehículos registrados correctamente.")

    elif opcion == 2:
        if 'amarillo' in locals():
            print("\n===== RESULTADOS =====")
            print("Amarillo:", amarillo)
            print("Rosa:", rosa)
            print("Rojo:", roja)
            print("Verde:", verde)
            print("Azul:", azul)
        else:
            print("Primero debe registrar los vehículos.")

    elif opcion == 3:
        print("Gracias por utilizar el programa.")
        break

    else:
        print("Opción no válida. Intente nuevamente.")