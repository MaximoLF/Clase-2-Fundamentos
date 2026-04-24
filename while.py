# Uso o y explicacion de while

# cont=1
# while cont<=3:
#     print("Repeticion ", cont)
#     cont+=1


# Ingrese PIN

pin=3242
baka=int(input("Ingrese su pin: "))
while pin!=baka:
    print("Pin incorrecto, intenta de nuevo")
    baka=int(input("Ingrese su pin: "))
print("Pin correcto")


#---------------------------------------------------------------------------------------------------------


# While y match

op=0
total=0
while op!=4:
    print("1.- Xbox Series S $250.000")
    print("1.- Sony PS5 $ $500.000")
    print("1.- LGTV 60 Pulgadad $600.000")
    print("4.- Salir")
    op=int(input("Seleccione una opcion: "))
    match op:
        case 1:
            print("El valor a pagar ", 250000*1.19)
            total+=250000*1.19
        case 2:
            print("El valor a pagar ", 500000*1.19)
            total+=500000*1.19
        case 3:
            print("El valor a pagar ", 600000*1.19)
            total+=600000*1.19
        case 4:
            print("Saliendo...")
            print(f"El total a pagar es {total}")
        case _:
            print("Opcion invalida")