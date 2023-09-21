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
import math

while True:
    print("Menú de Operaciones:")
    print("1. a * b + c")
    print("2. a * (b + c)")
    print("3. a / b * c")
    print("4. 3a + 2b / c^2")
    print("5. Calcular la fórmula cuadrática")
    print("6. Salir")
    
    opcion = input("Seleccione una opción (1/2/3/4/5/6): ")
    
    if opcion == '1':
        a = float(input("Ingrese el valor de a: "))
        b = float(input("Ingrese el valor de b: "))
        c = float(input("Ingrese el valor de c: "))
        resultado = a * b + c
        print(f"Resultado de a * b + c: {resultado}")
    elif opcion == '2':
        a = float(input("Ingrese el valor de a: "))
        b = float(input("Ingrese el valor de b: "))
        c = float(input("Ingrese el valor de c: "))
        resultado = a * (b + c)
        print(f"Resultado de a * (b + c): {resultado}")
    elif opcion == '3':
        a = float(input("Ingrese el valor de a: "))
        b = float(input("Ingrese el valor de b: "))
        c = float(input("Ingrese el valor de c: "))
        resultado = (a / b) * c
        print(f"Resultado de a / b * c: {resultado}")
    elif opcion == '4':
        a = float(input("Ingrese el valor de a: "))
        b = float(input("Ingrese el valor de b: "))
        c = float(input("Ingrese el valor de c: "))
        resultado = 3 * a + 2 * b / (c ** 2)
        print(f"Resultado de 3a + 2b / c^2: {resultado}")
    elif opcion == '5':
        a = float(input("Ingrese el valor de a: "))
        b = float(input("Ingrese el valor de b: "))
        c = float(input("Ingrese el valor de c: "))
        
        discriminante = b ** 2 - 4 * a * c
        
        if a != 0 and discriminante >= 0:
            x1 = (-b + math.sqrt(discriminante)) / (2 * a)
            x2 = (-b - math.sqrt(discriminante)) / (2 * a)
            print(f"Soluciones de la fórmula cuadrática: x1 = {x1}, x2 = {x2}")
        else:
            print("Error: a debe ser distinto de 0 y b^2 - 4ac debe ser mayor o igual a 0.")
    elif opcion == '6':
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida (1/2/3/4/5/6).")
        