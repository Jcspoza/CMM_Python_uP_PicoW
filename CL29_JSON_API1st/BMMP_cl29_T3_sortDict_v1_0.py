# Taller Programación y Robótica en CMM BML – 2023 - Clase 29
# Resumen: Aprender metodos de ordenacion de Diccionarios
# Topicos nuevos: Sorted() lambda functions
# Ref Tutorial : https://realpython.com/sort-python-dictionary/
# Fecha inicio 2024 03 11
# Licencia : CC BY-NC-SA 4.0
# Version 2.0 more comments & names more clear

# Informative block - start
p_topic = "Ordenar diccionarios"
p_project = "- Sub parte de - A Real World Example (sort of)"
p_ref = "https://realpython.com/sort-python-dictionary/"
p_version = "1.0"
p_keyLib = "None"
print(f"Topic : {p_topic} - Ref : {p_ref}")
print(f"Libreria: {p_keyLib}")
print(f"Program: {p_project} - Version: {p_version}")
print("============================")
# Informative block - end

# Ir comentando y des-comentado para ver mejor los ejemplos

# 1- Ejemplo 1 funcion sorted() : ordena objetos itelables como listas y diccionarios
print('EJ 1- Ordenamos una lista de numeros')
numbers = [5, 3, 4, 3, 6, 7, 3, 2, 3, 4, 1]
print('Lista sin ordenar')
print(numbers)
print('Lista ORDENADA')
print(sorted(numbers))

# # Ejemplo 2- ordenamos lista de palabras - orden normal
# print('EJ 2- Ordenamos una lista de palabras - orden normal')
# words = ["ab", "aa", "ac", "ba", "cb", "ca"]
# print('Lista sin ordenar')
# print(words)
# print('Lista ORDENADA')
# print(sorted(words))
# print('IMPORTANTE : con la funcion sorted() se genera una lista NUEVA. Volvamos a imprimir lista original')
# print(words)
# print('Si hubieramos usado el metodo .sort() hubieramos MODIFICADO la lista original. aplicamos .sort()')
# words.sort()
# print('Volvamos a imprimir lista original (despues de .sort())')
# print(words)



# Ejemplo 3 - ordenamos una lista de palabaras por la segunda letra de cada palabra
# To customize what the sorted() function uses to sort the elements,
# you can pass in a callback function to the key parameter.
# A callback function is a function that’s passed as an argument to another function.
# For sorted(), you pass it a function that acts as a sort key.
# The sorted() function will then call back the sort key for every element.
# def select_second_character(word):
#     return word[1]
# 
# print('EJ 3- Ordenamos una lista de palabras - orden por la 2da letra')
# words = ["ab", "aa", "ac", "ba", "cb", "ca"]
# print('Lista sin ordenar')
# print(words)
# print('Lista ORDENADA por la segunda letra')
# print(sorted(words, key=select_second_character))
# print('Nota: cuando la 2da letra es igual, se conserva el orden original')

# Ejemplo 4 - Generar vistas de un diccionario y ordenar por claves 
# Las vistas de diccionario son maneras 'ligeras' de generar iterables ligados a diccionarios
# para trabajr sobre los diccionarios. Son de solo lectura, pero al estar ligadas a los diccionarios
# reflejan los cambios
# print('EJ 4- Generar vistas de un diccionario y ordenar por claves')
# people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}
# print('Generamos una vista de solo lectura de las claves')
# print(people.keys())
# print('Generamos una vista de solo lectura de los valores')
# print(people.values())
# print('Generamos una vista de solo lectura de clave-valor')
# print(people.items())
# print('Cambiamos un valor y volvemos a ver la vista generada ANTERIORMENTE')
# people[2] = "Jose"
# print(people.items())
# print('Si ahora usamos la funcion sorted() sobre la vista de lectura de clave-valor tenemos')
# print(sorted(people.items()))
# print('Ordena las tuplas lexicograficamente = ordena el diccionario por claves')

# # Ejemplo 5 - Ordenar vistas de diccionario por valor (no por clave)
# # print('EJ 5- Ordenar vistas de diccionario por valor (no por clave)')
# people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}
# def obtener_valor(cosa): # tomara el 2do elemento de 'cosa'
#     return cosa[1]
# 
# print('Generamos una vista de solo lectura de clave-valor')
# print(people.items())
# print('Ahora usamos la funcion sorted() sobre la vista y ordenamos por el SEGUNDO elemento = valor')
# print('usando una funcion definida con anterioridad para la funcion "callback" de ordenacion')
# print(sorted(people.items(),key=obtener_valor))
# 
# # The 'key' parameter accepts a callback function.
# # The function can be a normal function identifier or a lambda function.
# # Lambda functions are also known as anonymous functions because they don’t have a name.
# # Lambda functions are standard for functions that you’re only using once in your code.
# # Lambda functions confer no benefit apart from making things more compact, 1 line only
# 
# print('Ahora ordenamos por el SEGUNDO elemento = valor, pero con funcion lambda')
# print(sorted(people.items(),key=lambda cosa: cosa[1]))
# 
# print('Ahora ordenamos por el SEGUNDO elemento = valor, pero con funcion lambda y orden INVERSO')
# print(sorted(people.items(),key=lambda cosa: cosa[1], reverse=True))