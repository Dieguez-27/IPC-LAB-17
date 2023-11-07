#Introducción a la programación, sección 17
#Fecha de creación del programa: 07/11/2023
#Autor: Sofia Diéguez 
#Objetivo: Crear una clase que pueda mostrar los datos del vehículo
#Entrada: Clase de atributos y métodos
"""
Procesos principales
1. Solicitarle al usuario un
2. Realizar las operaciones aritméticas tomando en cuenta la jerarquía de operaciones.
3. Mostrar el resultado
"""
class Vehiculo:
    def __init__(self, modelo=0, precio=0.0, marca="", disponible=True, Tipocambio=7.94):
        self.modelo = modelo
        self.precio = precio
        self.marca = marca
        self.disponible = disponible
        self.Tipocambio = Tipocambio
        if self.disponible:
            return "Disponible"
        else:
            return "No se encuentra disponible actualmente"

    def MostrarInformacion(self):
        precioDolar= self.precio / self.Tipocambio
        return f"Marca: {self.marca}. Modelo: {self.modelo}. Precio de venta: Q{self.precio}. Precio en dólares: ${precioDolar}. {self.disponible()}"

    def AplicarDescuento(self, miDescuento):
        self.descuentoAplicado = miDescuento
        self.precio -= miDescuento
        self.DefinirPrecio(self.precio)
        
carro = Vehiculo()
carro.DefinirModelo(2019)
carro.DefinirPrecio(65000.0)
carro.DefinirMarca("Chevrolet")
carro.DefinirTipoCambio(7.0)
print(carro.MostrarInformacion())
carro.CambiarDisponibilidad()
print(carro.MostrarInformacion())
carro.AplicarDescuento(1000.0)
print(carro.MostrarInformacion())