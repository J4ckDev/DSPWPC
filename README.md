# :computer: DeepSec Pentesting Web Python Course
El curso de pentesting web consiste en enseñar como realizar ataques a diferentes entornos o sistemas donde se desee detectar y prevenir posibles fallos de seguridad. 

**:warning: AVISO: Este repositorio tiene la finalidad de compartir mis notas de clase y códigos desarrollados durante el curso para que cualquier persona aprenda a probar la seguridad de sus sistemas o aplicaciones desarrolladas. No me hago responsable del mal uso que se realice al contenido de este repositorio, siendo exclusiva responsabilidad de la persona que accede a él y lo utiliza.**

## Primera Clase
Aquí se hizo la introducción al curso donde se explicó como configurar el laboratorio de trabajo y un repaso sobre el lenguaje de programación Python.
### Configuración del laboratorio
Para el curso es necesario un laboratorio que disponga de las herramientas necesarias para aplicar lo aprendido. Para esto es necesario realizar lo siguiente:

1. Instalar [VMware Workstation](https://www.vmware.com/uk/products/workstation-player/workstation-player-evaluation.html) o [VirtualBox](https://www.virtualbox.org/) para administrar máquinas virtuales.

2. Descargar y/o configurar una máquina virtual de [Kali Linux](https://www.kali.org/get-kali/#kali-virtual-machines) o [Parrot OS](https://www.parrotsec.org/download/). En mi caso usé Kali Linux V2022.3.

3. Instalar [Docker](https://docs.docker.com/get-started/) en el sistema operativo elegido. En caso de elegir Kali, [**aquí**](./Primera%20clase/Docker.md) puedes ver los pasos que usé para instalarlo.

4. Por último, instalar Metasploitable2. Esto es un servidor que cuenta con diversas vulnerabilidades para poder realizar diferentes ataques. Se puede instalar como máquina virtual o como contenedor Docker. En caso de elegir el contenedor, [**aquí**](./Primera%20clase/Metasploitable.md) puedes ver los pasos que seguí para instalarlo en Kali Linux con Docker.

### Lenguaje Python
Gracias a la versatilidad, la cantidad de librerías y simplicidad de Python es muy sencillo crear herramientas, exploits, etc.

Es importante conocer los principios básicos del lenguaje como las variables, los tipos de variables, el uso de listas, el uso de diccionarios, el manejo de la programación orientada a objetos (POO), etc. Adicionalmente, se recomienda estudiar sobre el manejo de árboles, gráfos, stacks y colas. 

En la carpeta de la **Primera clase** por ahora se encontrará un archivo `Main.py` que tiene un ejemplo de POO. Si desea conocer lo básico del lenguaje lo invito a ver [esta sección](https://github.com/J4ckDev/MisionTic2022/tree/main/Ciclo1) de otro mis repositorios que muestro el manejo básico del lenguaje. Para las estructuras de datos como los árboles, grafos, etc; más adelante haré un repositorio dedicado a todas las estructuras de datos cuando comience a estudiarlas.