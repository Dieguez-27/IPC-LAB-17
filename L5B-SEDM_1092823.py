#Introducción a la programación, sección 17
#Fecha de creación del programa: 12/09/2023
#Autor: Sofia Diéguez 
#Objetivo: Crear un programa que pueda mostrar el día al momento de solo ingresar un número.
#Entrada: Ingresar un dato númerico
"""
Procesos principales
1. Solicitarle al usuario un número del 1 al 7
2. Reconocer el número al día que le corresponde
3. Mostrar el resultado
"""
print("Programa para determinar que día de la semana es utilizando números")
#Salida
print("Ejercicio 2")

#Solicitar datos
print("Ingrese un valor numérico entero")

# Pedir al usuario que ingrese un número del 1 al 7
numero = int(input("Ingresa un número del 1 al 7: "))

# Definir una lista con los nombres de los días de la semana
dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

# Verificar si el número está en el rango válido (1-7)
if 1 <= numero <= 7:
    # Obtener el nombre del día de la lista usando el índice
    dia = dias_semana[numero - 1]
    print(f"El día correspondiente al número {numero} es {dia}.")
else:
    print("Número fuera de rango. Debe ser un número del 1 al 7.")
