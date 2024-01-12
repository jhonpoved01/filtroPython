# import json
# from commons.menus import *

# def crear_genero(generos):
#     limpiar_pantalla()
#     genero=True
#     while genero:
#         try:
#             identificacion=int(input(f"Ingresa el codigo con el que quieres identificar el genero(numero)\n"))
#         except ValueError:
#             print("Ingresa un numero")
#         else:
#             identificacion="G"+str(identificacion)
#             conteo=0
#             for i in generos:
#                 if i==identificacion:
#                     print(f"Este genero ya existe\n Id: {i} Nombre: {generos[i]['nombre']}")
#                     conteo=1
#             if conteo==0:
#                 genero=False
    
#     nombreGenero=str(input("Ingrese el nombre del genero que desea crear\n"))
#     generos[identificacion]=dict([("id", identificacion), ("nombre", nombreGenero)])
#     input(f"Se creo el genero {generos[identificacion]['nombre']} con el codigo {identificacion}\nOprime Enter")
#     with open("generos.json","w+") as f:
#         f.write(json.dumps(generos, indent=4))
# def listar_generos(generos):
#     limpiar_pantalla()
#     print("Los generos ingresados al sistema son:")
#     for i in generos:
#         print(f"Id: {i}     Nombre del genero: {generos[i]['nombre']}")
#     input("Oprime Enter Para Salir")

import json
from commons.menus import *


def crear_genero(generos):
    limpiar_pantalla()
    while True:
        try:
            identificacion = int(input("Ingresa el código con el que quieres identificar el género (número): "))
            identificacion = f"G{identificacion}"
        except ValueError:
            print("Ingresa un número válido.")
        else:
            if identificacion not in generos:
                break
            else:
                print(f"Este género ya existe. Id: {identificacion} Nombre: {generos[identificacion]['nombre']}")

    nombre_genero = input("Ingrese el nombre del género que desea crear: ")
    generos[identificacion] = {"id": identificacion, "nombre": nombre_genero}
    
    with open("generos.json", "w") as f:
        json.dump(generos, f, indent=4)
    
    input(f"Se creó el género {nombre_genero} con el código {identificacion}\nPresiona Enter")

def listar_generos(generos):
    limpiar_pantalla()
    print("Los géneros ingresados al sistema son:")
    for identificacion, info_genero in generos.items():
        print(f"Id: {identificacion}     Nombre del género: {info_genero['nombre']}")
    input("Presiona Enter para salir")
