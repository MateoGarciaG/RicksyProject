# Proyecto Scrapping
## RicksyProject

![Project Logo](frontend/resources/img/logos/logo_rickMorty.jpg)

### Descripción del Proyecto
En este proyecto, hemos construido un sitio web con base HTML y CSS, para luego scrappear este mismo sitio construyendo propiamente un scrapper.

### Como se ejecuta?
Para ejecuta el programa podemos ejecutar el archivo desde la terminal o desde el IDE haciendo click derecho y ejecutandolo.

```
adria@DESKTOP-OSU69DN MINGW64 ~/Escritorio/proyecto_diciembre/RicksyProject$ python main.py
```

### Virtual environment
En este proyecto también hemos hecho uso de un entorno virtual que se crean de esta manera:
```
(ruta) -m venv nuevo_entorno_virtual
```
luego de haberlo creado hay que activarlo:
```
nuevo_entorno_virtual\Scripts\activate.bat
```
de esta manera el entorno ya estarà activado en la ruta que le haya indicado

### Funcionalidad
La función de este programa es la de ser capaz de extraer información de un pàgina web de menus y poder almacenarla en una base de datos, en este caso MongoDB.

### Como distribución
* Crea el directorio y sitúate en él:
```
$ mkdir ./RicksyProject
$ cd RicksyProject
```
* Clona el proyecto
```
git clone https://github.com/MateoGarciaG/RicksyProject.git
```
* Activa el entorno virtual:
```
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip3 install -r requirements.txt
```
* Instala el proyecto:
```
$ pip3 install dist/Menus_Scrapping_Tool-0.0.1-py3-none-any.whl
```
* Ejecuta la herramienta:
```
python3 main.py
```
### Tecnología de las cuales hemos hecho uso
* Python 3
* HTML5
* CSS3
* requests
* autopep8
* pymongo
* dnspython
* pytest
* MongoDB
* json module

### Documentación

https://github.com/MateoGarciaG/RicksyProject/blob/master/docs/documentacion_proyecto_RicksyProject.pdf

### Documentación mediante PyDoc
También puedes acceder a la documentación respecto al backend y relacionada con cada modulo y función. Para ello necesitas primero activar el entorno virtual y mediante los siguientes comandos:

* Para ver la documentación de un módulo:
```
$ python3 -m pydoc ruta/nombre_modulo
```
* Para ver la documentación de un fichero del módulo:
```
$ python3 -m pydoc ruta/nombre_modulo/nombre_fichero
```
* Con PyDoc podemos generar documentación de nuestro código donde se creará un fichero html con la información del fichero , esto con el siguiente comando:
```
$ python3 -m pydoc -w ruta/nombre_modulo/nombre_fichero
```
* En el caso de que lo hicieramos para un módulo:
```
$ python3 -m pydoc -w ruta/nombre_modulo . /
```
* Incluso PyDoc nos permite consultar toda nuestro documentación iniciando un servidor local temporal desde el directorio del paquete:
```
$ python3 -m pydoc -p 5001
```

### Licencia
MIT License

Copyright (c) 2020 Adrià Flexas and Mateo García

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

### Autores
Mateo García y Adrià Flexas! 