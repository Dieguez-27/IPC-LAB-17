#Introducción a la programación, sección 17
#Fecha de creación del programa: 26/09/2023
#Autor: Sofia Diéguez 
#Objetivo: Crear un programa que pueda realizar cálculos factoriales y una frecuencia de Fibonacci.
#Entrada: Ingresar un dato númerico
"""
Procesos principales
1. Solicitarle al usuario un número entero
2. Realizar las operaciones aritméticas 
3. Mostrar el resultado
"""
print("Programa para realizar operaciones aritméticas")
print("Ejercicio Semana 8: Factorial y Secuencia de Fibonacci")

#Menú de opción en ciclo
opcion = ""
num=0
contador=1

def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)

def fibonacci(numero):
    if numero <= 0:
        return []
    elif numero == 1:
        return [0]
    elif numero == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, numero):
            next_fib = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_fib)
        return fib_sequence

while True:
    print("Menú:")
    print("1. Factorial")
    print("2. Secuencia de Fibonacci")
    print("3. Salir")

    opcion = int(input("Ingrese el número del menú que desea ejecutar: "))

    if opcion == 1:
        num = int(input("Ingrese un número para realizar el cálculo del factorial: "))
        solucion = factorial(num > 1)
        print(f"{num}! = {solucion * 1 * 2 * 3 * 4 * 5 * ... * (num-1) * num}")
    elif opcion == 2:
        num = int(input("Ingrese un número para ejecutar la secuencia de Fibonacci: "))
        contador = fibonacci(num)
        print(",".join(map(str, contador)), f"... Fibonacci ({num})")
    elif opcion == 3:
        print("Fin :)\n")
        break
    else:
        print("Error. Por favor, ingrese un caracter valido.")