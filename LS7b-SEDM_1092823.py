#Introducción a la programación, sección 17
#Fecha de creación del programa: 19/09/2023
#Autor: Sofia Diéguez 
#Objetivo: Crear un programa que pueda realizar operaciones aritméticas.
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

while True:
    print("\nSeleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Cociente")
    print("6. Exponenciación")
    print("7. Salir")

    opcion = input("Ingrese el número de la operación que desea realizar (1-7): ")

    if opcion == '7':
        print("¡Hasta luego!")
        break

    if opcion not in ('1', '2', '3', '4', '5', '6'):
        print("Opción inválida. Por favor, elija una opción válida.")
        continue

    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))

    if opcion == '1':
        resultado = numero1 + numero2
        operacion = '+'
    elif opcion == '2':
        resultado = numero1 - numero2
        operacion = '-'
    elif opcion == '3':
        resultado = numero1 * numero2
        operacion = '*'
    elif opcion == '4':
        if numero2 == 0:
            resultado = "No es posible dividir por cero"
        else:
            resultado = numero1 / numero2
        operacion = '/'
    elif opcion == '5':
        if numero2 == 0:
            resultado = "No es posible dividir por cero"
        else:
            resultado = numero1 // numero2
        operacion = '//'
    elif opcion == '6':
        resultado = numero1 ** numero2
        operacion = "**"

    print(f"(numero1) (operacion) (numero2) = (resultado)")
