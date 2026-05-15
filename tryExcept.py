# while True:
#     try:
#         num=int(input("ingrese un numero: "))
#     except:
#         print("solo numeros enteros")
#     break

   

# while True:
#     n=input("ingrese su nombre")



# op=0
# total=0
  
# while op!=4:
#     try:
#      print("1.- xbox series s $250.000")
#      print("2.- sony ps5 s $500.000")
#      print("3.- lgtv 60 pulgadas s $600.000")
#      print("4.- salir ")
#      op=int(input("selecione una opcon: "))
     
#     except:
#      print("SOLO SE ACEPTAN NUMEROS ENTEROS")

#     match op:
#       case 1:
#          print("el valor a pagar", 250000*1.19)
#          total+=250000*1.19
#       case 2:
#          print("el valor a pagar", 500000*1.19)
#          total+=500000*1.19
#       case 3:
#          print("el valor a pagar", 600000*1.19)
#          total+=600000*1.19
#       case 4:
#          print("saliendo...")
#          print(f"el total a pagar es {total}")
#       case _:
#         print("opcion invalida")





# notas=int(input("INGRESE LA CANTIDAD DE NOTAS: "))
# suma=0
# for i in range(notas):
#   n=float(input(f"ingrese la nota {i+1}: "))
#   suma=suma+n
# #   suma+=n
# prom=suma/notas
# prin("el promedio es", round(prom,1))

# if prom>=4:
#   print("alumno aprobado")
# else:
#   print("alumno reprobado")



# op=0
# total=0
# while op!=4:
#     try:  
#      print("1.- PC $500.000")
#      print("2.- LGTV 55 pulgadas $450.000")
#      print("3.- Microondas Mademsa $100.000")
#      print("4.- Salir")
#      print("Seleccione una opcion")
#     op=int(input())
#     match op:
#         case 1:
#             print("El total a pagar es ",500000*1.19 )
#             total+=500000*1.19
#         case 2:
#             print("El total a pagar es ",450000*1.19 )
#             total+=450000*1.19
#         case 3:
#             print("El total a pagar es ",100000*1.19 )
#             total+=100000*1.19
#         case 4:
#             print("Saliendo")
#             print("El total a pagar es", total)
#         case _:
#             print("Opción inválida")




# ___________________________________________________________________________________________________________________________________

# Pedir al usuario la cantidad d notas 
# mostrar el premedio de ellas
# determinar si el alumno aprueba o no
   





while True:
    try: 
        num=int(input("ingrese un numero: ")) 
        break
    except:
        print("solo numeros enteros ")

       



notas=int(input("Ingrese la cant de notas: "))
suma=0
for i in range(notas):
       n=float(input(f"Ingrese la nota {i+1}: "))
       suma=suma+n
    # suma+=n
prom=suma/notas
print("El promedio es",round(prom,1) )

if prom>=4:
    print("Alumno aprobado")
else:
    print("Alumno reprobado")