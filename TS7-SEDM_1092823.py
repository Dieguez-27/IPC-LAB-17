#Introducción a la programación, sección 17
#Fecha de creación del programa: 21/09/2023
#Autor: Sofia Diéguez 
#Objetivo: Crear un programa que pueda mostrar el día al momento de solo ingresar un número.
#Entrada: Ingresar un dato númerico
"""
Procesos principales
1. Solicitarle al usuario un número del 1 al 10
2. Asegurarse que el número ingresado este entre el rango requerido
3. Realizar la tabla de multiplicar del número seleccionado
4. Mostrar el resultado
"""
print("Programa de tabals de multiplicar")
#Salida
print("Ejercicio Semana 7")
# Muestra tu nombre completo
nombre_completo = "Sofia Elizabeth Diéguez Martínez"
print("Nombre completo:", nombre_completo)

while True:
    # Solicita al usuario ingresar un número en el rango de 1 a 10
    numero = int(input("Ingresa un número entre 1 y 10: "))
    
    # Verifica que el número esté en el rango correcto
    if 1 <= numero <= 10:
        # Utiliza un bucle for para mostrar la tabla de multiplicar
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero} X {i} = {resultado}")
        
        # Pregunta al usuario si desea generar la tabla de otro número
        respuesta = input("¿Deseas generar la tabla de otro número? (OUT para salir): ")
        if respuesta.upper() == "OUT":
            break
    else:
        print("El número ingresado no está en el rango de 1 a 10. Inténtalo de nuevo.")