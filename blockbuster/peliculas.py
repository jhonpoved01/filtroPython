# import json
# from commons.menus import *
# from commons.utlis import *

# def crear_pelicula(peliculas, generos, formatos, actores):
#     limpiar_pantalla()
#     peliculas=True
#     while peliculas:
#         try:
#             identificacion=int(input(f"Ingresa el codigo con el que quieres identificar la pelicula(numero)\n"))
#         except ValueError:
#             print("Ingresa un numero")
#         else:
#             identificacion="P"+str(identificacion)
#             conteo=0
#             for i in peliculas:
#                 if i==identificacion:
#                     print(f"Esta Pelicula ya existe\n Id: {i} Nombre: {peliculas[i]['nombre']}") 
#                     conteo=1
#             if conteo==0:
#                 peliculas=False
#     peliculas[identificacion]=dict([("Id", identificacion)]) 
#     limpiar_pantalla()
#     nombre_pelicula=str(input("Ingresa el nombre de la pelicula que quieres agregar al sistema\n"))
#     peliculas[identificacion]["Nombre"]= nombre_pelicula
#     while True:
#         limpiar_pantalla()
#         try:
#             duracion=int(input(f"Ingresa la duracion de la pelicula en minutos(numero)\n"))
#         except ValueError:
#             input("Ingresa un numero en la duracion de la pelicula(Oprimir Enter)")
#         else:
#             duracion=str(duracion)+" minutos"
#             break
#     peliculas[identificacion]["Duracion"]= duracion
#     limpiar_pantalla()
#     sinopsis=str(input("Ingresa la sinopsis de la pelicula\n"))
#     peliculas[identificacion]["Sinopsis"]= sinopsis
#     limpiar_pantalla()
    
#     genero={}
#     comprobar=True
#     while comprobar:
#         limpiar_pantalla()
#         bandera=True
#         while bandera:
#             print("Ingresa el Id del genero que le deseas asignar a la pelicula")
#             for i in generos:
#                 print(f"Id: {i}     Nombre del genero: {generos[i]['nombre']}")
#             eleccion_genero=str(input())
#             correcto=0
#             for i in generos:
#                 if eleccion_genero==i:
#                     correcto=1
#             if correcto==1:
#                 comprobacion=0
#                 for i in genero:
#                     if eleccion_genero==i:
#                         input("Ya le agregaste ese genero a la pelicula")
#                         comprobacion=1
#                 if comprobacion==0:
#                     genero[eleccion_genero]=generos[eleccion_genero]
#                 bandera=False
#             elif correcto==0:
#                 input("Ese genero no existe ingresa una opcion correcta(Oprime enter)")
#         while True:
#             try:
#                 otra_vez=int(input("Quieres agregarle otro genero\n 1. Si\n 2. No\n"))
#             except ValueError:
#                 input("Ingresa un numero(Oprimir Enter)")
#             else:
#                 break
#         if otra_vez==2:
#             comprobar=False
#         elif otra_vez==1:
#             comprobar=True
#     peliculas[identificacion]["generos"]= genero
#     actores={}
#     comprobar=True
#     while comprobar:
#         limpiar_pantalla()
#         bandera=True
#         while bandera:
#             print("Ingresa el Id del Actor que le deseas asignar a la pelicula")
#             for i in actores:
#                 print(f"Id: {i}     Nombre del genero: {actores[i]['nombre']}")
#             eleccion_actor=str(input())
#             correcto=0
#             for i in actores:
#                 if eleccion_actor==i:
#                     correcto=1
#             if correcto==1:
#                 comprobacion=0
#                 for i in actores:
#                     if eleccion_actor==i:
#                         input("Ya le agregaste ese Actor a la pelicula")
#                         comprobacion=1
#                 if comprobacion==0:
#                     actores[eleccion_actor]=actores[eleccion_actor]
#                 bandera=False
#             elif correcto==0:
#                 input("Ese actor no existe ingresa una opcion correcta(Oprime enter)")
#         while True:
#             try:
#                 otra_vez=int(input("Quieres agregarle otro Actor\n 1. Si\n 2. No\n"))
#             except ValueError:
#                 input("Ingresa un numero(Oprime Enter)")
#             else:
#                 break
#         if otra_vez==2:
#             comprobar=False
#         elif otra_vez==1:
#             comprobar=True
#     peliculas[identificacion]["Actores"]= actores
#     formato={}
#     comprobar=True
#     while comprobar:
#         limpiar_pantalla()
#         bandera=True
#         while bandera:
#             print("Ingresa el Id del formato que le deseas asignar a la pelicula")
#             for i in formatos:
#                 print(f"Id: {i}     Nombre del formato: {formatos[i]['nombre']}")
#             eleccion_formato=str(input())
#             correcto=0
#             for i in formatos:
#                 if eleccion_formato==i:
#                     correcto=1
#             if correcto==1:
#                 comprobacion=0
#                 for i in formato:
#                     if eleccion_formato==i:
#                         input("Ya le agregaste ese Formato a la pelicula")
#                         comprobacion=1
#                 if comprobacion==0:
#                     formato[eleccion_formato]=formatos[eleccion_formato]
#                 bandera=False
#             elif correcto==0:
#                 input("Ese genero no existe ingresa una opcion correcta(Oprime enter)")
#         while True:
#             try:
#                 otra_vez=int(input("Quieres agregarle otro formato\n 1. Si\n 2. No\n"))
#             except ValueError:
#                 input("Ingresa un numero(Oprime Enter)")
#             else:
#                 break
#         if otra_vez==2:
#             comprobar=False
#         elif otra_vez==1:
#             comprobar=True
#     peliculas[identificacion]["formatos"]= formato
#     with open("peliculas.json", "w+") as p:
#         p.write(json.dumps(peliculas, indent=4))    
# def editar_peliculas(peliculas, generos, formatos, actores):
#     print("Escribe el Id de la pelicula que deseas editar")
#     for i in peliculas:
#         print(f"Id: {i}     Nombre del genero: {peliculas[i]['Nombre']}")
#     eleccion_pelicula=str(input())
#     correcto=0
#     for i in peliculas:
#         if eleccion_pelicula==i:
#             correcto=1               
#     if correcto==1:
#         print("Que desea editar")
#         for i, j in enumerate(peliculas[eleccion_pelicula]):
#             print(f"{i+1}, {j}")
#         eleccion_modificar=int(input())
#         if eleccion_modificar==1:
#             input("El Id no se puede modificar")
#         elif eleccion_modificar==2:
#             nombre_pelicula=str(input("Ingresa el nombre de la pelicula que quieres agregar al sistema\n"))
#             peliculas[eleccion_pelicula]["Nombre"]= nombre_pelicula
#             with open("peliculas.json", "w+") as p:
#                 p.write(json.dumps(peliculas, indent=4))  
#         elif eleccion_modificar==3:
#             while True:
#                 limpiar_pantalla()
#                 try:
#                     duracion=int(input(f"Ingresa la duracion de la pelicula en minutos(numero)\n"))
#                 except ValueError:
#                     input("Ingresa un numero en la duracion de la pelicula(Oprime Enter)")
#                 else:
#                     duracion=str(duracion)+" minutos"
#                     break
#                 peliculas[eleccion_pelicula]["Duracion"]= duracion
#             with open("peliculas.json", "w+") as p:
#                 p.write(json.dumps(peliculas, indent=4))  
#         elif eleccion_modificar==4:
#             sinopsis=str(input("Ingresa la sinopsis de la pelicula\n"))
#             peliculas[eleccion_pelicula]["Sinopsis"]= sinopsis
#             with open("peliculas.json", "w+") as p:
#                 p.write(json.dumps(peliculas, indent=4))  
#         elif eleccion_modificar==5:
#             genero={}
#             comprobar=True
#             while comprobar:
#                 limpiar_pantalla()
#                 bandera=True
#                 while bandera:
#                     print("Ingresa el Id del genero que le deseas asignar a la pelicula")
#                     for i in generos:
#                         print(f"Id: {i}     Nombre del genero: {generos[i]['nombre']}")
#                     eleccion_genero=str(input())
#                     correcto=0
#                     for i in generos:
#                         if eleccion_genero==i:
#                             correcto=1
#                     if correcto==1:
#                         comprobacion=0
#                         for i in genero:
#                             if eleccion_genero==i:
#                                 input("Ya le agregaste ese genero a la pelicula")
#                                 comprobacion=1
#                         if comprobacion==0:
#                             genero[eleccion_genero]=generos[eleccion_genero]
#                         bandera=False
#                     elif correcto==0:
#                         input("Ese genero no existe ingresa una opcion correcta(Oprime enter)")
#                 while True:
#                     try:
#                         otra_vez=int(input("Quieres agregarle otro genero\n 1. Si\n 2. No\n"))
#                     except ValueError:
#                         input("Ingresa un numero(Oprime Enter)")
#                     else:
#                         break
#                 if otra_vez==2:
#                     comprobar=False
#                 elif otra_vez==1:
#                     comprobar=True
#             peliculas[eleccion_pelicula]["generos"]= genero
#             with open("peliculas.json", "w+") as p:
#                 p.write(json.dumps(peliculas, indent=4))  
#         elif eleccion_modificar==6:
#             actors={}
#             comprobar=True
#             while comprobar:
#                 limpiar_pantalla()
#                 bandera=True
#                 while bandera:
#                     print("Ingresa el Id del Actor que le deseas asignar a la pelicula")
#                     for i in actores:
#                         print(f"Id: {i}     Nombre del genero: {actores[i]['nombre']}")
#                     eleccion_actor=str(input())
#                     correcto=0
#                     for i in actores:
#                         if eleccion_actor==i:
#                             correcto=1
#                     if correcto==1:
#                         comprobacion=0
#                         for i in actors:
#                             if eleccion_actor==i:
#                                 input("Ya le agregaste ese Actor a la pelicula")
#                                 comprobacion=1
#                         if comprobacion==0:
#                             actors[eleccion_actor]=actores[eleccion_actor]
#                         bandera=False
#                     elif correcto==0:
#                         input("Ese actor no existe ingresa una opcion correcta(Oprimir enter)")
#                 while True:
#                     try:
#                         otra_vez=int(input("Quieres agregarle otro Actor\n 1. Si\n 2. No\n"))
#                     except ValueError:
#                         input("Ingresa un numero(Oprimir Enter)")
#                     else:
#                         break
#                 if otra_vez==2:
#                     comprobar=False
#                 elif otra_vez==1:
#                     comprobar=True
#             peliculas[eleccion_pelicula]["Actores"]= actores
#             with open("peliculas.json", "w+") as p:
#                 p.write(json.dumps(peliculas, indent=4))  
#         elif eleccion_modificar==7:
#             formato={}
#             comprobar=True
#             while comprobar:
#                 limpiar_pantalla()
#                 bandera=True
#                 while bandera:
#                     print("Ingresa el Id del formato que le deseas asignar a la pelicula")
#                     for i in formatos:
#                         print(f"Id: {i}     Nombre del formato: {formatos[i]['nombre']}")
#                     eleccion_formato=str(input())
#                     correcto=0
#                     for i in formatos:
#                         if eleccion_formato==i:
#                             correcto=1
#                     if correcto==1:
#                         comprobacion=0
#                         for i in formato:
#                             if eleccion_formato==i:
#                                 input("Ya le agregaste ese Formato a la pelicula")
#                                 comprobacion=1
#                         if comprobacion==0:
#                             formato[eleccion_formato]=formatos[eleccion_formato]
#                         bandera=False
#                     elif correcto==0:
#                         input("Ese genero no existe ingresa una opcion correcta(Oprime enter)")
#                 while True:
#                     try:
#                         otra_vez=int(input("Quieres agregarle otro formato\n 1. Si\n 2. No\n"))
#                     except ValueError:
#                         input("Ingresa un numero(Oprime Enter)")
#                     else:
#                         break
#                 if otra_vez==2:
#                     comprobar=False
#                 elif otra_vez==1:
#                     comprobar=True
#             peliculas[eleccion_pelicula]["formatos"]= formato
#             with open("peliculas.json", "w+") as p:
#                 p.write(json.dumps(peliculas, indent=4))  
# def eliminar_pelicula(peliculas):
#     print("Escribe el Id de la pelicula que deseas eliminar")
#     for i in peliculas:
#         print(f"Id: {i}     Nombre del genero: {peliculas[i]['Nombre']}")
#     eleccion_pelicula=str(input())
#     correcto=0
#     for i in peliculas:
#         if eleccion_pelicula==i:
#             correcto=1    
#     if correcto==1:
#         peliculas[eleccion_pelicula].remove()
#         with open("peliculas.json", "w+") as p:
#             p.write(json.dumps(peliculas, indent=4))  
#     elif correcto==0:
#         input("La pelicula que ingresaste no existe(Oprime Enter)")
# def eliminar_actor(peliculas):
#     print("Escribe el Id de la pelicula que deseas eliminar")
#     for i in peliculas:
#         print(f"Id: {i}     Nombre del genero: {peliculas[i]['Nombre']}")
#     eleccion_pelicula=str(input())
#     correcto=0
#     for i in peliculas:
#         if eleccion_pelicula==i:
#             correcto=1    
#     if correcto==1:
#         print("Escribe la Id del actor que deseas eliminar")
#         for i in peliculas[eleccion_pelicula]["Actores"]:
#             print(f"Id {i} Actor: {peliculas[eleccion_pelicula]['Actores'][i]['nombre']}")
#         eleccion_actor_eliminar=input()
#         correcto2=0
#         for i in peliculas[eleccion_pelicula]["Actores"]:
#             if eleccion_actor_eliminar==i:
#                 correcto2=1
#         if correcto2==1:
#             peliculas[eleccion_pelicula]['Actores'][eleccion_actor_eliminar].remove()
#         elif correcto2==0:
#             input("No existe este actor en la pelicula(Oprime Enter)")
#     elif correcto==0:
#         input("No existe esta pelicula(Oprime Enter)")
# def buscar_pelicula(peliculas):
#     print("Escribe el Id de la pelicula que deseas eliminar")
#     for i in peliculas:
#         print(f"Id: {i}     Nombre del genero: {peliculas[i]['Nombre']}")
#     eleccion_pelicula=str(input())
#     correcto=0
#     for i in peliculas:
#         if eleccion_pelicula==i:
#             correcto=1    
#     if correcto==1:
#         print(peliculas[eleccion_pelicula])
# def listar_peliculas(peliculas):
#     for i in peliculas:
#         print(f"Id: {i}     Nombre del genero: {peliculas[i]['nombre']}")
#     input("Oprimir enter")
            
import json
from commons.menus import *
from commons.utlis import *


def crear_pelicula(lista_peliculas, generos, formatos, actores):
    limpiar_pantalla()
    nueva_pelicula = True
    while nueva_pelicula:
        try:
            identificacion = int(input("Ingresa el código con el que quieres identificar la película (número)\n"))
        except ValueError:
            print("Ingresa un número")
        else:
            identificacion = "P" + str(identificacion)
            conteo = 0
            for pelicula_id in lista_peliculas:
                if pelicula_id == identificacion:
                    print(f"Esta película ya existe\n Id: {pelicula_id} Nombre: {lista_peliculas[pelicula_id]['Nombre']}")
                    conteo = 1
            if conteo == 0:
                nueva_pelicula = False

    lista_peliculas[identificacion] = {"Id": identificacion}

    limpiar_pantalla()
    nombre_pelicula = input("Ingresa el nombre de la película que quieres agregar al sistema\n")
    lista_peliculas[identificacion]["Nombre"] = nombre_pelicula

    while True:
        limpiar_pantalla()
        try:
            duracion = int(input("Ingresa la duración de la película en minutos (número)\n"))
        except ValueError:
            input("Ingresa un número en la duración de la película (Oprime Enter)")
        else:
            lista_peliculas[identificacion]["Duracion"] = f"{duracion} minutos"
            break

    limpiar_pantalla()
    sinopsis = input("Ingresa la sinopsis de la película\n")
    lista_peliculas[identificacion]["Sinopsis"] = sinopsis

    
    with open("peliculas.json", "w+") as file:
        json.dump(lista_peliculas, file, indent=4)

with open("generos.json", "r") as f:
    generos_data = json.loads(f.read())

with open("actores.json", "r") as a:
    actores_data = json.loads(a.read())

with open("formatos.json", "r") as j:
    formatos_data = json.loads(j.read())



peliculas_data = {}
crear_pelicula(peliculas_data, generos_data, formatos_data, actores_data)
