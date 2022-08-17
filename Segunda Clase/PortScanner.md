# Escáner de puertos
El código de este script permite escanear los puertos de la dirección IP especificada y los guarda en un archivo para su posterior uso.

```python
#!/usr/bin/python3

import socket
import sys

# Pedir parámetros por línea de comandos
try:
	ip_server = sys.argv[1] # Direccion IP del servidor al cuál desea escanear los puertos
	nombre_archivo = sys.argv[2] # Nombre del archivo donde se guardarán los puertos que tiene abiertos el servidor
except:
	print("python3 port_scanner.py <ip-victima> <nombre-archivo>")
	print("\n<ip-victima> Direccion IP del servidor al cuál desea escanear los puertos")
	print("<nombre-archivo> Nombre del archivo donde se guardarán los puertos que tiene abiertos el servidor")
	sys.exit()

# Abre un archivo para agregar informacion, sino existe lo crea
file = open(nombre_archivo, "a")

# Información a escribir
salida = str()

# La cantidad de puertos totales a escanear van desde 0 a 65535
for port in range(1, 65536):
	try:
		s = socket.socket() # Crear el socket TCP

		s.connect((ip_server, port)) # Conectarse al socket, si no puede retorna una excepción que se captura por el try y la procesa el except, siguiendo con el siguiente puerto.

		salida += str(port) + "\n" # Si se onecta al socket, se guarda el puerto.

		s.close() # Se cierra la conexión.
	except:
		continue # Continuar con el siguiente puerto si no se puede conectar.

file.write(salida) # Escribir la información en el archivo
file.close() # Cerrar el archivo
```

___

[:arrow_backward: Regresar al inicio](../README.md)
