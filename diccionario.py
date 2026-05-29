productos=[
    ["Xbox Series S", 300000],
    ["Sony PS5", 600000],
    ["LGTV 60 Pulgadas", 450000]
]

def menuProd():
    select=1
    for p in productos:
        print(f"{select}.- Producto: {p[0]} Precio: ${p[1]}")
        select+=1


def menuPrincipal():
    print("1.- Menu admin")
    print("2.- Menu Cliente")
    print("3.- Salir")

op=0


def selecProd():
    total=0
    while True:
          match op:
            case 1:
                print("El total a pagar es ",300000*1.19 )
                total+=300000*1.19
            case 2:
                print("El total a pagar es ",600000*1.19 )
                total+=600000*1.19
            case 3:
                print("El total a pagar es ",450000*1.19 )
                total+=450000*1.19
            case 4:
                print("Saliendo")
                print("El total a pagar es", total)
            case _:
                print("Opción inválida")

def selectAdmin():
    while True:
        print("1.- Agregar Producto:")
        print("2.- Eliminar Producto:")
        print("3.- Actualizar Producto:")
        print("4.- Mostrar Producto:")
        print("5.- Volver al menu principal")
        op=int(input("Seleccione una opcion: "))
        match op:
            case 1:
                nombreP=input("Ingrese el nombre del producto: ")
                precioP=int(input("Ingrese el precio del producto: "))
                productos.append([nombreP, precioP])
            case 4:
                menuProd()
            case 5:
                print("Salir")
                break
            case _:
                print("Opcion no valida")



def selectPrin():
    while True:
        menuPrincipal()
        op=int(input("Seleccione una opcion: "))
        match op:
            case 1:
                print("---Menu Admin---")
                selectAdmin()
            case 2:
                print("---Menu Cliente---")
                selecProd()
            case 3:
                print("Salir")
                break
            case _:
                print("Opcion no valida")
                
selectPrin()