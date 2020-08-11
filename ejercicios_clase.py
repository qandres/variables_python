#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.3"


def ej1():
    # Ejercicios de práctica numérica

    # Operadores con números decimales
    print('Ingrese el primer número decimal a operar:')
    numero_1 = float(input())

    print('Ingrese el segundo número decimal a operar:')
    numero_2 = float(input())

    suma = (numero_1 + numero_2)
    
    resta = (numero_1 - numero_2)

    division = (numero_1 / numero_2)

    multiplicacion = (numero_1 * numero_2)

    # Alumno: Imprima en pantalla los dos números decimales solicitados
    # print(....)

    # Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
    # numero_1, numero_2
    # Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
    # El resultado de sumar 4 y 2 es 6

    # Suma
     
    print ('El resultado de sumar', numero_1, 'y', numero_2, 'es', suma  )

    # Resta

    print ('El resultado de restar', numero_1, 'y', numero_2, 'es', resta  )

    # División

    print ('El resultado de dividir', numero_1, 'y', numero_2, 'es', division  )

    # Multiplicación

    print ('El resultado de multiplicar', numero_1, 'y', numero_2, 'es', multiplicacion  )

def ej2():
    # Ejemplos variables de texto

    # Ingrese primero su nombre y luego su apellido
    # Capture ambos datos e imprima su nombre completo

    print('Ingrese su nombre/s:')
    nombre = str(input())

    print('Ingrese su apellido/s:')
    apellido = str(input())

    nombre_completo = (nombre + apellido)

    # Imprima su nombre completo

    print (nombre, apellido)

    # Almacenar su nombre completo en una variable
    # nombre_completo = .....

    
    nombre_completo = (nombre + apellido)

    # Imprimir la cantidad de letras que posee su nombre completo

    print (len(nombre_completo))


def ej3():
    # Ejemplos variables de texto

    # Ingrese tres palabras y arme un acrónimo con ellas
    # Si desea puede modificar el código para ingresar más palabras
    print('Ingrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

    print('Ingrese palabra 3:')
    palabra_3 = str(input())

    # De cada palabra debe tomar la primera letra y armar el acrónimo

    subtext_1 = palabra_1[0]

    subtext_2 = palabra_2[0]

    subtext_3 = palabra_3[0]

    acronimo = (subtext_1 + subtext_2 + subtext_3)

    # Ejemplo: Alumbrado, barrido y limpieza --> ABL
    # Imprimir el resultado en pantalla

    print (acronimo)


def ej4():
    # Ejemplos variables de texto

    # Ingrese dos palabras y arme combinaciones con ella
    print('Ingrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())



    # De la primera palabra tome las primeras tres letras, utilice el operador 
    
    subtext_1 = palabra_1[0:3]

    # De la segunda palabra tome las últimas tres letras, utilice el operador :

    subtext_2 = palabra_2[-3:]

    # Formar una nueva palabra con los recortes solicitados
    # Imprima en pantalla los resultados
     
    nueva_palabra = (subtext_1 + subtext_2)

    print (nueva_palabra)

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    #ej2()
    #ej3()
    #ej4()
