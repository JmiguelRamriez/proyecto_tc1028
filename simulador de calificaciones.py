//Revisar calificaciones de estudiante


print('El total de todas las actividades equivale al 70% de la calificacion final')
print('El examen equivale al 30% de la calificacion final')

def simulador_calf ():
    return () 

def notas ():   
    act1 = float(input('Ingrese su calificacion de la actividada 1: '))
    act2 = float(input('Ingrese su calificacion de la actividada 2: '))
    act3 = float(input('Ingrese su calificacion de la actividada 3: '))
    act4 = float(input('Ingrese su calificacion de la actividada 4: '))
    exam = float(input('Ingrese su calificaion en el examen: '))

    actividades = 0.70
    examen = 0.30

    actividades = (act1 + act2 + act3 + act4 )/4
    nota_final = actividades + examen
    print('la nota final es :', nota_final)
    return (nota_final)


notas ()
