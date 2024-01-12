# import json
# from commons.utlis import *
# from commons.menus import *

# def crear_formato(formatos):
#     limpiar_pantalla()
#     bandera=True
#     while bandera:
#         try:
#             identificacion=int(input(f"Ingresa el codigo con el que quieres identificar el formato(numero)\n"))
#         except ValueError:
#             print("Ingresa un numero")
#         else:
#             identificacion="F"+str(identificacion)
#             conteo=0
#             for i in formatos:
#                 if i==identificacion:
#                     print(f"Este formato ya existe\n Id: {i} Nombre: {formatos[i]['nombre']}")
#                     conteo=1
#             if conteo==0:
#                 bandera=False
#     limpiar_pantalla()
#     nombre_formato=str(input("Ingrese el nombre del formato que desea ingresar al sistema\n"))  
#     formatos[identificacion]=dict([("id", identificacion), ("nombre", nombre_formato)])
#     input(f"Se creo el formato {nombre_formato} con el codigo {identificacion}\n Oprime Enter")
#     with open("formatos.json","w+") as a:
#         a.write(json.dumps(formatos, indent=4))
# def listar_formatos(formatos):
#     limpiar_pantalla()
#     print("Los actores ingresados al sistema son:")
#     for i in formatos:
#         print(f"Id: {i}       Formato: {formatos[i]['nombre']}")
#     input("Oprime enter para salir")

import json
from commons.utlis import limpiar_pantalla
from commons.menus import *

def crear_formato(formatos):
    limpiar_pantalla()
    bandera = True
    while bandera:
        try:
            identificacion = int(input("Ingresa el código con el que quieres identificar el formato (número)\n"))
        except ValueError:
            print("Ingresa un número")
        else:
            identificacion = "F" + str(identificacion)
            conteo = 0
            for formato_id in formatos:
                if formato_id == identificacion:
                    print(f"Este formato ya existe\n Id: {formato_id} Nombre: {formatos[formato_id]['nombre']}")
                    conteo = 1
            if conteo == 0:
                bandera = False

    limpiar_pantalla()
    nombre_formato = input("Ingrese el nombre del formato que desea ingresar al sistema\n")
    formatos[identificacion] = {"id": identificacion, "nombre": nombre_formato}
    input(f"Se creó el formato {nombre_formato} con el código {identificacion}\n Oprime Enter")
    
    with open("formatos.json", "w+") as file:
        json.dump(formatos, file, indent=4)

def listar_formatos(formatos):
    limpiar_pantalla()
    print("Los formatos ingresados al sistema son:")
    for formato_id in formatos:
        print(f"Id: {formato_id}       Formato: {formatos[formato_id]['nombre']}")
    input("Oprime enter para salir")

