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

def calcular_notas(matriz_calificaciones):
    estudiante_num = 1  
    for calificaciones in matriz_calificaciones:
        actividades = calificaciones[:4]  
        examen = calificaciones[4]        

        promedio_actividades = sum(actividades) / len(actividades)
        
        actividades_final = 0.70 * promedio_actividades
        examen_final = 0.30 * examen

        nota_final = actividades_final + examen_final
        print('La nota final del estudiante ' + str(estudiante_num) + ' es: ' + str(nota_final))
        estudiante_num += 1  

def ingresar_calificaciones():
    matriz_calificaciones = []
    num_estudiantes = int(input('¿Cuántos estudiantes desea ingresar?: '))

    for i in range(num_estudiantes):
        calificaciones = []
        print('Estudiante: ',i+1)
        
        for j in range(1, 5):  
            calificacion = float(input('Ingrese su calificación de la actividad ' + str(j) + ': '))
            calificaciones.append(calificacion)

        examen = float(input('Ingrese su calificación en el examen: '))
        calificaciones.append(examen)  
        
        matriz_calificaciones.append(calificaciones)  

    return matriz_calificaciones

def menu():
    while True:
        print("\nSeleccione una opción:")
        print("1. Ver como funciona el simulador")
        print("2. Ingresar calificaciones y calcular notas finales")
        print("3. Salir")

        opcion = input("Ingrese el número de su elección: ")

        if opcion == '1':
            simulador_calf()
        elif opcion == '2':
            matriz_calificaciones = ingresar_calificaciones()  
            calcular_notas(matriz_calificaciones)  
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu()

