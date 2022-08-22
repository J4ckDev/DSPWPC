# Escaneo de puertos con Nmap
El escaneo de puertos permite conocer el estado en que se encuentran los puertos de una red. En TCP y UDP los estados que puede tener un puerto son los siguientes:

- **Open - Abierto**: El puerto responde a las peticiones de conexión.
- **Closed - Cerrado**: El puerto es inalcanzable, indicando que no existe ningún servicio en ejecución.
- **Filtered - Filtrado**: Existe un firewall o cortafuegos monitoreando el tráfico que bloquea ciertas peticiones de conexión al puerto.

De estos estados, normalmente el objetivo es encontrar los puertos abiertos para analizar si se puede [explotar algún tipo de vulnerabilidad](https://www.infosegur.net/blog/que-es-un-puerto-abierto-y-como-puede-afectar-a-nuestra-seguridad#:~:text=En%20ciberseguridad%2C%20el%20t%C3%A9rmino%20puerto,paquetes%2C%20es%20un%20puerto%20cerrado.). Es aquí donde Nmap toma importancia, ya que es una herramienta que tiene diversas formas para realizar el escaneo de puertos.

## Tipos de escaneo
A continuación se explicarán los tipos de escaneo que se pueden realizar.

### TCP Connect Scan - Comando sT
El escaneo por conexión TCP construye una petición y la envía a la dirección IP del sistema objetivo estableciendo una conexión TCP completa (SYN - SYN/ACK - ACK). Este tipo de escaneo es demorado porque debe enviar más paquetes para obtener obtener información, por lo que es más probable que el sistema guarde el registro de la petición o un sistema de detección de intrusos detecte la petición.

### TCP Stealth Scan - Comando sS
El escaneo sigiloso construye una petición y la envía a la dirección IP del sistema objetivo estableciendo una conexión TCP a medio completar (SYN - SYN/ACK - RST). Este tipo de escaneo es rápido y el más popular para identificar si un puerto está abierto.

### UDP Scan - Comando sU
El escaneo por UDP consiste en enviar paquetes UDP a la dirección IP del sistema objetivo, si recibe como respuesta otro paquete UDP significa que el puerto está abierto. Aunque este escaneo es lento, algunas veces los auditores de seguridad ignoran estos puertos, por lo que es muy frecuente encontrar servicios UDP vulnerables. Este escaneo se puede combinar con el [anterior](#tcp-stealth-scan---comando-ss) para comprobar ambos protocolos al mismo tiempo.

### TCP ACK Scan - Comando sA
A diferencia de los escaneos anteriores, el escaneo por ACK se utiliza identificar si el sistema objetivo cuenta con un firewall o cortafuegos. Si se recibe como respuesta RST, significa que el puerto no está filtrado; pero si se recibe un mensaje de error ICMP o no se reciba respuesta, significa que el puerto está filtrado.

### TCP NULL Scan - Comando sN
El escaneo nulo envía una petición sin ninguna bandera definida, esto se traduce a que [la cabecera de bandera TCP (TCP flag header) la iguala a 0](https://www.hackingarticles.in/nmap-scans-using-hex-value-flags/). Si el sistema objetivo sigue al pie de la letra el [RFC del estándar TCP](https://www.rfc-editor.org/rfc/rfc793.txt), cuando se realiza este tipo de escaneo si se obtiene como respuesta un RST, significa que el puerto está cerrado; si no se recibe respuesta, el sistema tiene el puerto abierto con posible filtrado; pero si se recibe un error ICMP, significa que es un puerto filtrado.

## Referencias
- [Introducción TCP/IP](https://www.um.es/docencia/barzana/DIVULGACION/INFORMATICA/Introduccion_a_TCPIP.pdf)
- [Open Port Vulnerabilities List](https://blog.netwrix.com/2022/08/04/open-port-vulnerabilities-list/)
- [Port Scanning Basics](https://nmap.org/book/man-port-scanning-basics.html)
- [Port Scanning Techniques](https://nmap.org/book/man-port-scanning-techniques.html)
___

[:arrow_backward: Regresar al inicio](../README.md)