#Introducción a la programación, sección 17
#Fecha de creación del programa: 12/09/2023
#Autor: Sofia Diéguez 
#Objetivo: Crear un programa que se pueda utilizar para la recoleción de datos.
#Entrada: Ingresar un dato númerico
"""
Procesos principales
1. Solicitarle al usuario un número entero
2. Reconocer si es el número entero es positivo, negativo o cero
3. Mostrar el resultado
"""

from ast import If

print("Programa para determinar si un número entero es positivo, negativo o cero")
#Salida
print("Ejercicio 1")

#Solicitar datos
print("Ingrese un valor numérico entero")
try:
    numero = float(input("Ingresa un número: "))
    
    if numero > 0:
        print("El número es positivo.")
    elif numero < 0:
        print("El número es negativo.")
    else:
        print("El número es cero.")
except ValueError:
    print("Error: Debes ingresar un valor numérico válido.")