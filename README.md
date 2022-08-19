# :computer: DeepSec Pentesting Web Python Course <!-- omit in toc -->
El curso de pentesting web consiste en enseñar como realizar ataques a diferentes entornos o sistemas donde se desee detectar y prevenir posibles fallos de seguridad. 

**:warning: AVISO: Este repositorio tiene la finalidad de compartir mis notas de clase y códigos desarrollados durante el curso para que cualquier persona aprenda a probar la seguridad de sus sistemas o aplicaciones desarrolladas. No me hago responsable del mal uso que se realice al contenido de este repositorio, siendo exclusiva responsabilidad de la persona que accede a él y lo utiliza.**

## Tabla de Contenido <!-- omit in toc -->
- [Clase 1 - Introducción al curso](#clase-1---introducción-al-curso)
  - [Configuración del laboratorio](#configuración-del-laboratorio)
  - [Lenguaje Python](#lenguaje-python)
- [Clase 2 - Comandos Linux y Sockets](#clase-2---comandos-linux-y-sockets)
  - [Lista de comandos Linux](#lista-de-comandos-linux)
  - [Conexiones con sockets en Python](#conexiones-con-sockets-en-python)

## Clase 1 - Introducción al curso
Aquí se hizo la introducción al curso donde se explicó como configurar el laboratorio de trabajo y un repaso sobre el lenguaje de programación Python.
### Configuración del laboratorio
Para el curso es necesario un laboratorio que disponga de las herramientas necesarias para aplicar lo aprendido. Para esto es necesario realizar lo siguiente:

1. Instalar [VMware Workstation](https://www.vmware.com/uk/products/workstation-player/workstation-player-evaluation.html) o [VirtualBox](https://www.virtualbox.org/) para administrar máquinas virtuales.

2. Descargar y/o configurar una máquina virtual de [Kali Linux](https://www.kali.org/get-kali/#kali-virtual-machines) o [Parrot OS](https://www.parrotsec.org/download/). En mi caso usé Kali Linux V2022.3.

3. Instalar [Docker](https://docs.docker.com/get-started/) en el sistema operativo elegido. En caso de elegir Kali, [**aquí**](./Clase%201/Docker.md) puedes ver los pasos que usé para instalarlo.

4. Por último, instalar Metasploitable2. Esto es un servidor que cuenta con diversas vulnerabilidades para poder realizar diferentes ataques. Se puede instalar como máquina virtual o como contenedor Docker. En caso de elegir el contenedor, [**aquí**](./Clase%201/Metasploitable.md) puedes ver los pasos que seguí para instalarlo en Kali Linux con Docker.

### Lenguaje Python
Gracias a la versatilidad, la cantidad de librerías y simplicidad de Python es muy sencillo crear herramientas, exploits, etc.

Es importante conocer los principios básicos del lenguaje como las variables, los tipos de variables, el uso de listas, el uso de diccionarios, el manejo de la programación orientada a objetos (POO), etc. Adicionalmente, se recomienda estudiar sobre el manejo de árboles, gráfos, stacks y colas. 

En la carpeta de la **Primera clase** por ahora se encontrará un archivo `Main.py` que tiene un ejemplo de POO. Si desea conocer lo básico del lenguaje lo invito a ver [esta sección](https://github.com/J4ckDev/MisionTic2022/tree/main/Ciclo1) de otro mis repositorios que muestro el manejo básico del lenguaje. Para las estructuras de datos como los árboles, grafos, etc; más adelante haré un repositorio dedicado a todas las estructuras de datos cuando comience a estudiarlas.

___

[:arrow_up_small: Regresar a la Tabla de Contenido](#tabla-de-contenido)

## Clase 2 - Comandos Linux y Sockets
Se hizo una introducción a los comandos linux que usaremos en el curso y como realizar conexiones con sockets en Python.

### Lista de comandos Linux
Todos los comandos se ejecutan en un terminal. A continuacion, se presenta la lista de comandos usados en la clase:

- `ls -lah`: Este comando lista los archivos con todos los detalles y ordenados en orden alfabético.
- `mkdir nombre_carpeta`: Sirve para crear una carpeta.
- `cd ruta/al/directorio`: Nos posiciona en el directorio o carpeta especificada.
- `pwd`: Nos indica donde nos encontramos.
- `chmod +x archivo`: Nos permite adicoinarle el permiso de ejecución a un archivo.
- `nano`: Abre el editor de texto.
- `cat`: Mostrar el contenido de un archivo.
- `cp archivo ruta/a/la/nueva/ubicación`: Copia un archivo a la ubicación especificada.
- `mv archivo ruta/a/la/nueva/ubicación`: Mueve un archivo a la ubicación especificada.
- `touch nombre_archivo`: Crea un archivo vacío con el nombre y extensión especificada.
- `man comando`: Sirve para obtener la documentación detallada de un comando especificado. Por ejemplo, `man ls` muestra la documentación más detallada del comando `ls`.
- `rm archivo`: Elimina el archivo especificado.

Existen otros comandos pero estos serán los más usados durante el curso, si desea conocer otros detalles sobre Linux puede revisar [este curso](https://www.netacad.com/es/courses/os-it/ndg-linux-essentials). Si se desea una explicación rápida de los comandos, puede usar [este sitio web](https://explainshell.com/). 

### Conexiones con sockets en Python
Para esta sección se recomienda tener un conocimiento básico sobre el [modelo cliente - servidor](https://blog.infranetworking.com/modelo-cliente-servidor/), los [protocolos TCP - UDP](https://ccnadesdecero.es/capa-transporte-definicion-y-funciones/) para las conexiones de red y tener claro qué es un [socket](https://www.redeszone.net/tutoriales/configuracion-puertos/que-es-socket-tcp-udp-diferencias-puertos/).

Con los términos claros, en la primera parte de esta sección se realizaron dos códigos que nos permitieron crear un pequeño [servidor](./Clase%202/Server.md) y un [cliente](./Clase%202/Clients.md#cliente-con-librería-socket) para probar conexiones entre sí. En la segunda parte se encendió el contenedor de Metasploitable2, en mi caso con los comandos `docker start container-name` y `docker exec -it container-name sh -c "/bin/services.sh && bash"`, y se ejecutó un [escáner de puertos](./Clase%202/PortScanner.md) desarrollado en clase para detectar sus puertos abiertos. En la última parte se usa la librería [PWN Tools](https://github.com/Gallopsled/pwntools#readme) para hacer un [cliente](./Clase%202/Clients.md#cliente-con-librería-pwn) que nos permitiera conectarnos a un socket de una forma más sencilla.

___

[:arrow_up_small: Regresar a la Tabla de Contenido](#tabla-de-contenido)