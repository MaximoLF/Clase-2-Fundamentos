# n=" Pedro"
# name= "Maximo Lorca"
# #    -3-2-1
# nom= "Eva"
# #     012
# print(name[0])
# print(len(name))
# print(n.strip()) # Borrar espacio
# print(name.upper()) # Hacer todo mayuscula
# # name=name.lower() # Reasignando el valor a la variable
# print(name.lower()) # Hacer todo minuscula
# print(name.replace("Lorca", "Font")) # Remplazar
# print(name.split()) # Hacerlo tipo lista


#----------------------------------------------------------------------------------------------------------------------------

# PEDIR CLAVE AL USUARIO Y VERIFICAR QUE SEA "SHAZAM"

# clave="SHAZAM" or "shazam"
# contraseña=input ("Ingrese la contraseña: ")
# if contraseña==clave:
#     print("Acceso Otorgado")
# else:
#     print("Acceso denegado")



#----------------------------------------------------------------------------------------------------------------------------

# INGRESAR NOMBRE DE USUARIO Y QUE TENGA DE 4 A 10 CARACTERES

# user=input("Ingrese un nombre de usuario: ")

# if len(user)<4:
#     print("Debe tener al menos 4 caracteres")
# elif len(user)>10:
#     print("Error, tiene mas de 10 caracteres")
# else:
#     print("Usuario creado correctamente")


#----------------------------------------------------------------------------------------------------------------------------

# CREAR UN PIN Y QUE TENGA EXACTAMENTE 4 DIGITOS

pin=int(input("Ingrese su pin: "))
if len(str(pin))==4:
    print("Pin creado")
else:
    print("El pin debe ser de 4 digitos")

