#Introducción a la programación, sección 17
#Fecha de creación del programa: 19/09/2023
#Autor: Sofia Diéguez 
#Objetivo: Crear un programa que pueda realizar operaciones aritméticas utilizando jerarquía de operaciones.
#Entrada: Ingresar un dato númerico
"""
Procesos principales
1. Solicitarle al usuario un número entero
2. Realizar las operaciones aritméticas tomando en cuenta la jerarquía de operaciones.
3. Mostrar el resultado
"""
print("Programa para realizar operaciones aritmética utilizando jerarquía de operaciones")
#Salida
print("Ejercicio 3: Jerarquía de operaciones")

# Solicitar al usuario ingresar tres números (a, b y c)
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

# Realizar las operaciones y mostrar los resultados
resultado1 = a * b + c
resultado2 = a * (b + c)
resultado3 = (a / b) * c
resultado4 = 3 * a + 2 * b / (c ** 2)

# Mostrar los resultados en pantalla
print(f"Resultado de a * b + c: {resultado1}")
print(f"Resultado de a * (b + c): {resultado2}")
print(f"Resultado de a / b * c: {resultado3}")
print(f"Resultado de 3a + 2b / c^2: {resultado4}")
