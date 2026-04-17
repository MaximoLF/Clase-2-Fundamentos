# explicacion y uso del for

# for i in range(3): # En el parentesis poner la cantidad de veces que se repite
#     print("hola") 

#---------------------------------------------------------------------------------------------------------b

# num=int(input("Ingrese un numero ")) # Para ingresar una variable, en este caso para elegir el  numero

# for i in range(num):
#     print(i+1, "Repeticion") # i es para mostrar la cantidad de repeticiones

# print("Segunda forma")
# for i in range(1,num+1): 
#     print(i, "Repeticion") 

#---------------------------------------------------------------------------------------------------------

# Pedir un numero al usuario y 
# mostrar su tabla de multiplicar

# num=int(input("Ingrese un numero "))

# # Primera forma

# for i in range(10): 
#     print(f"{num}x{i+1}={num*(i+1)}") # Aqui no se ocupan comas y lo que este fuera de {} lo toma como texto

# # Segunda forma

# for i in range(10): # Seria la cantidad de multiplicaciones
#     print(num, "x", i+1, "=", num*i ) # num (numero ingresado), i+1 (Contador), num*i (Numero X contador)

#---------------------------------------------------------------------------------------------------------

# Preguntar cuantas notas son y sacar el promedio de ellas


# num=int(input("Ingres la cantidad de notas: ")) # Cantidad de notas
# suma=0
# for i in range(num): 
#     n=float(input("Ingrese la nota: ")) # Ingresa las notas
#     suma=suma+n
# prom=suma/num # num (cantidad de notas)
# print(f"El promedio es {prom}")

# if prom>=4:
#     print("Almuno Aprobado")
# else:
#     print("Almno Reprobado")

#---------------------------------------------------------------------------------------------------------

# Sumatoria 

# num=int(input("Ingres un numero: "))
# total=0
# for i in range(num):
#     total=total+i+1
# print("La sumatoria es: ", total) # Si pongo un 3 | 1+2+3=6 y si pongo un 4// 1+2+3+4=10


# Factorial

# num=int(input("Ingres un numero: "))
# total=1
# for i in range(num):
#     total=total*(i+1)
# print("La sumatoria es: ", total)


#---------------------------------------------------------------------------------------------------------


# for i in "Maximo":  #Repetira la cantidad de letras, cuando termine de recorrer el objeto fin | Si "Hola" tiene 4 letras se repetira 4 veces
#     print(i)

# Letras

# letras=0
# nombre=input("Ingrese una palabra: ") #Palabra ingresada
# for i in nombre:
#     print(i)
#     letras=letras+1
# print(f"El total de letras es {letras}") # Contador de letras


# Vocales


# vocales=0
# nombre=input("Ingrese una palabra: ") #Palabra ingresada
# for i in nombre:
#     print(i)
#     if i in "aeiouAEIOU": # Letras que contara
#         # vocales=vocales+1
#         vocales+=1 # Lo mismo de arriba
# print(f"El total de vocales es {vocales}") 

# Vocales y consonantes

# vocales=0
# conso=0
# nombre=input("Ingrese una palabra: ") #Palabra ingresada
# for i in nombre:
#     print(i)
#     if i in "aeiouAEIOU": # Letras que contara
#         vocales+=1
#     elif i ==" ":
#         ''''''
#     else:
#         conso+=1
# print(f"El total de vocales es {vocales}") 
# print(f"El total de consonantes es {conso}") 

#---------------------------------------------------------------------------------------------------------

alumnos=int(input("Cuantos alumnos son?: ")) # Cantidad de alumnos
for j in range(alumnos): 

    notas=int(input(f"Ingres la cantidad de notas del almuno {j+1}: ")) # Cantidad de notas
    suma=0
    for i in range(notas): 
        n=float(input(f"Ingrese la nota {i+1}: ")) # Ingresa las notas
        suma=suma+n
    prom=suma/notas # num (cantidad de notas)
    print(f"El promedio es {prom}")

    if prom>=4:
        print("Almuno Aprobado")
    else:
        print("Almno Reprobado")