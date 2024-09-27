//Revisar calificaciones de estudiante


def simulador_calf():
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
    actividades = []
    
    for i in range(1, 5):
        calificacion = float(input(f'Ingrese su calificación de la actividad {i}: '))
        actividades.append(calificacion)  

    exam = float(input('Ingrese su calificación en el examen: '))

    promedio_actividades = sum(actividades) / len(actividades)
    
    actividades_final = 0.70 * promedio_actividades
    examen_final = 0.30 * exam

    nota_final = actividades_final + examen_final
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

        else:
            print("Opción no válida. Intente de nuevo.")

menu()
