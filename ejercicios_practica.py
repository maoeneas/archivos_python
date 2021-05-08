#!/usr/bin/env python 
'''
Archivos [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.4

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''


__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.4"

import csv
import re

def ej1():
    print('Ejercicios con diccionarios')
    # Crear un diccionario vacio que luego completaremos
    # con el stock de elementos de ferreteris
    # el diccionario vacio debe llamarse "stock"
    
    # stock = ....
    stock={}
    

    # Luego de crear el diccionario completelo
    # con el siguiente stock:
    # tornillos = 100
    # tuercas = 150
    # arandelas = 300
    stock= {"tornillos":"100","tuercas":"150","arandelas":"300"}
    

    # Los nombres tornillos, tuercas y arandelas
    # son las claves (keys) del diccionario
    # mientras que las cantidades son los valores (values)

    # Una vez armado el diccionario imprimirlo en pantalla con print
    print(stock)


def ej2():
    print('Ejercicio con diccionarios')
    # Basado en el ejemplo anterior, deseamos tener un stock mes a mes
    # de los items tornillos, tuerca y arandelas.

    # Crear un diccionario por cada mes, cada diccionario se llamara "mes"
    # Cada uno que se genere debe tener los tres campos
    # tornillos, tuerca y arandelas y su respectivo stock

    # Cada diccionario deberá almacenarse en una lista llamada stock

    enero={"tornillos":100, "tuerca":100, "arandelas":100}
    febrero={"tornillos":100, "tuerca":100, "arandelas":100}
    marzo={"tornillos":100, "tuerca":100, "arandelas":100}
    
    stock_enero= [enero] 
    stock_febrero= [febrero]
    stock_marzo= [febrero]

    # Paso 1:
    # Generar un bucle de 3 iteraciones, solo generaremos el stock de
    # tres meses
    stock_agrupado=[]
    for i in (stock_enero):
        stock_final= stock_agrupado + [i]
        stock_final= stock_febrero+stock_marzo
    print(stock_final)

    # Paso 2:
    # En cada iteracion del bucle solicitar por consola cuando
    # stock se desea informar de cada uno de los 3 elementos

    # Paso 3:
    # Generar un diccionar llamado "mes" con los tres valores
    # de stock ingresados por consola

    # Paso 4:
    # Almacenar ese diccionario generado en una lista
    # llamada "stock"

    # Paso 5:
    # Repetir el proceso nuevamente en la siguiente
    # iteracion del bucle
    # Cuando finalice el bucle su lista debera contener los tres
    # diccionarios almacenados.

    # Paso 6:
    # Imprimir en pantalla el resultado, deberá verse como
    # el siguiente ejemplo:

    # [{'tornillos': 30, 'tuercas': 20, 'arandelas': 5}, 
    # {'tornillos': 100, 'tuercas': 50, 'arandelas': 15}, 
    # {'tornillos': 80, 'tuercas': 70, 'arandelas': 10}]

    # NOTA: Este ejercicio es exactamente lo mismo que armar
    # el edificio viste en clase, con los departamentos por piso
    # pero los valores para cada diccionario en cada mes
    # son ingresados por consola

def ej3():
    print('Ejercicio de archivos CSV')
    '''
    Realice un programa que abra el archivo 'stock.csv'
    y cuente el stock total de tornillos a lo largo
    de todo el archivo, sumando el stock en cada
    fila del archivo
    '''
    tornillos=[]
    with open('stock.csv') as archivo:
        lineas=archivo.read().splitlines()
        lineas.pop(0)
        for l in lineas:
            linea=l.split(",")
            tornillos.append(int(linea[1]))     
        resultado= sum(tornillos)
    print("es stock de tornillos es :" ,resultado)
    csv_file.close()


def ej4():
    print('Ejercicios con archivos CSV')
    
    '''
    Realice un programa que abra el archivo CSV "propiedades.csv"
    en modo lectura. Recorrar dicho archivo y contar
    la cantidad de departamentos de 2 ambientes y la cantidad
    de departamentos de 3 ambientes disponibles.
    Al finalizar el proceso, imprima en pantalla los resultados.
    '''
    ambientes_2=0
    ambientes_3=0
    # archivo = 'propiedades.csv'
    with open('propiedades.csv') as archivo:
        lineas=archivo.read().splitlines()
    lineas.pop(0)
    for l in lineas:
        linea=l.split(",")
        if (linea[-1])=="2":
            ambientes_2 +=1 
            
        elif (linea[-1])=="3":
            ambientes_3 +=1
            
    
    print("la cantidad de deptos de 2 ambientes es de: ",ambientes_2 )
    print("la cantidad de deptos de 3 ambientes es de: ",ambientes_3 )

        # # no me arroja el resultado!!!! fuck...

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    # ej1()
    # ej2()
    # ej3()
    ej4()
