"""
Simulador de calificaciones
El programa permite ingresar las calificaciones de varias actividades y un examen final para varios estudiantes, 
y calcula su nota final ponderada. Las actividades equivalen al 70% y el examen al 30% de la calificacion total
"""

"""
================== Funcion de simulacion  =====================================
"""

def simulador_calf():
    """
    Explica al usuario la distribucion de la calificacion total:
    - Las actividades tienen un peso del 70%
    - El examen tiene un peso del 30%
    
    El usuario puede decidir si regresar al menu principal o salir del simulador
    """
    print('El total de todas las actividades equivale al 70% de la calificacion final')
    print('El examen equivale al 30% de la calificacion final')
    
    # Bucle para permitir al usuario regresar o salir
    while True:
        volver = input("¿Desea volver al menu principal? (s/n): ")
        if volver == 's':
            return  # Regresa al menu principal
        elif volver == 'n':
            print("Saliendo del simulador.")
            break  # Sale del programa
        else:
            print("Opcion no valida, por favor ingrese 's' para si o 'n' para no.")

"""
================== Funcion para calcular las notas  ===========================
"""

def calcular_notas(matriz_calificaciones):
    """
    Calcula las notas finales de cada estudiante en base a las calificaciones 
    de las actividades y el examen.

    Recibe:
    - matriz_calificaciones: Lista de listas, donde cada sublista contiene 
      las calificaciones de un estudiante (4 actividades y 1 examen)

    Para cada estudiante:
    - Calcula el promedio de las actividades.
    - Aplica los porcentajes (70% actividades, 30% examen)
    - Imprime la nota final de cada estudiante.
    """
    estudiante_num = 1  # Contador para identificar a los estudiantes
    
    for calificaciones in matriz_calificaciones:
        actividades = calificaciones[:4]  # Primeros 4 valores son las actividades
        examen = calificaciones[4]        # El ultimo valor es el examen

        # Calcula el promedio de las actividades
        promedio_actividades = sum(actividades) / len(actividades)
        
        # Aplica los porcentajes
        actividades_final = 0.70 * promedio_actividades
        examen_final = 0.30 * examen

        # Calcula la nota final
        nota_final = actividades_final + examen_final
        print('La nota final del estudiante ' + str(estudiante_num) + ' es: ' + str(nota_final))
        
        estudiante_num += 1  # Incrementa el numero del estudiante

"""
================== Funcion para ingresar calificaciones  ======================
"""

"""
================== Funcion para ingresar calificaciones con validacion  =======
"""

def ingresar_calificaciones():
    """
    Solicita al usuario que ingrese las calificaciones de los estudiantes 
    para 4 actividades y 1 examen, asegurándose de que estén entre 0 y 10. 
    La cantidad de estudiantes la decide el usuario.

    Devuelve:
    - Una matriz de calificaciones, donde cada fila es una lista de 
      calificaciones de un estudiante.
    """
    matriz_calificaciones = []  # Lista vacía para almacenar las calificaciones
    num_estudiantes = int(input('¿Cuántos estudiantes desea ingresar?: '))

    # Bucle para ingresar las calificaciones de cada estudiante
    for i in range(num_estudiantes):
        calificaciones = []  # Lista para almacenar las calificaciones de un estudiante
        print(f'Estudiante {i + 1}')

        # Ingreso de las 4 calificaciones de las actividades
        for j in range(1, 5):
            while True:
                calificacion = float(input(f'Ingrese su calificación de la actividad {j} (0-10): '))
                if 0 <= calificacion <= 10:
                    calificaciones.append(calificacion)
                    break
                else:
                    print("Calificación inválida. Debe estar entre 0 y 10.")

        # Ingreso de la calificación del examen
        while True:
            examen = float(input('Ingrese su calificación en el examen (0-10): '))
            if 0 <= examen <= 10:
                calificaciones.append(examen)
                break
            else:
                print("Calificación inválida. Debe estar entre 0 y 10.")
        
        # Agrega la lista de calificaciones del estudiante a la matriz
        matriz_calificaciones.append(calificaciones)

    return matriz_calificaciones  # Devuelve la matriz completa de calificaciones


"""
================== Funcion del menu principal  ================================
"""

def menu():
    """
    Muestra un menu interactivo al usuario con tres opciones:
    1. Explicar como funciona el simulador.
    2. Ingresar calificaciones y calcular las notas finales.
    3. Salir del programa.
    
    Dependiendo de la seleccion del usuario, ejecuta la funcion correspondiente.
    """
    while True:
        # Muestra el menu con las opciones
        print("Seleccione una opcion:")
        print("1. Ver como funciona el simulador")
        print("2. Ingresar calificaciones y calcular notas finales")
        print("3. Salir")

        opcion = input("Ingrese el numero de su eleccion: ")

        # Seleccion de opciones
        if opcion == '1':
            simulador_calf()  # Explicacion del simulador
            break
        elif opcion == '2':
            matriz_calificaciones = ingresar_calificaciones()  # Ingreso de calificaciones
            calcular_notas(matriz_calificaciones)  # Calculo de notas finales
        elif opcion == '3':
            print("Saliendo del programa...")
            break  # Sale del programa
        else:
            print("Opcion no valida. Intente de nuevo.")  # Manejo de errores

# Llamada a la funcion principal del menu
menu()
