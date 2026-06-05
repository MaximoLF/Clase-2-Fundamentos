
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

# # print(list(vegetales.items())[-1])

#---------------------------------------------------------------------------------------------------------

# productosDicc={
#   1:{"nombre": "Maracuya", "precio": 3000},
#   2:{"nombre": "Pera", "precio": 1500},
#   3:{"nombre": "Cebolla", "precio": 1200}
# }

# (productosDicc[2]["precio"]) # Precio de la Pera
# (productosDicc[3]["precio"]) # Precio de la Cebolla


# productosList={
#   1:{"nombre": "Maracuya", "precio": 3000},
#   2:{"nombre": "Pera", "precio": 1500},
#   3:{"nombre": "Cebolla", "precio": 1200}
# }

# print(productosList[2]["precio"]) # Precio de la Cebolla
# print(productosList[0]["nombre"]) # Nombre del Maracuya

#---------------------------------------------------------------------------------------------------------




productosList=[
    ["Maracuya", 3000],
    ["Maracuya", 1500],
    ["Maracuya", 1200]
]

total=0

def muestraProdcutos():
    print("-"*20)
    c=1
    for f in productosList:
        print(f"{c}.- {f}")
        c+=1
    print("-"*20)

def boleta():
    
    print(f"El total de su compra es de {total}")

while True:
    try:
        print("1.- Comprar:")
        print("2.- Crear Boleta")
        print("3.- Salir:")
        op=int(input("Seleccione una opcion: "))
        match op:
            case 1:
                muestraProdcutos()
                sel=int(input("Seleccione un producto para agregar: "))
                total=sel+total

            case 2:
                boleta()
            case 3:
                print("-"*20)
                print("Salir")
                print("-"*20)
                break
            case _:
                print("-"*20)
                print("Opcion no valida")
                print("-"*20)

    except ValueError as e:
        print("error", e)




