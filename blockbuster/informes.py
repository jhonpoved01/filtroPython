# from commons.menus import *

# def listar_generos_especifico(peliculas, generos):
#     print("Escribe el Id del genero que deseas listar")
#     for i in generos:
#         print(f"Id: {i}     Nombre del genero: {generos[i]['nombre']}")
#     eleccion_genero=str(input())
#     for i in peliculas:
#         for j in peliculas[i]["generos"]:
#             print (j)
#             if eleccion_genero==j:
#                 print(f"Id: {i} Nombre: {peliculas[i]['nombre']}")
#     input("Oprimir enter")
# def listar_actor_especifico(peliculas):
#     for i in peliculas:
#         for j in peliculas[i]["actores"]:
#             if "A1"==j:
#                 print(f"Id: {i} Nombre: {peliculas[i]['nombre']}")
#     input("Oprimir enter")
# def buscar_peliculas_sinopsis(peliculas):
#     print("Escribe el Id de la pelicula que deseas saber su sinopsis y los actores")
#     for i in peliculas:
#         print(f"Id: {i}     Nombre del genero: {peliculas[i]['nombre']}")
#     eleccion_pelicula=str(input())
#     correcto=0
#     for i in peliculas:
#         if eleccion_pelicula==i:
#             correcto=1    
#     if correcto==1:
#         print(f"Sinopsis: {peliculas[eleccion_pelicula]['Sinopsis']} Actores: {peliculas[eleccion_pelicula]['Actores']}")
#     input("Oprimir enter")

from commons.menus import *

def imprimir_generos(generos):
    for i in generos:
        print(f"Id: {i}     Nombre del género: {generos[i]['nombre']}")

def listar_generos_especifico(peliculas, generos):
    print("Escribe el Id del género que deseas listar")
    imprimir_generos(generos)
    eleccion_genero = str(input())
    for i in peliculas:
        for j in peliculas[i]["generos"]:
            if eleccion_genero.lower() == j.lower():
                print(f"Id: {i} Nombre: {peliculas[i]['nombre']}")
    input("Oprimir Enter")

def listar_actor_especifico(peliculas, actor_id="A1"):
    for i in peliculas:
        for j in peliculas[i]["actores"]:
            if actor_id == j:
                print(f"Id: {i} Nombre: {peliculas[i]['nombre']}")
    input("Oprimir Enter")

def buscar_peliculas_sinopsis(peliculas):
    print("Escribe el Id de la película que deseas saber su sinopsis y los actores")
    for i in peliculas:
        print(f"Id: {i}     Nombre de la película: {peliculas[i]['nombre']}")
    eleccion_pelicula = str(input())
    if eleccion_pelicula in peliculas:
        print(f"Sinopsis: {peliculas[eleccion_pelicula]['Sinopsis']} Actores: {peliculas[eleccion_pelicula]['Actores']}")
    else:
        print("Película no encontrada.")
    input("Oprimir Enter")
