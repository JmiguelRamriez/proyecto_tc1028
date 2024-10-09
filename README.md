# Protecto_tc1028
Contexto

Revisar calificaciones de estudiante

Este es un programa en Python que permite calcular la nota final de uno o varios estudiantes a partir de las calificaciones obtenidas en actividades y un examen final. Las actividades equivalen al 70% de la nota final y el examen al 30%. Con esto se podra especular sobre el promedio final. 


- Simulación: Dentro del programa hay una funcion llamada Simulador_caf() en la que se explica como funcina el programa. Explica cómo se calculan las notas en base a las actividades y el examen. 
- Ingreso de calificaciones:Dentro del programa hay una funcion ingresar_calificaciones(). Permite ingresar las calificaciones de varios estudiantes para calcular su nota final. 
- Cálculo automático:Dentro del programa hay una funcion llama calcular_notas(). El programa calcula la nota final ponderando las actividades y el examen.


============================ Subcompetencia 1 =====================================


Sub-Competencia: 1
	Componente: plantea una situación problema que le permite aplicar y demostrar sus conocimientos de programación.
Error original: No estaba bien planteado el algoritmo del programa 

Cambio realizado: Corregí el algoritmo.


============================ Subcompetencia 2 =====================================


Sub-Competencia: 2
  Componente: usa operadores aritméticos de manera eficaz.

Error original: La mayoria del codigo no esta bien estrocturado, y las operadores aritmeticos no estaban correctos.

    acticidad1 = act1;  //con esto asignamos variables para cada una de las actividades 
    acticidad2 = act2;
    acticidad3 = act3;
    acticidad4 = act4;
    acticidad5 = act5;
    print('El total de todas las actividades equivale al 70% de la calificacion final')
    print('El examen equivale al 30% de la calificacion final')
    
    nota_final = ((act1 + act2 + act3 + act4 + act5)/5);
    def simulador_calf ():
        return () 

    print ("ingrese la calificación que le gustaria tener: "), act1       //aqui se ingresa los datos que estan asignados a cada variable 
    print ("ingrese la calificación que le gustaria tener: "), act2
    print ("ingrese la calificación que le gustaria tener: "), act3
    print ("ingrese la calificación que le gustaria tener: "), act4
    print ("ingrese la calificación que le gustaria tener: "), act5
    def notas ():   
    act1 = float(input('Ingrese su calificacion de la actividada 1: '))
    act2 = float(input('Ingrese su calificacion de la actividada 2: '))
    act3 = float(input('Ingrese su calificacion de la actividada 3: '))
    act4 = float(input('Ingrese su calificacion de la actividada 4: '))
    exam = float(input('Ingrese su calificaion en el examen: '))

    print ("La nota que usted va a tener para el final del semestre es de: "), nota_final   //aqui podemos ver el posible resultado que queremos obtener para el final del semestre
    actividades = 0.70
    examen = 0.30

    actividades = (act1 + act2 + act3 + act4 )/4
    nota_final = actividades + examen
    print('la nota final es :', nota_final)
    return (nota_final)
    notas ()

Cambio realizado: Se corrigio la mayoria del codigo y utilice de manera correcta los operadores aritmeticos  

    def notas ():   
      act1 = float(input('Ingrese su calificacion de la actividada 1: '))
      act2 = float(input('Ingrese su calificacion de la actividada 2: '))
      act3 = float(input('Ingrese su calificacion de la actividada 3: '))
      act4 = float(input('Ingrese su calificacion de la actividada 4: '))
      exam = float(input('Ingrese su calificaion en el examen: '))
      
      actividades = 0.70 * ((act1 + act2 + act3 + act4) / 4)
      examen = 0.30 * exam
      
      print('la nota final es :', nota_final)
      return (nota_final)
    
Líneas de código donde se ve la corrección:
	3 - 19 aun no estaba definida la funcion. 
  9 - 17 se agrego tambien la funcion nota.


  ============================ Subcompetencia 3 =====================================


Sub-Competencia: 3
	componente: Separa el código en funciones pequeñas reusables, haciendo uso correcto de paso por parametros y return.

Error original: No se envio el avance 

Cambio realizado: Si se agrego las funciones para separa el codigo pero no se envio el avance, en el avance 4 ya sepuede ver que si esta divido en funciones 

Líneas de código donde se ve la corrección: 4 - 23 Se agrego funciones al codigo


============================ Subcompetencia 5 =====================================


Sub-Competencia: 
componente: usa la forma más a apropiada al problema para guardar los datos (listas, variable, archivos etc...) (avance 6 y avance 7)


Error original: En el github se me olvido borrar la primera linea del codigo anterior por lo que habian dos funciones lo cual probocaba error.

		def simulador_calf():
    def simulador_calf():

Cambio realizado: Se borro la funcion repetida 

    def simulador_calf():


Líneas de código donde se ve la corrección: 4 a 5


