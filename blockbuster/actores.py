# import json
# from commons.utlis import *


# def crear_actor(actores):
#         limpiar_pantalla()
#         actor=True
#         while actor:
#             try:
#                 identificacion=int(input(f"Ingresa el codigo con el que quieres identificar el actor(numero)\n"))
#             except ValueError:
#                 print("Ingresa un numero")
#             else:
#                 identificacion="A"+str(identificacion)
#             conteo=0
#             for i in actores:
#                 if i==identificacion:
#                     print(f"Este Actor ya existe\n Id: {i} Nombre: {actores[i]['nombre']}")
#                     conteo=1
#             if conteo==0:
#                 actor=False
   
#         nombre_actor=str(input("Ingrese el nombre completo del actor que desea ingresar al sistema\n"))  
#         actores[identificacion]=dict([("id", identificacion), ("nombre", nombre_actor)])
#         input(f"Se creo al Actor {nombre_actor} con el codigo {identificacion}\n Oprime Enter")
#         with open("actores.json","w+") as a:
#              a.write(json.dumps(actores, indent=4))

# def listar_actores(actores):
#     limpiar_pantalla()
#     print("Los actores ingresados al sistema son:")
#     for i in actores:
#         print(f"Id: {i}       Actor: {actores[i]['nombre']}")
#     input("Oprime enter para salir")

import json
from commons.utlis import limpiar_pantalla


def crear_actor(actores):
    limpiar_pantalla()
    actor = True
    while actor:
        try:
            identificacion = int(input("Ingresa el código con el que quieres identificar el actor (número)\n"))
        except ValueError:
            print("Ingresa un número")
        else:
            identificacion = "A" + str(identificacion)
            conteo = 0
            for actor_id in actores:
                if actor_id == identificacion:
                    print(f"Este Actor ya existe\n Id: {actor_id} Nombre: {actores[actor_id]['nombre']}")
                    conteo = 1
            if conteo == 0:
                actor = False

    nombre_actor = input("Ingrese el nombre completo del actor que desea ingresar al sistema\n")
    actores[identificacion] = {"id": identificacion, "nombre": nombre_actor}
    input(f"Se creó al Actor {nombre_actor} con el código {identificacion}\n Oprime Enter")
    
    with open("actores.json", "w+") as file:
        json.dump(actores, file, indent=4)

def listar_actores(actores):
    limpiar_pantalla()
    print("Los actores ingresados al sistema son:")
    for actor_id in actores:
        print(f"Id: {actor_id}       Actor: {actores[actor_id]['nombre']}")
    input("Oprime enter para salir")
