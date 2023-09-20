#Introducción a la programación, sección 17
#Fecha de creación del programa: 19/09/2023
#Autor: Sofia Diéguez 
#Objetivo: Crear un programa que pueda mostrar el día al momento de solo ingresar un número.
#Entrada: Ingresar un dato númerico
"""
Procesos principales
1. Solicitarle al usuario un número entero
2. Realizar las operaciones aritméticas 
3. Mostrar el resultado
"""
print("Programa para realizar operaciones aritméticas")
#Salida
print("Ejercicio 1: Operaciones Aritméticas")

# Solicitar al usuario que ingrese dos números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Realizar las operaciones
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

# Manejar la división por cero
if numero2 != 0:
    division = numero1 / numero2
    cociente = numero1 // numero2
else:
    division = "No es posible dividir por cero"
    cociente = "No es posible dividir por cero"

# Calcular la exponenciación
exponenciacion = numero1 ** numero2

# Mostrar los resultados en pantalla
print(f"{numero1} + {numero2} = {suma}")
print(f"{numero1} - {numero2} = {resta}")
print(f"{numero1} * {numero2} = {multiplicacion}")
print(f"{numero1} / {numero2} = {division}")
print(f"{numero1} // {numero2} = {cociente}")
print(f"{numero1} ** {numero2} = {exponenciacion}")
