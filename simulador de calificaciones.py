//Revisar calificaciones de estudiante


def simulador_calf():
    print('El total de todas las actividades equivale al 70% de la calificación final')
    print('El examen equivale al 30% de la calificación final')
    while True:
        volver = input("¿Desea volver al menú principal? (s/n): ")
        if volver == 's':
            return
        elif volver == 'n':
            print("Saliendo del simulador.")
            break
        else:
            print("Opción no válida, por favor ingrese 's' para sí o 'n' para no.")

def notas():
    act1 = float(input('Ingrese su calificación de la actividad 1: '))
    act2 = float(input('Ingrese su calificación de la actividad 2: '))
    act3 = float(input('Ingrese su calificación de la actividad 3: '))
    act4 = float(input('Ingrese su calificación de la actividad 4: '))
    exam = float(input('Ingrese su calificación en el examen: '))

    actividades = 0.70 * ((act1 + act2 + act3 + act4) / 4)
    examen = 0.30 * exam

    nota_final = actividades + examen
    print('La nota final es:', nota_final)
    return nota_final

def menu():
    while True:
        print("\nSeleccione una opción:")
        print("1. Ver como funciona el simulador")
        print("2. Calcular nota final")
        print("3. Salir")

        opcion = input("Ingrese el número de su elección: ")

        if opcion == '1':
            simulador_calf()
        elif opcion == '2':
            notas()
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu()
