# crear lista de frutas y realizar todos estas operaciones
        # print("1.- Agregar Fruta:")
        # print("2.- Eliminar Fruta:")
        # print("3.- Actualizar Fruta:")
        # print("4.- Mostrar Frutas:")




frutas=["Maracuya", "Pera"]

def agregaFrutas():
    print("-"*20)
    nombreF=input("Ingrese el nombre de la Fruta: ")
    frutas.append(nombreF)
    print("-"*20)

def eliminaFrutas():
    print("-"*20)
    muestraFrutas()
    opc=int(input("Seleccione el numero de la fruta a eliminar: "))
    frutas.pop(opc-1)
    print("-"*20)

def actualizaFrutas():
    print("-"*20)
    muestraFrutas()
    opci=int(input("Seleccione el numero de la fruta a eliminar: "))
    nuevaFruta=input("ingrese la nueva fruta: ")
    frutas[opci-1]=nuevaFruta
    print("-"*20)

def muestraFrutas():
    print("-"*20)
    c=1
    for f in frutas:
        print(f"{c}.- {f}")
        c+=1
    print("-"*20)

def feria():
    while True:
        print("1.- Agregar Fruta:")
        print("2.- Eliminar Fruta:")
        print("3.- Actualizar Fruta:")
        print("4.- Mostrar Frutas:")
        print("5.- Volver al menu principal")
        op=int(input("Seleccione una opcion: "))
        match op:
            case 1:
                agregaFrutas()
            case 2:
                eliminaFrutas()
            case 3:
                actualizaFrutas()
            case 4:
                muestraFrutas()
            case 5:
                print("-"*20)
                print("Salir")
                print("-"*20)
                break
            case _:
                print("-"*20)
                print("Opcion no valida")
                print("-"*20)

feria()



#---------------------------------------------------------------------------------------------------------