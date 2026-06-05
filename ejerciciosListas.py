# crear lista de frutas y realizar todos estas operaciones
        # print("1.- Agregar Fruta:")
        # print("2.- Eliminar Fruta:")
        # print("3.- Actualizar Fruta:")
        # print("4.- Mostrar Frutas:")




# frutas=["Maracuya", "Pera"]

# def agregaFrutas():
#     print("-"*20)
#     nombreF=input("Ingrese el nombre de la Fruta: ")
#     frutas.append(nombreF)
#     print("-"*20)

# def eliminaFrutas():
#     print("-"*20)
#     muestraFrutas()
#     opc=int(input("Seleccione el numero de la fruta a eliminar: "))
#     frutas.pop(opc-1)
#     print("-"*20)

# def actualizaFrutas():
#     print("-"*20)
#     muestraFrutas()
#     opci=int(input("Seleccione el numero de la fruta a eliminar: "))
#     nuevaFruta=input("ingrese la nueva fruta: ")
#     frutas[opci-1]=nuevaFruta
#     print("-"*20)

# def muestraFrutas():
#     print("-"*20)
#     c=1
#     for f in frutas:
#         print(f"{c}.- {f}")
#         c+=1
#     print("-"*20)

# def feria():
#     while True:
#         print("1.- Agregar Fruta:")
#         print("2.- Eliminar Fruta:")
#         print("3.- Actualizar Fruta:")
#         print("4.- Mostrar Frutas:")
#         print("5.- Volver al menu principal")
#         op=int(input("Seleccione una opcion: "))
#         match op:
#             case 1:
#                 agregaFrutas()
#             case 2:
#                 eliminaFrutas()
#             case 3:
#                 actualizaFrutas()
#             case 4:
#                 muestraFrutas()
#             case 5:
#                 print("-"*20)
#                 print("Salir")
#                 print("-"*20)
#                 break
#             case _:
#                 print("-"*20)
#                 print("Opcion no valida")
#                 print("-"*20)

# feria()



#---------------------------------------------------------------------------------------------------------

# # Crear ima ñosta de 7 numeros no sucesivos
# # Mostrar el menor y el mayor de ellos

# nums=[15, 20, 67, 27, 420, 7 ,12]

# print(nums)
# nums.sort()
# print(nums)

# print(f"El numero mayor es {nums[-1]}")
# print(f"El numero menor es {nums[0]}")
# nums.reverse
# print(nums)

#---------------------------------------------------------------------------------------------------------


# # Crea una lista de productos con nombre y precio
# # Ordar pro precio de menor a mayor

# prods=[
#     ["pendrive", 8000],
#     ["HDMI 2.1", 13000],
#     ["Disco duro 1 TB", 35000],
#     ["Teclado", 15000]
# ]

# # for p in prods:
# #     print(p[0], "= $", p[1])
# # prods.sort(key=lambda p:p[1])
# # for p in prods:
# #     print(p[0], "= $", p[1])


# # Sumar el precio de todos los productos
# print(prods[2])
# total=0
# for p in prods:
#     total=total+p[1]

# print("El total de los productos es", total)


#---------------------------------------------------------------------------------------------------------

# notas=[4.6, 6.8, 4.1]

# def muestraNotas():
#     print("-"*20)
#     c=1
#     for f in notas:
#         print(f"{c}.- {f}.-")
#         c+=1
#     print("-"*30)

# def  agregaNotas():
#     n=float(input("Ingrese la nota: "))
#     notas.append(n)
#     print("Agregado correctamente")

# def muestracanNotas():
#     print(f"La cantidad de notas son {len(notas)}")

# def promedioNotas():
#     suma=0
#     for n in notas:
#         suma=suma+n
#     prom=suma/len(notas)
#     print(f"El promedio es {round(prom, 1)}")

# while True:
#     try:
#         print(''' 
# 1.- Agregar notas a la lista creada
# 2.- Muestre por pantalla todas las notas integradas
# 3.- Muestre la cantidad de notas ingresadas
# 4.- obtenga el promedio de las notas
# 5.- Salir''')
        
#         op=int(input("Seleccione una opcion"))
#         match op:
#             case 1:
#                 agregaNotas()
#             case 2:
#                 muestraNotas()
#             case 3:
#                 muestracanNotas()
#             case 4:
#                 promedioNotas()
#             case 5:
#                 print("Saliendo")
#                 break
#             case _:
#                 print("Opcion no valida")

#     except ValueError as e:
#         print("error", e)



#---------------------------------------------------------------------------------------------------------

# vegetales={

#   1:"maracuya",

#   2:"pera",

#   3:"cebolla",

#   7:"papa"



# }

# def agregavetal():

#   nombref=input("ingrese el nombre del vegetal")

#   vegetales[list(vegetales.items())[-1][0]+1]=nombref

# def muestravegetal():

#   for key, value in vegetales.items():

#     print(key, "-" , value)

#     print("-"*30)

# def eliminarvegetal():

#   muestravegetal()
#   borrar=int(input("Cual desea eliminar): "))
#   del vegetales[borrar]

# def actualizarvegetal():

#   muestravegetal()
#   actualiza=int(input("Cual desea actualizar?: "))
#   nuevo_vegetal=input("Cual es el nombre nuevo?: ")
#   vegetales[actualiza]=nuevo_vegetal

# def vegetalsssmenu():

#   while True:

#     try:

#       print("1.- agregar vegetal")

#       print("2.- eliminar vegetal")

#       print("3.- actualizar vegetal") 

#       print("4.- mostrar vegetal")

#       print("5.- salir")

#       op=int(input("seleccione una opcion: "))

#       match op:

#         case 1:

#           agregavetal()

#         case 2:

#           eliminarvegetal()

#         case 3:

#           actualizarvegetal()

#         case 4:

#           muestravegetal()

#         case 5:

#           print("salir")

#         case _:

#           print()

#     except:

#       print("error, intente denuevo")

# # vegetalsmenu()

# print(list(vegetales.items())[-1])




