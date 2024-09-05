//Revisar calificaciones de estudiante


def simulador_calf():
    print('El total de todas las actividades equivale al 70% de la calificación final')
    print('El examen equivale al 30% de la calificación final')
    return simulador_calf

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
    print("Seleccione una opción:")
    print("1. Ver simulador de calificaciones")
    print("2. Calcular nota final")
    
    opcion = input("Ingrese el número de su elección: ")

    if opcion == '1':
        return simulador_calf()
    elif opcion == '2':
        return notas()
    else:
        print("Opción no válida. Intente de nuevo.")
        
menu()
