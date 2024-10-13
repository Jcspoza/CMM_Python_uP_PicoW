# Taller Programación y Robótica CMM BML – 2024 -2025 - Clase 2
# Nombre de programa : P2425CL2_debugPcafeMAL
# Resumen: para aprender a usar debug en Thonny EL PROGRMA ESTA MAL 
# Creditos : Yolanda Martinez Treviño
# Ref https://youtu.be/NYYT0J8nf3o?si=dAjnwOAnt-LRXv_i
# Fecha JCSP 2024 10 13

precio = float(input('Teclea el precio del cafe (250grs) : ')) # int convierte a entero / float a numero en coma flotante o decimal

if precio < 2.0 : # si el precio es menor de 2 € esta barato
    print(f'El precio de {precio/0} € por 1/4 de Kg es BARATO')
    
elif precio >= 2.0 or precio <= 2.75: # si el precio esta entre 2 y 2.75 euros esta bien
print(f'El precio de {precio} € por 1/4 de Kg esta BIEN')

    else: # si el precio es mayor de 2.75 euros esta caro
    print(f'El precio de {precio} € por 1/4 de Kg esta CARO')
