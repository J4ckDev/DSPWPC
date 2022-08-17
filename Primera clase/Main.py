#!/usr/bin/python3

class Auto:
    # Constructor de la clase
	def __init__(self, color, aceleracion):
		self.color = color # Encapsulacion tipo: public
		self.__kilometraje = 0 # Encapsulacion tipo: private
		self.aceleracion = aceleracion # Encapsulacion tipo: public
		self.velocidad = 0 # Encapsulacion tipo: public

    # Secciçón de los métodos de la clase
	def acelera(self, vel):
		self.velocidad = vel + self.aceleracion

	def frena(self):
		v = self.velocidad - self.aceleracion
		if v < 0:
			v = 0
		self.velocidad = v

	def get_kilometraje(self):
		return self.__kilometraje

autito = Auto("Rojo", 100) # Instancia de la clase Auto en la variable autito
print(autito.color) # Imprimir por consola
print(autito.get_kilometraje())

lista = list() # Lista vacío. Tambien se puede instanciar como lista = []

lista = [1, 2, 3, 4, 5, 6, 7 ,8]

persona = dict() # Diccionario vacío. También se puede instanciar como persona = {}

persona = {"Nombre": "Pepe",
		"Edad": 19,
		"Genero": 'M',
		"DNI": 6253536267263} # diccionario con datos

print(persona["Edad"]) # Acceder a un elemento del diccionario
print(lista[2]) # Acceder a un elemento de la lista