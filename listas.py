# # Ejemplo y uso de listas


# #     -5  -4  -3 -2  -1
# lista=[4, 7, 9, 2, 3.8]
# #       0  1  2  3   4

# print(lista)
# print(lista[4])

# name="LINK"

# # for i in name:
# #     print(i)

# for i in lista:
#     print(i)

#--------------------------------------------------------------------------------------------

# Crear una lista de 4 frutas y mostrarlas en la pantalla

# frutas=["Manzana", "Platano", "Naranja", "Uva"]
# ccVocal=0
# for i in frutas:
#     if i[0].lower() in ("aeiou"):
#         print("La fruta es ", i, " Comienza con vocal")
#         ccVocal+=1
#     else:
#         print("La fruta es ", i)
# print("Total de frutas que inician con vocal: ", ccVocal)


#--------------------------------------------------------------------------------------------

# # Cree una lista con 3 nombres
# # Crear otra lista con 3 apellidos
# # Mostrar ambos por pantalla

# nombres=["Maximo", "Paola", "Jorge",]
# apellidos=["Lorca", "Font", "Bucksbaum"]

# for i in range(len(apellidos)):
#     print(nombres[i], apellidos[i])

# nombres.append("Jorgito") # Agregar nombres a la lista
# apellidos.append("Lorca") # Agregar nombres a la lista

# for i in range(len(apellidos)):
#     print(nombres[i], apellidos[i])


#--------------------------------------------------------------------------------------------

# # Crear una lista de animales con 3 elementos
# # Agregue 2 mas y muestre el resultado de la misma

# animales=["Gato", "Perro", "Pato"]

# animales.append("Conejo")
# animales.append("Koala")

# for i in range(len(animales)):
#     print(animales[i])



#--------------------------------------------------------------------------------------------

# # Diccionario

# alumno={    
#     "nombre:":"Huevito Rey",
#     "carrera:": "Informatica",
#     "edad:": "20"
# }

# # Recorrer cada elemento de un diccionario
# print(alumno)
# for key, value in alumno.items():
#     print(key, value)

# # Buscas
# print(alumno["nombre:"])

# # Insssersion
# alumno["email"]="huevitorey@gmail.com"

# # Actualizacion

# alumno["edad:"]=25

# # Eliminacion

# del alumno["carrera:"]

# print(alumno)
# for key, value in alumno.items():
#     print(key, value)

#--------------------------------------------------------------------------------------------

# Cree un diccionario de 3 productos, cada uno con nombre, categoria y precio.

productos={
    1:{"nombre": "Laptop",
       "categoria": "Electronica",
       "precio": 40000},
    2:{"nombre": "Chaleco",
       "categoria": "Ropa",
       "precio": 15000},
    3:{"nombre": "Celular",
       "categoria": "Electronica",
       "precio": 451000},
}


print(productos[2]["precio"])


