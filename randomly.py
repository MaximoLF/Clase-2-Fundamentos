# Uso y explicacion de randmom

import random
import time
# num=random.randint(1, 10)
# print(num)

# for i in range(num):
#     print("Hola Maximo")


# for i in range(10): # Tabla de multiplicar
#     print(f"{num}x{i}={num*i}")


#---------------------------------------------------------------------------------------------------------

# Hay 3 personas que juegan golf, y cada persona tiene la posibilidad de golpear y la distancia varia entre 60 y 190 metros.
#  mostrar al final, el golpe mas fuerte

# 

# ball=random.randint(60, 190)
# ball2=random.randint(60, 190)
# ball3=random.randint(60, 190)
# j1=input("intrese el nombre del jugador 1: ")
# j2=input("intrese el nombre del jugador 2: ")
# j3=input("intrese el nombre del jugador 3: ")
# print(j1,"Ah golpeado la pelato a", ball, "metros!")
# print(j2,"Ah golpeado la pelato a", ball2, "metros!")
# print(j3,"Ah golpeado la pelato a", ball3, "metros!")


# FORMA HECHA POR EL PROFE

# j1=random.randint(60, 190)
# j2=random.randint(60, 190)
# j3=random.randint(60, 190)

# print(f"El jugador 1 lanzo la pelota a {j1} metros")
# print(f"El jugador 2 lanzo la pelota a {j2} metros")
# print(f"El jugador 3 lanzo la pelota a {j3} metros")

# if j1>j2 and j1>j3:
#     print(f"El jugador 1 lanzo la pelota mas lejos")
# elif j2>j1 and j2>j3:
#     print(f"El jugador 2 lanzo la pelota mas lejos")
# elif j3>j1 and j3>j2:
#     print(f"El jugador 1 lanzo la pelota mas lejos")
# else:
#     print("Nadie gano, hay un empate")


#---------------------------------------------------------------------------------------------------------

# Tirar 2 dados

# dado1=random.randint(1, 6)
# dado2=random.randint(1, 6)
# print(f"El dado dio {dado1}")
# print(f"El dado dio {dado2}")

# # Si los dados dan el mismo numero el jugador se va a la carcel

# if dado1==dado2:
#     print("Te salieron 2 numeros iguales, te vas a la carcel")
# else:
#     print("Continue avanzando")

#---------------------------------------------------------------------------------------------------------

# Ludo | 1 jugador juega,y lanza 2 dados, por cada unidad en el dado avanza una posicion el el trablero
# cuando llegue a 50, gana, mostrar cuantos turnos le tomo llegar a la meta


# posicion=0
# meta=50
# turnos=1

# while posicion<meta:
#     dado1=random.randint(1,6)
#     dado2=random.randint(1,6)

#     print(f"El dado dio {dado1}")
#     print(f"El dado dio {dado2}")
#     time.sleep(1)
#     posicion+=dado1+dado2
#     print(f"El jugado esta en la posicion {posicion}")
#     turnos+=1

# print(f"El jugador ha llegado a la meta {turnos} turnos")


# Dos peleadores se piden al inicio de la pelea, cada peleador inicia con 100 de HP, se debe hacer una pelea por tunrnos
# Y cada golpe varia entre 7 y 18, se ternmina el match cuando uno o los 2 tienen su HP menor o igual a 0
# Se debe mostrar el ganador final | BONUS: mostrar el barras de energia de cada peleador



#---------------------------------------------------------------------------------------------------------

# Adicina el numero | Crea un numero random entre el 1 y el 100, luego pide al usuario que adivine el numero
# Si el usuario pone un numero mayor al generado debe decir "Te pasaste", en caso contrario "El numero a adivinar es mayor"
# Solo hay 5 posibilidades de adivinar.


#---------------------------------------------------------------------------------------------------------

# Loteria
# Generar 3 numeros entre 1 y 9, luego tirar numeros al azar en ese rango. Cuando todos los numeros coincidan con los primeros 3
# generados, debe poner "Ganaste", luego contar cuantos numeros tuvo que tirar para ganar la loteria

# n1=random.randint(1,9) # Generar numero en rango
# n2=random.randint(1,9) # Generar numero en rango
# n3=random.randint(1,9) # Generar numero en rango
# t1=False
# t2=False
# t3=False
# print(f"Los numeros ganadores son: {n1}, {n2}, {n3}")
# nums=0
# while not t1 or not t2 or not t3:
#     numerito=random.randint(1,9)
#     print("El numero es", numerito)
#     time.sleep(1)
#     if numerito==n1:
#         t1=True
#     if numerito==n2:
#         t2=True
#     if numerito==n3:
#         t3=True
#     nums+=1
# print(f"Ganaste, en {nums} turnos")


#---------------------------------------------------------------------------------------------------------

# FABRICA DE ENLATADOS (PRACTICA PRUEBA)
# Se necesita hacer el algoritmode productos enlatados. Se debe consultar el peso del producto (en gramos) (solo valores positivos)
# El porcentaje de sodio en el (Solo valores entre 1 y 100), y si se va a vender nacional o internacionalmente.
# Considera los criterios en la siguiente tabla

# menos de 500grs | lata normal
# 501 hasta 1500grs | lata mediana
# 1501 y mas | lata grande
# Si el sodio es menos del 5%, la lata queda igual | si es entre 5% y 8% lata especial | si tiene 9% o mas, lata acorazada
# a las latas internacionales, se le debe pegar un sticket de validacion sanitaria
# EJ:800, 7%, 2==> lata mediana, especial con sticket sanitario

#Otra forma

# while True:
#     print("Solo valores positivos")
#     peso=int(input("Ingrese el peso del producto: "))
#     if peso>0:
#         break

# -------------

# peso=int(input("Ingrese el peso del producto: "))
# while peso<1:
#     print("Solo valores positivos")
#     peso=int(input("Ingrese el peso del producto: "))

# sodio=int(input("Ingrese el procentaje de sodio del producto: "))
# while sodio<1 or sodio>100:
#     print("El porcentaje debe ser entre 1 y 100")
#     sodio=int(input("Ingrese el procentaje de sodio del producto: "))

# mercado=int(input("Ingrese el mercado del producto: 1.- Nacional , 2.- Internacional"))
# while mercado<1 or mercado>2:
#     mercado=int(input("Ingrese el mercado del producto: 1.- Nacional , 2.- Internacional"))

# if peso<500:
#     lata="Lata normal"
# elif 501<peso<1500:
#     lata="Lata mediana"
# elif peso>1501:
#     lata="Lata grande"

# if sodio<5:
#     sodio="Lata normal"
# elif 5<sodio>8:
#     sodio="Lata especial"
# elif sodio>9:
#     sodio="Lata acorazada"

# if mercado==1:
#     sticker="Sin sticker sanitario"
# else:
#     sticker="Con Sticker Sanitario"

# print(f"{lata}, {sodio}, {sticker}")




#---------------------------------------------------------------------------------------------------------


# Realizar las clasificacion de peces. Generar una cantidad aleatoria de captura de peces entre 10 y 20
# Capturar peces y clasificarlos por su peso, para saber como se venderan
# 800grs o menos, a lata | 801 o mas, a la plancha | contar cuando quedaron a la plancha cuantos quedaron para embasar a lata


captura=random.randint(10, 20)

print(f"Caputuraste {captura} peces")
peces=0
pez1=0
pez2=0
peces=captura
peces=random.randint(pez1, pez2)

print(f"Tienes {pez1} que pesan menos de 800grs, y {pez2} que pesan mas de 801 grs")






