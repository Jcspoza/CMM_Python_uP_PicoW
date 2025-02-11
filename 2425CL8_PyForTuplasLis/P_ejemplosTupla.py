# Taller Programación y Robótica en Colegio Santo Domingo – 2024 -2025 - Clase 5
# Resumen: Ejemplos con tuplas
# Aprendizajes :  uso de for 
# Autor y y Fecha JCSP 2024 10 08
# Licencia : CC BY-NC-SA 4.0
# https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es


# Defino la tupla que voy a usar en los ejemplos

tLetrasyNum = 'd', 'c', 'b', 'a', 4, 3, 2, 1
# es mas elegante definir con () tLetrasyNum = ('d', 'c', 'b', 'a', 4, 3, 2, 1) , pero es =

print('Veamos el tipo de la variable compuesta con "type(tLetrasyNum)"')
print(type(tLetrasyNum))
print('----')

print('Veamos la longitud = numero de objetos dentro con "len(tLetrasyNum)"')
print(len(tLetrasyNum))
print('----')

print('Veamos si 4 esta dentro del objeto con "4 in tLetrasyNum"')
print(4 in tLetrasyNum)
print('----')

print('Veamos si "A" esta dentro del objeto con "A in tLetrasyNum"')
print('A' in tLetrasyNum)
print('----')

print('Veamos el primer objeto con "tLetrasyNum[0]"')
print(tLetrasyNum[0])
print('----')

# print('Veamos el objeto 10º objeto con "tLetrasyNum[9]"')
# print(tLetrasyNum[9])
# print('----')
# 
print('Veamos el lugar del objeto "a" con "tLetrasyNum.index(a)"')
print(tLetrasyNum.index('a'))
print('----')

print('Veamos un corte de la tupla del 2º al 4º objeto con "tLetrasyNum[1:4]"')
print(tLetrasyNum)
print(tLetrasyNum[1:4])
print('----')