## Uso y explicacion de funciones

def saludo():
    print("Hola Maximo")
# saludo()

name="Monica"

def chao():
    print("Hola", name)

# chao()

def suma():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("Ingrese un numero: "))
    print(f"El resultado es {n1+n2}")
    
    suma()