from commons.utlis import *


# def menu_principal():
#     limpiar_pantalla()
#     while True:
#         try:
#             eleccion_menu_principal=int(input(f"SISTEMA GESTOR DE PELICULAS BLOCKBUSTER\
#                                             1. Administrador de Generos\
#                                             2. Administrador de Actores\
#                                             3. Administrador de Formatos\
#                                             4. Gestor de Informes\
#                                             5. Gestor Peliculas\
#                                             6. Salir"))
#         except ValueError:
#             input("Ingresa un numero(Oprimir enter)")
#         else:
#             break
#     return eleccion_menu_principal
# def menu_generos():
#     limpiar_pantalla()
#     while True:
#         try:
#             eleccion_menu_generos=int(input(f"GESTOR DE GENEROS\
#                                              1. Crear genero\
#                                              2. Listar generos\
#                                              3. Ir Menu principal"))
#         except ValueError:
#             input("Ingresa un numero(Oprimir enter)")
#         else:
#             break
#     return eleccion_menu_generos
# def menu_actores():
#     limpiar_pantalla()
#     while True:
#         try:
#             eleccion_menu_actores=int(input(f"GESTOR DE ACTORES\
#                                              1. Crear Actor\
#                                              2. Listar Actores\
#                                              3. Salir"))
#         except ValueError:
#             input("Ingresa un numero(Oprimir enter)")
#         else:
#             break
#     return eleccion_menu_actores
# def menu_formato():
#     limpiar_pantalla()
#     while True:
#         try:
#             eleccion_menu_formato=int(input(f"GESTOR DE FORMATOS\
#                                              1. Crear Formato\
#                                              2. Listar Formatos\
#                                              3. Salir"))
#         except ValueError:
#             input("Ingresa un numero(Oprimir enter)")
#         else:
#             break
#     return eleccion_menu_formato
# def menu_peliculas():
#     limpiar_pantalla()
#     while True:
#         try:
#             eleccion_menu_peliculas=int(input("GESTOR DE PELICULAS\
#                                                1. Agregar Pelicula\
#                                                2. Editar Pelicula\
#                                                3. Eliminar Pelicula\
#                                                4. Eliminar Actor\
#                                                5. Buscar Pelicula\
#                                                6. Listar todas las peliculas\
#                                                7. Ir Menu principal"))
#         except ValueError:
#             input("Ingres un numero(Oprimir enter)")
#         else:
#             break
#     return eleccion_menu_peliculas   
# def menu_informes():
#      limpiar_pantalla()
#      while True:
#         try:
#             eleccion_menu_informes=int(input("GESTOR DE INFORMES\
#                                              1. Listar peliculas de un genero en especifico\
#                                              2. Listar las peliculas donde el protagonista sea Silvester Stallone\
#                                              3. Buscar Pelicula y mostrar sinopsis y actores\
#                                              4. Ir al menu Principal"))
#         except ValueError:
#             input("Ingres un numero(Oprimir enter)")
#         else:
#             break
#      return eleccion_menu_informes    


def menu_principal():
    limpiar_pantalla()
    while True:
        try:
            eleccion_menu_principal = int(input('''SISTEMA GESTOR DE PELÍCULAS BLOCKBUSTER
                                                1. Administrador de Géneros
                                                2. Administrador de Actores
                                                3. Administrador de Formatos
                                                4. Gestor de Informes
                                                5. Gestor Películas
                                                6. Salir: '''))
        except ValueError:
            input("Ingresa un número. Presiona Enter")
        else:
            break
    return eleccion_menu_principal

def menu_generos():
    limpiar_pantalla()
    while True:
        try:
            eleccion_menu_generos = int(input('''GESTOR DE GÉNEROS
                                                1. Crear Género
                                                2. Listar Géneros
                                                3. Ir al Menú Principal: '''))
        except ValueError:
            input("Ingresa un número. Presiona Enter")
        else:
            break
    return eleccion_menu_generos

def menu_actores():
    limpiar_pantalla()
    while True:
        try:
            eleccion_menu_actores = int(input('''GESTOR DE ACTORES
                                                1. Crear Actor
                                                2. Listar Actores
                                                3. Salir: '''))
        except ValueError:
            input("Ingresa un número. Presiona Enter")
        else:
            break
    return eleccion_menu_actores

def menu_formato():
    limpiar_pantalla()
    while True:
        try:
            eleccion_menu_formato = int(input('''GESTOR DE FORMATOS
                                                1. Crear Formato
                                                2. Listar Formatos
                                                3. Salir: '''))
        except ValueError:
            input("Ingresa un número. Presiona Enter")
        else:
            break
    return eleccion_menu_formato

def menu_peliculas():
    limpiar_pantalla()
    while True:
        try:
            eleccion_menu_peliculas = int(input('''GESTOR DE PELÍCULAS
                                                   1. Agregar Película
                                                   2. Editar Película
                                                   3. Eliminar Película
                                                   4. Eliminar Actor
                                                   5. Buscar Película
                                                   6. Listar Todas las Películas
                                                   7. Ir al Menú Principal: '''))
        except ValueError:
            input("Ingresa un número. Presiona Enter")
        else:
            break
    return eleccion_menu_peliculas

def menu_informes():
    limpiar_pantalla()
    while True:
        try:
            eleccion_menu_informes = int(input('''GESTOR DE INFORMES
                                                1. Listar películas de un género específico
                                                2. Listar las películas donde el protagonista sea Sylvester Stallone
                                                3. Buscar Película y mostrar sinopsis y actores
                                                4. Ir al Menú Principal: '''))
        except ValueError:
            input
