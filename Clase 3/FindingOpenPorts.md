# Encontrando puertos abiertos en metasploitable2
A fin de practicar los [tipos de escaneo](./ScanningTypes.md) con Nmap, se hará uso de metaspoitable2 como laboratorio de práctica. A continuación, a modo de bitácora se muestra lo desarrollado en la práctica:

1. Se inicializa el contenedor de metasploitable2 con el comando `docker start container-name`, nos conectamos al terminal del contenedor mediante el comando `docker exec -it container-name sh -c "/bin/services.sh && bash"` y ejecutamos el comando `ifconfig` o `ip a` para obtener su dirección IP, en mi caso fue **172.17.0.2**.
2. En otra pestaña del terminal se instala la librería [python-nmap](https://pypi.org/project/python-nmap/) con el comando `sudo pip3 install python-nmap`, la cuál hace uso del [API de Nmap](https://nmap.org/book/nse-api.html) para ejecutar los comandos que especifiquemos.
3. Con todo preparado, se realizó un [primer script](./scripts/BasicPortScanner.py) para obtener la información de los puertos. A continuación se explica linea a linea:
    ```python
    #!/usr/bin/python3

    import nmap # Importar la librería de nmap
    from pprint import PrettyPrinter # Importar lalibrería para impresión "bonita"

    nmap_port_scanner = nmap.PortScanner() # Instanciar el escaner de puertos

    ip_to_scan = '172.17.0.2' # IP del sistema objetivo, en este caso será metasploitable2

    ports_to_scan = '1-65535' # Se escanean los puertos desde el 1 hasta 65535.
    #ports_to_scan = '10, 20, 30, 44, 25' # Especificar un grupo de puertos a escanear.
    #ports_to_scan = '21' # Se escanea solo el puerto 21 que es donde comúnmente se encuentra el servicio FTP.

    aditional_parameters = "-sS" # Parámetros adicionales para tenerlos en cuenta al ejecutar el escaneo. En este caso se especifica el escaneo sigiloso.

    scan_result = nmap_port_scanner.scan(ip_to_scan, ports_to_scan, aditional_parameters) # Ejecutar el escaneo con los datos configurados anteriormente. Primero se pasa la ip, luego el puerto o puertos y después los parámetros adicionales.

    pretty_print = PrettyPrinter(depth=10) # Instanciar el objeto de configuración de impresión formateada e identada. Se configura a una profundidad de 10, si llegasemos a tener un diccionario con más de 10 niveles de profundidad, autómaticamente los siguientes niveles se reemplazan por tres puntos seguidos (...).
    pretty_print.pprint(scan_result) # Mostrar en consola de forma identada y ordenada el resultado del escaneo.
    ```
4. Por último se realiza un filtrado los puertos abiertos y se vuelven a escanear con los parámetros `-sV`, `-sC` y `-O`, los cuales permiten obtener la información del servicio que se está ejecutando en formato [CPE]((https://nmap.org/book/output-formats-cpe.html)), ejecutar scripts por defecto de Nmap para encontrar vulnerabilidades y para detectar el sistema operativo que el sistema objetivo, respectivamente. Otra alternativa para no escribir todos los parámetros uno por uno, es colocar el parámetro `-A`. Con esto se realiza el [segundo script](./scripts/ObtainingInformation.py) y a continuación se explica linea a linea:
    ```python
    #!/usr/bin/python3

    import nmap # Se importa Nmap

    # Se define una función para limpiar un poco las respuestas de cada item, cuando se realiza un escaneo
    def clean_string(string_value):
        string_value.strip() #Eliminar cualquier espacio, salto de línea, etc. A los lados de un texto.
        string_value = string_value.replace("\t","-") #Reemplazr las tabulaciones por un guión
        string_value = string_value.replace(" ","")#Reemplazar los espacios por nada
        return string_value.replace("\n", "|") #Reemplazar los saltos de línea por el caracter |     

    nmap_port_scanner = nmap.PortScanner() # Instanciar el escáner de uertos

    ip_to_scan = '172.17.0.2' # Ip a escanear, en este caso la de metasploitable2

    ports_to_scan = '10, 20, 21, 80, 25' #Conjunto de puertos a escanear

    aditional_parameters = "-O -sS" #Consultar información del sistema operativo y hacer escaneo sigiloso

    scan_result = nmap_port_scanner.scan(ip_to_scan, ports_to_scan, aditional_parameters) #Ejecutar el escaneo con los parámetros configurados anteriormente
    os_info = scan_result['scan'][ip_to_scan]['osmatch'][0]#Obtener información del sistema operativo
    os_class = "Clase(s) de sistema(s)\n" # Título
    for osclass in os_info['osclass']:
        os_class += f"CPE: {osclass['cpe'][0]}\n" # Formatear detalles del sistema

    filtered_info = (
        f"OS Info - Detectado con {os_info['accuracy']}% de probabilidad\n" 
        f"Nombre: {os_info['name']}\n"
        f"{os_class}\n"
        "Información de los puertos abiertos detectados\n"  
        "----------------------------------------------------------\n"  
    ) # Procesar y formatear la información

    for port, port_data in scan_result['scan'][ip_to_scan]['tcp'].items(): # Recorrer la información de cada puerto escaneado
        if port_data['state'] == 'open': # Validar que está abierto para volver a escanear por más información. Aquí se hizo el for en conjunto con este if por practicar programación, pero se puede declarar --open en aditional_parameters para que Nmap retorne solo los puertos abiertos
            result_port_info = nmap_port_scanner.scan(ip_to_scan, f"{port}", "-sCV") # Ejecutar escaneo que retorna los scripts ejecutados y la información del servicio en dicho puerto´
            result_port_info = result_port_info['scan'][ip_to_scan]['tcp'][port] # Filtrar la información del puerto
            filtered_info += (
                "Puerto\tNombre\tProducto\tCPE\n"
                f"{port}\t{result_port_info['name']}\t{clean_string(result_port_info['product'])}\t{clean_string(result_port_info['cpe'])}\n"
            )# Formatear la información
            if "script" in result_port_info: #Validar la ejecución de scripts
                filtered_info += (
                    "----------------------------------------------------------\n"
                    "Nombre Script\t\tDescripción\n"
                )# Títulos
                for script_name, description in result_port_info['script'].items(): # Recorrer los scripts ejecutados para obtener su nombre y descripción o resultado obtenido
                    filtered_info += f"{clean_string(script_name)}\t\t{clean_string(description)}\n" #Dar formato a la información
            filtered_info += "----------------------------------------------------------\n" #Cierre de la respuesta

    print(filtered_info) #Mostrar en consola el resultado
    ```

Es importante mencionar que para ejecutar los scripts, los debe realizar con permisos de administrador o root. En el caso de Kali se usó `sudo`.
___

[:arrow_backward: Regresar al inicio](../README.md)

## Referencias
- [Realiza escaneos de puertos con Nmap a cualquier servidor o sistema](https://www.redeszone.net/tutoriales/configuracion-puertos/nmap-escanear-puertos-comandos/)
- [Service and version detection](https://nmap.org/book/man-version-detection.html)
- [Nmap Scripting Engine (NSE)](https://nmap.org/book/man-nse.html)
- [OS Detection](https://nmap.org/book/man-os-detection.html)
- [21/tcp open FTP vsftpd 2.3.4 Exploit](https://amolblog.com/21-tcp-open-ftp-vsftpd-2-3-4-exploit/)
- [NSE Scripts](https://nmap.org/nsedoc/scripts/)
- [Guía definitiva Nmap en español](https://deepsec.com.mx/blog/f/guia-definitiva-de-nmap-en-espa%C3%B1ol---deepsec-academy)