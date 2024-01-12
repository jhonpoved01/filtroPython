# import os

# def limpiar_pantalla():
#     os.system('clear' if os.name == 'posix' else 'cls')    


# def validar_opcion(enunciando,inferior,superior):
#     while True:
#         try:
#             opcion =int(input(enunciando))
#             if opcion>=inferior and opcion<=superior:
#                 return opcion
#             else:
#                 print(f"Opción no está entre el intervalo de ({inferior}-{superior})")
#         except ValueError:
#             print("Por favor, introduce un número válido. ")

import os

def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    os.system('clear' if os.name == 'posix' else 'cls')    


def validar_opcion(enunciado, inferior, superior):
    """
    Solicita al usuario una opción y valida que esté dentro del rango especificado.

    Args:
    - enunciado (str): El mensaje que se mostrará al usuario.
    - inferior (int): Límite inferior del rango.
    - superior (int): Límite superior del rango.

    Returns:
    - int: La opción válida ingresada por el usuario.
    """
    while True:
        try:
            opcion = int(input(enunciado))
            if inferior <= opcion <= superior:
                return opcion
            else:
                print(f"La opción no está dentro del intervalo ({inferior}-{superior})")
        except ValueError:
            print("Por favor, introduce un número entero válido.")


