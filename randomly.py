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

