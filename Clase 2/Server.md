# Servidor
El código enseña como construir un servidor simple para comprender lo visto en la clase 2. 

```python
#!/usr/bin/python3

import socket

# Función que gestionará la conexión de los clientes
def connection():
	conn, addr = s.accept() # Aceptar las conexiones 
	print(addr) # Mostrar en consola la IP y el puerto de origen o del cliente
	conn.send("Gracias por conectarte\n".encode()) # Enviar un mensaje al cliente, se debe codificar en bytes
	conn.close() # Cerrar la conexión del cliente

s = socket.socket() # Crear el socket TCP

port = 7676 # Puerto de escucha para el servidor

ip_address = '127.0.0.1' # IP del servidor

s.bind((ip_address, port)) # Vincular la dirección IP y el puerto

max_clients = 5 # Definir la cola máxima de clientes a atender

s.listen(max_clients) # Esperar la conexión de clientes

while True:
	connection()
	break # Romper el ciclo cuando el servidor atiende un cliente, si se quita o comenta el break, el servidor escuchará por siempre a no ser que se termine el proceso con un gestor de procesos como htop o presionando en el terminal la combinación de teclas Ctrl + letra C

s.close() # Apagar el servidor
```

Para ejecutar este código, copie y guarde en un archivo con extensión `.py`, luego en un terminal diríjase a la ubicación del archivo y ejecute el comando `python3 archivo.py`. Por ejemplo si lo llama como `server.py`, en el terminal ejecutará el comando `python3 server.py`.

___

[:arrow_backward: Regresar al inicio](../README.md)