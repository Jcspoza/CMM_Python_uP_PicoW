# Trabajar con JSON -> Visualizar API´s Spanish

## Objetivo

En esta clase, vamos a estudiar 2 temas que necesitamos para "armar" la visualización de una consulta con API´s en python o micropython

1. **Aprender a trabajar con JSON en Python**

2. **Explotar los datos open source por medio de API´s** del Ayuntamiento de Madrid y/ o AEMT - primeros pasos

Quedaría por estudiar como '**Crear GUI´s con guizero'**, pero lo dejaremos para otra clase

## <u>1-Aprender a trabajar con JSON en Python (fin)</u>

### Tutoriales que vamos a Seguir

[Tutorial 1 Sencillo - Python leer archivo JSON – Cómo cargar JSON desde un archivo y procesar dumps](https://www.freecodecamp.org/espanol/news/python-leer-archivo-json-como-cargar-json-desde-un-archivo-y-procesar-dumps/)

[Tutorial 2 + Completo - Working With JSON Data in Python – Real Python](https://realpython.com/python-json/)

[Tutorial 3 - Ordenar Listas y Diccionarios en Python](https://realpython.com/sort-python-dictionary/))

### Tabla resumen de programas

| Programa                                                       | Tutorial 1 o 2 | Objetivo de Aprendizaje                                                                                                                 |
| -------------------------------------------------------------- |:--------------:| --------------------------------------------------------------------------------------------------------------------------------------- |
| [BMMP_cl29_T1_json2dict.py](./BMMP_cl29_T1_json2dict.py)       | T1 - Ejemplo1  | Ver como se convierte un JSON (str) a diccionario                                                                                       |
| [BMMP_cl29_T1_dict2json.py](BMMP_cl29_T1_dict2json.py)         | T1- Ejemplo2   | Ver como se convierte un diccionario a JSON (str). Indentar  y ordenar el JSON                                                          |
| [BMMP_cl29_T1_filejson2dict.py](BMMP_cl29_T1_filejson2dict.py) | T1- Ejemplo 3  | Ver como se convierte un fichero JSON  a diccionario                                                                                    |
| [BMMP_cl29_T1_dict2filejson.py](BMMP_cl29_T1_dict2filejson.py) | T1 - Ejemplo 4 | Ver como se convierte un Diccionario ( obtenido de fichero JSON y luego manipulado) a fichero JSON (modificado)                         |
| [BMMP_cl29_T2_tSimple2JSON.py](BMMP_cl29_T2_tSimple2JSON.py)   | T1 y T2        | Ejemplos de cambio de tipos de datos simple de Python a JSON y de nuevo a Python                                                        |
| [BMMP_cl29_T3_sortDict_v1_0.py](BMMP_cl29_T3_sortDict_v1_0.py) | T3             | Ejemplos de ordenación de Listas y Diccionarios                                                                                         |
| [BMMP_cl29_T2_APItodos_v2_0.py](BMMP_cl29_T2_APItodos_v2_0.py) | T2- real world | Como obtener información con API´s bajada como JSON, luego manipularla y volcar el resultado de la manipulación a un nuevo fichero JSON |

### Recomendaciones de estudio con los 2 tutoriales

1. **Leer y hacer primero el tutorial 1** que es relativamente sencillo. Incluye 4 ejemplos que estan hechos en los programas adjuntos con algo mas de detalle que lo indicado en el tutorial 

2. **Leer la parte teórica del Tutorial 2** desde "*A (Very) Brief History of JSON" -> "Deserializing JSON""*

3. **Estudiar como se vuelca a JSON cada tipo `simple'**

4. **Leer y hacer el Tutorial 3 Ordenar Listas y Diccionarios.** Ejecutar el programa de ejemplo en ejemplo,  volviendo comentarios el resto de ejemplos.

5. **Leer y hacer la parte de "A Real World Example (sort of)"**. Hay varios conceptos de Python que serán nuevos, asi que servirá como aprendizaje de manipular diccionarios y listas

6. No es necesario leer el resto de Tutorial 2 , es excesivamente técnico

### **Leer y hacer el tutorial 1**

Los programas siguen el tutorial y no son complicados de entender. Recomiendo hacerlos y ejecutarlos de uno en uno junto a la lectura del tutorial

| Programa                      | Tutorial 1 o 2 | Objetivo de Aprendizaje                                                                                         |
| ----------------------------- | -------------- | --------------------------------------------------------------------------------------------------------------- |
| BMMP_cl29_T1_json2dict.py     | T1 - Ejemplo1  | Ver como se convierte un JSON (str) a diccionario                                                               |
| EBMMP_cl29_T1_dict2json.py    | T1- Ejemplo2   | Ver como se convierte un diccionario a JSON (str). Indentar y ordenar el JSON                                   |
| BMMP_cl29_T1_filejson2dict.py | T1- Ejemplo 3  | Ver como se convierte un fichero JSON  a diccionario                                                            |
| BMMP_cl29_T1_dict2filejson.py | T1 - Ejemplo 4 | Ver como se convierte un Diccionario ( obtenido de fichero JSON y luego manipulado) a fichero JSON (modificado) |

### **Leer la parte teórica del Tutorial 2**

Desde "*A (Very) Brief History of JSON" -> "Deserializing JSON", y aunque no hay conceptos nuevos respecto al tutorial 1, conviene leerlo por asentar conceptos y segur el resto de este tutorial 2

### Estudiar como se vuelca a JSON cada tipo `simple'

En los ejemplos del Tutorial 1 habremos comprendido que la serialización y deserialización son parecidos a traducir y volver al idioma original: el resultado será muy parecido, pero no idéntico: **Ver el caso de las Tuplas**

**Con los tipos de datos complejos o los tipos de datos "creados por nosotros" la traducción a JSON es un proceso complejo**. Si tienes interes, lee la ultima parte del Tutorial 2

### Leer y hacer Tutorial 3 Ejemplos de ordenación de Listas y Diccionarios

Ir haciendo los ejemplos en Python de ordenación de Listas y Diccionarios del programa:

[BMMP_cl29_T3_sortDict_v1_0.py](BMMP_cl29_T3_sortDict_v1_0.py)

Aqui se explicara la funcion **sorted()** en detalle y el uso de **funciones lambda** ( solo lo necesario para el ejemplo)

### Leer y hacer la parte de *A Real World Example (sort of)*

Es la parte mas interesante del tutorial. Se recomienda ir siguiendo los apartados del seudocódigo junto con el programa:

[BMMP_cl29_T2_APItodos_v2_0.py](BMMP_cl29_T2_APItodos_v2_0.py), 

pasando el codigo python a comentarios, e ir des-comentando lo a medida que se va entendiendo cada parte. Veamos el seudocódigo

1- Consultar una API de ejemplos aplicación de tareas y extraer una lista de todos

2 - Ver aspecto de los datos con los 3 primeros de ellos (si se ha volcado como  lista)

3- Extraemos la info de todos los 'todos' para determinar los usuarios con el máximo numero de tareas completadas

3.1 Map of userId to number of complete TODOs for that user

        Obtenemos el diccionario 'Done_todos_by_user'

3.2 Create a sorted list of (userId, num_complete) dictionary pairs.

    Aqui necesitamos saber como ordenar diccionarios por los valores ( cosa que no es directa) [Ordenar diccionarios - Sorting a Python Dictionary: Values, Keys, and More – Real Python](https://realpython.com/sort-python-dictionary/))

Hay que hacer un par de ejemplos de este tutorial, para entender la ordenación de diccionarios por valor

3.3 Get the maximum number of complete TODOs

3.4 Create a list of all users who have completed the maximum number of TODOs, porque puede ser mas de uno, y lo muestra

3.5 Define unaa funcion para filtar los 'todos' de los usuarios con mas numero de 'todos' completados

3.6 Con la ayuda de la funcion de filtor, escribe a un fichero los 'todos' filtrados.

4. Muestra el fichero resultado

## <u>2-Entendiendo las API´s de AEMET y Ayuntamiento de Madrid - Primeros pasos (en progreso)</u>

### Enlaces mas genéricos

[Portal de datos abiertos del Ayuntamiento de Madrid](https://datos.madrid.es/portal/site/egob)

Hay un video explicativo asi como un "visualizador" para publico en general y luego hay un acceso a datos por API´s

[AEMET OpenData - Agencia Estatal de Meteorología - AEMET. Gobierno de España](https://www.aemet.es/es/datos_abiertos/AEMET_OpenData)

De nuevo hay un visualizador para publico en general y luego hay un acceso a datos por API´s

### Enlaces específicos

[Open data AEMET- Documentacion y Prueba](https://opendata.aemet.es/dist/index.html?)

[Madrid Datos Abiertos API - Documentacion y Prueba - API - Portal de datos abiertos del Ayuntamiento de Madrid](https://datos.madrid.es/portal/site/egob/menuitem.214413fe61bdd68a53318ba0a8a409a0/?vgnextoid=b07e0f7c5ff9e510VgnVCM1000008a4a900aRCRD&vgnextchannel=b07e0f7c5ff9e510VgnVCM1000008a4a900aRCRD&vgnextfmt=default)

### ¿ Como estudiar estas API´s?

Ambas fuentes de información ( AEMET y Ayuntamiento MAD)  son muy amplias y solo queremos en esta clase acceder y dar unos primeros pasos básicos.

Asi que vamos a fijar una **estrategia progresiva de estudio**:

1. Curiosear por la documentación y elegir 1 información objetivo en cada web

2. Acceder y ver si hay que dar 1 paso o 2 para la información objetivo

3. Ver estructura de la información objetivo en cada caso

4. Extraer (parte de ) la información objetivo y presentarla

Vamos a usar estos 2 programas, y hay que ejecutarlos, tapando como comentarios la parte final de los progrmas e irla desvelando poco a poco

| Programa                                                               | Fuente                 | Objetivo de Aprendizaje               |
| ---------------------------------------------------------------------- | ---------------------- | ------------------------------------- |
| [BMMP_CL29_APImad_CMM_1_0.py](BMMP_CL29_APImad_CMM_1_0.py)             | Ayuntamiento de Madrid | Informacion Centros de Mayores Centro |
| [BMMP_CL29_APIaemet_predMad_1_0.py](BMMP_CL29_APIaemet_predMad_1_0.py) | AEMET                  | Predicción Madrid capital             |

---

TO DO :  
