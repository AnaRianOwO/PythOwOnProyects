# 1. Leer un número y mostrar su cuadrado, repetir el proceso hasta que se introduzca un número negativo.


# print("Ejercicio 1")
# num = int(input("Ingrese un número: "))

# while num >= 0:
#    print(f"El cuadrado de {num} es {num**2}")
#    num = int(input("Ingrese un número: "))
# else:
#    print("Número negativo ingresado. Fin del programa.")



# 2. Realizar un juego para adivinar un número.
# Para ello pedir un número N, y luego ir pidiendo números indicando “mayor” o “menor” según sea mayor o menor con respecto a N.
# El proceso termina cuando el usuario acierta.




# print("Ejercicio 2")

# import random
# azar = random.randint(1, 10)

# while True:
#     num = int(input("Ingrese un número: "))
#     if num == azar:
#         print("¡Adivinaste! Fin del programa.")
#         break
#     elif num < azar:
#         print("El número es mayor, intenta de nuevo")
#     else:
#         print("El número es menor, intenta de nuevo")




# 3. Diseñar un programa que muestre el producto de los 10 primeros números impares.




# print("Ejercicio 3")

# numerosImpares = []
# producto = 1

# for i in range(1, 20, 2):
#     numerosImpares.append(i)

# for i in numerosImpares:
#     producto *= i
#     print(f"{producto} * {i} = {producto}")





# 4. Pedir un número y calcular su factorial.





# print("Ejercicio 4")

# num = int(input("Ingrese un número: "))
# factorial = 1
# for i in range(1, num+1):
#     factorial *= i
    
# print(f"El factorial de {num} es {factorial}. Fin del programa.")





# 5. Pedir 10 números. Mostrar la media de los números positivos, la media de los números negativos y la cantidad de ceros.






# print("Ejercicio 5")

# lista = []

# print("Ingrese 10 números, pueden ser positivos, negativos o 0")

# for i in range(1, 11):
#     num = int(input(f"Ingrese el número {i}: "))
#     lista.append(num)
    
# positivos = [i for i in lista if i > 0]
# negativos = [i for i in lista if i < 0]
# ceros = [i for i in lista if i == 0]

# print(f"La media de los números positivos es {sum(positivos)/len(positivos)}")
# print(f"La media de los números negativos es {sum(negativos)/len(negativos)}")
# print(f"La cantidad de ceros es {len(ceros)}")
# print("Fin del programa.")





# 6. Pide un número (que debe estar entre 0 y 10) y muestra la tabla de multiplicar de dicho número.





# print("Ejercicio 6")

# num = int(input("Ingrese un número entre 0 y 10: "))

# if num < 0 or num > 10:
#     num = int(input("Número incorrecto. Ingrese un número entre 0 y 10: "))

# for i in range(1, 11):
#     print(f"{num} x {i} = {num*i}")





# 7. Una empresa que se dedica a la venta de desinfectantes necesita un programa para gestionar las facturas.
# En cada factura figura: el código del artículo, la cantidad vendida en litros y el precio por litro.
# Se pide de 5 facturas introducidas: Facturación total, cantidad en litros vendidos del artículo 1 y cuantas facturas se emitieron de más de 600.



# print("Ejercicio 7")

# facturas = [{"codigo": 0, "cantidad (l)": 0, "precio x litro": 0} for i in range(5)]

# for i in range(5):
#     facturas[i]['codigo'] = int(input(f"Ingrese el código del artículo {i+1}: "))
#     facturas[i]['cantidad (l)'] = int(input(f"Ingrese la cantidad vendida en litros del artículo {i+1}: "))
#     facturas[i]['precio x litro'] = int(input(f"Ingrese el precio por litro del artículo {i+1}: "))

# factTotal = 0

# for i in facturas:
#     factTotal += i['cantidad (l)']*i['precio x litro']
    
# print(f"Facturación total: {factTotal}")

# litrosArt1 = 0

# for i in facturas:
#     if i['codigo'] == 1:
#         litrosArt1 += i['cantidad (l)']
        
# print(f"Cantidad en litros vendidos del artículo 1: {litrosArt1}")

# facturasMas600 = 0

# for i in facturas:
#     if i['precio x litro']*i['cantidad (l)']>600:
#         facturasMas600 += 1
        
# print(f"Cantidad de facturas emitidas de más de 600: {facturasMas600}")
# print("Fin del programa.")

# 8. Pedir un número N, introducir N sueldos, y mostrar el sueldo máximo. 




# print("Ejercicio 8")

# totalSueldos = int(input("Ingrese la cantidad de sueldos a introducir: "))
# sueldoMax = 0

# for i in range(totalSueldos):
#     sueldo = int(input(f"Ingrese el sueldo {i+1}: "))
#     if sueldo > sueldoMax:
#         sueldoMax = sueldo

# print(f"El sueldo máximo es {sueldoMax}. Fin del programa.")




# 9. Necesitamos mostrar un contador con 5 dígitos (X-X-X-X-X), que muestre los números del 0-0-0-0-0 al 9-9-9-9-9, con la particularidad que cada vez que aparezca un 3 lo sustituya por una E.

# print("Ejercicio 9")

# contador = "0-0-0-0-0"

# for i in range(10):
#     print(contador.replace("3", "E"))
#     contador = contador.replace(str(i), str(i+1))
