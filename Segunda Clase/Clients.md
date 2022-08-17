# Clientes
Código de los clientes realizados en la clase 2 para la conexión de sockets. Es importante que el servidor esté corriendo para realizar la prueba de conexión con cualquiera de los clientes o que Metasploitable2 esté corriendo.

## Cliente con librería Socket

```python
#!/usr/bin/python3

import socket

s = socket.socket() # Crear el socket TCP

port_server = 7676 # Puerto de escucha del servidor

ip_server = "127.0.0.1" # Dirección IP del servidor

s.connect((ip_server, port_server)) # Iniciar la conexión con el servidor

print(s.recv(1024).decode('UTF-8')) # Decodificar la respuesta en Bytes a UTF-8.

s.close() # Cerrar la conexión
```

## Cliente con librería PWN

```python
#!/usr/bin/python3

from pwn import *

conexion = remote("127.0.0.1", 7676) # Conectarse al servidor remoto
print(conexion.recvline().decode('UTF-8')) # Leer la primera línea de respuesta retornada por el servidor

```

Para ejecutar cualquiera de los códigos, copie y guarde en un archivo con extensión `.py`, luego en un terminal diríjase a la ubicación del archivo y ejecute el comando `python3 archivo.py`. Por ejemplo si lo llama como `client.py`, en el terminal ejecutará el comando `python3 client.py`.

___

[:arrow_backward: Regresar al inicio](../README.md)