# from commons.menus import *
# from commons.utlis import*
# from blockbuster.actores import *
# def load_actores_json():
#     limpiar_pantalla()
#     op=menu_principal()
#     if op==1:
#        Administracion_de_generos()
#        input("Presiona cualquier tecla para continuar: ")
#     if op==2:
#        Administracion_de_actores()
#        input("Presiona cualquier tecla para continuar: ")
#     if op==3:
#        Administracion_de_formatos()
#        input("Presiona cualquier tecla para continuar: ")
#     if op==4:
#         gestor_de_informes()
#         input("Presiona cualquier tecla para continuar: ")
#     if op==5:
#         gestor_de_peliculas()
#         input("Presiona cualquier tecla para continuar: ")

# from blockbuster.actores import *
# from blockbuster.formatos import *
# from blockbuster.generos import *
# from blockbuster.informes import buscar_peliculas_sinopsis, listar_actor_especifico, listar_generos_especifico
# from blockbuster.peliculas import *
# from commons.menus import *
# from commons.utlis import*
# import json

# generos={}
# actores={}
# formatos={}
# peliculas={}
# informes={}

# with open("generos.json", "r") as f:
#     generos=json.loads(f.read())
# with open("actores.json","r") as a:
#     actores=json.loads(a.read())
# with open("formatos.json","r") as j:
#     formatos=json.loads(j.read())
# while True:
    
#     limpiar_pantalla()
#     eleccion_menu_principal=menu_principal()
#     if eleccion_menu_principal==1:
#         while True:
#             with open("generos.json", "r") as f:
#                 generos=json.loads(f.read())
#             eleccion_menu_generos=menu_generos()
#             if eleccion_menu_generos==1:
#                 crear_genero(generos)
#             elif eleccion_menu_generos==2:
#                 listar_generos(generos)
#             elif eleccion_menu_generos==3:
#                 break
#             else:
#                 input("Ingresa un numero dentro de las opciones(Oprime Enter)")
#     elif eleccion_menu_principal==2:
#         limpiar_pantalla()
#         while True:
#             with open("actores.json","r") as a:
#                 actores=json.loads(a.read())
#             eleccion_menu_actores=menu_actores()
#             if eleccion_menu_actores==1:
#                 crear_actor(actores)
#             elif eleccion_menu_actores==2:
#                 listar_actores(actores)
#             elif eleccion_menu_actores==3:
#                 break
#             else:
#                 input("Ingresa un numero dentro de las opciones(Oprime Enter)")
#     elif eleccion_menu_principal==3:
#         limpiar_pantalla()
#         while True:
#             with open("formatos.json","r") as j:
#                 formatos=json.loads(j.read())
#             eleccion_menu_formatos=menu_formato()
#             if eleccion_menu_formatos==1:
#                 crear_formato(formatos)
#             elif eleccion_menu_formatos==2:
#                 listar_formatos(formatos)
#             elif eleccion_menu_formatos==3:
#                 break
#             else:
#                 input("Ingresa un numero dentro de las opciones(Oprime Enter)")
#     elif eleccion_menu_principal==5:
#         limpiar_pantalla()
#         while True:
#             with open("peliculas.json","r") as p:
#                 peliculas=json.loads(p.read())
#             eleccion_menu_peliculas=menu_peliculas()
#             if eleccion_menu_peliculas==1:
#                 crear_pelicula(peliculas, generos, formatos, actores)
#             elif eleccion_menu_peliculas==2:
#                 editar_peliculas(peliculas, generos, formatos, actores)
#             elif eleccion_menu_peliculas==3:
#                 eliminar_pelicula(peliculas)
#             elif eleccion_menu_peliculas==4:
#                 eliminar_actor(peliculas)
#             elif eleccion_menu_peliculas==5:
#                 buscar_pelicula(peliculas)
#             elif eleccion_menu_peliculas==6:
#                 listar_peliculas(peliculas)
#             elif eleccion_menu_peliculas==7:
#                 break
#             else:
#                 input("Selecciona alguna de las opciones(Oprime enter)")
#     elif eleccion_menu_principal==4:
#         limpiar_pantalla()
#         while True:
#             eleccion_menu_informes=menu_informes()
#             if eleccion_menu_informes==1:
#                 listar_generos_especifico(peliculas, generos)
#             elif eleccion_menu_informes==2:
#                 listar_actor_especifico(peliculas)
#             elif eleccion_menu_informes==3:
#                 buscar_peliculas_sinopsis(peliculas)
#             elif eleccion_menu_informes==4:
#                 break
#             else:
#                 input("Selecciona alguna de las opciones(Oprime enter)")


# from blockbuster.actores import *
# from blockbuster.formatos import *
# from blockbuster.generos import *
# from blockbuster.informes import buscar_peliculas_sinopsis, listar_actor_especifico, listar_generos_especifico
# #from blockbuster.peliculas import *

# from commons.menus import *
# from commons.utlis import *
# from data import *
# from data import json 
# Leer datos de los archivos JSON
# import json
# from blockbuster.actores import *
# from blockbuster.formatos import *
# from blockbuster.generos import *
# from blockbuster.informes import buscar_peliculas_sinopsis, listar_actor_especifico, listar_generos_especifico
# #from blockbuster.peliculas import *
# from commons.menus import *
# from commons.utlis import *

# Leer datos de los archivos JSON
# with open("data/generos.json", "r") as f:
#     generos = json.loads(f.read())

# with open("data/actores.json", "r") as a:
#     actores = json.loads(a.read())

# with open("data/formatos.json", "r") as j:
#     formatos = json.loads(j.read())

# with open("data/peliculas.json", "r") as p:
#     peliculas = json.loads(p.read())

# Resto del código...




# with open("generos.json", "r") as f:
#     generos = json.loads(f.read())

# with open("actores.json", "r") as a:
#     actores = json.loads(a.read())

# with open("formatos.json", "r") as j:
#     formatos = json.loads(j.read())

# with open("peliculas.json", "r") as p:
#     peliculas = json.loads(p.read())


import os
import json
from blockbuster.actores import *
from blockbuster.formatos import *
from blockbuster.generos import *
from blockbuster.informes import buscar_peliculas_sinopsis, listar_actor_especifico, listar_generos_especifico
from blockbuster.peliculas import editar_peliculas, eliminar_pelicula, eliminar_actor, buscar_pelicula, listar_peliculas, crear_pelicula
from commons.menus import *
from commons.utlis import *


current_directory = os.path.dirname(os.path.abspath(__file__))


generos_path = os.path.join(current_directory, "data", "generos.json")
actores_path = os.path.join(current_directory, "data", "actores.json")
formatos_path = os.path.join(current_directory, "data", "formatos.json")
peliculas_path = os.path.join(current_directory, "data", "peliculas.json")


with open("data","generos_path", "r") as f:
    generos = json.loads(f.read())

with open("data","actores.json", "r") as a:
    actores = json.loads(a.read())

with open("data","formatos.json", "r") as j:
    formatos = json.loads(j.read())

with open("data","peliculas.json", "r") as p:
    peliculas = json.loads(p.read())



while True:
    limpiar_pantalla()
    eleccion_menu_principal = menu_principal()

    if eleccion_menu_principal == 1:
        while True:
            eleccion_menu_generos = menu_generos()
            if eleccion_menu_generos == 1:
                crear_genero(generos)
            elif eleccion_menu_generos == 2:
                listar_generos(generos)
            elif eleccion_menu_generos == 3:
                break
            else:
                input("Ingresa un numero dentro de las opciones (Oprime Enter)")

    elif eleccion_menu_principal == 2:
        limpiar_pantalla()
        while True:
            eleccion_menu_actores = menu_actores()
            if eleccion_menu_actores == 1:
                crear_actor(actores)
            elif eleccion_menu_actores == 2:
                listar_actores(actores)
            elif eleccion_menu_actores == 3:
                break
            else:
                input("Ingresa un numero dentro de las opciones (Oprime Enter)")

    elif eleccion_menu_principal == 3:
        limpiar_pantalla()
        while True:
            eleccion_menu_formatos = menu_formato()
            if eleccion_menu_formatos == 1:
                crear_formato(formatos)
            elif eleccion_menu_formatos == 2:
                listar_formatos(formatos)
            elif eleccion_menu_formatos == 3:
                break
            else:
                input("Ingresa un numero dentro de las opciones (Oprime Enter)")

    elif eleccion_menu_principal == 5:
        limpiar_pantalla()
        while True:
            eleccion_menu_peliculas = menu_peliculas()
            if eleccion_menu_peliculas == 1:
                crear_pelicula(peliculas, generos, formatos, actores)
            elif eleccion_menu_peliculas == 2:
                editar_peliculas(peliculas, generos, formatos, actores)
            elif eleccion_menu_peliculas == 3:
                eliminar_pelicula(peliculas)
            elif eleccion_menu_peliculas == 4:
                eliminar_actor(peliculas)
            elif eleccion_menu_peliculas == 5:
                buscar_pelicula(peliculas)
            elif eleccion_menu_peliculas == 6:
                listar_peliculas(peliculas)
            elif eleccion_menu_peliculas == 7:
                break
            else:
                input("Selecciona alguna de las opciones (Oprime enter)")

    elif eleccion_menu_principal == 4:
        limpiar_pantalla()
        while True:
            eleccion_menu_informes = menu_informes()
            if eleccion_menu_informes == 1:
                listar_generos_especifico(peliculas, generos)
            elif eleccion_menu_informes == 2:
                listar_actor_especifico(peliculas)
            elif eleccion_menu_informes == 3:
                buscar_peliculas_sinopsis(peliculas)
            elif eleccion_menu_informes == 4:
                break
            else:
                input("Selecciona alguna de las opciones (Oprime enter)")
