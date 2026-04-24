# Uso y explicacion de match

# print("1.- Opcion 1")
# print("1.- Opcion 2")
# print("1.- Opcion 3")
# op=int(input("Seleccione una opcion: "))
# match op:
#     case 1:
#         print("Selecciono la opcion 1")
#     case 2:
#         print("Selecciono la opcion 2")
#     case 3:
#         print("Selecciono la opcion 3")
#     case _:
#         print("Opcion invalida")


#---------------------------------------------------------------------------------------------------------

## MENU



# print("1.- Xbox Series S $250.000")
# print("2.- Sony PS5 $ $500.000")
# print("3.- LGTV 60 Pulgadad $600.000")
# print("4.- Salir")
# op=int(input("Seleccione una opcion: "))
# match op:
#     case 1:
#         print("El valor a pagar ", 250000*1.19)
#     case 2:
#         print("El valor a pagar ", 500000*1.19)
#     case 3:
#         print("El valor a pagar ", 600000*1.19)
#     case 4:
#         print("Saliendo...")
#     case _:
#         print("Opcion invalida")



#---------------------------------------------------------------------------------------------------------

## Menu while y match



# op=0
# total=0
# while op!=4:
#     print("1.- Xbox Series S $250.000")
#     print("2.- Sony PS5 $ $500.000")
#     print("3.- LGTV 60 Pulgadad $600.000")
#     print("4.- Salir")
#     op=int(input("Seleccione una opcion: "))
#     match op:
#         case 1:
#             print("El valor a pagar ", 250000*1.19)
#             total+=250000*1.19
#         case 2:
#             print("El valor a pagar ", 500000*1.19)
#             total+=500000*1.19
#         case 3:
#             print("El valor a pagar ", 600000*1.19)
#             total+=600000*1.19
#         case 4:
#             print("Saliendo...")
#             print(f"El total a pagar es {total}")
#         case _:
#             print("Opcion invalida")


#---------------------------------------------------------------------------------------------------------

# CALCULADORA
# + - * /

op=0
total=0

while op!=5:
     print("1.- Sumar")
     print("2.- Restar")
     print("3.- Multiplicar")
     print("4.- Dividir")
     print("5.- Salir")
     op=int(input("Seleccione una opcion: "))
     match op:
          case 1:
               s1=int(input("Ingrese un numero: "))
               s2=int(input("Ingrese un numero: "))
               print(f"La suma de {s1}+{s2} es = a {s1+s2}")

          case 2:
                r1=int(input("Ingrese un numero: "))
                r2=int(input("Ingrese un numero: "))
                print(f"La resta de {r1}-{r2} es = a {r1-r2}")

          case 3:
               m1=int(input("Ingrese un numero: "))
               m2=int(input("Ingrese un numero: "))
               print(f"La multiplicacion de {m1}X{m2} es = a {m1*m2}")

          case 4:
               d1=int(input("Ingrese un numero: "))
               d2=int(input("Ingrese un numero: "))
               print(f"La resta de {d1}/{d2} es = a {d1/d2}")

          case 5:
               print("Saliendo...")

          case _:
               print("Opcion no valida")