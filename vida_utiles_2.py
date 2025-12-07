def crear_tablero(filas: int, columnas: int) -> list[list[bool]]:
    """
    Crea un nuevo tablero vacío, con todas las células muertas.
    Parametros:
        filas (int): Número de filas del tablero.
        columnas (int): Número de columnas del tablero.
    Devuelve:
        Una lista de listas con todos los elementos False.
    """

    tablero = list(list())
    for i in range(filas):
        tablero.append(list())
        for j in range(columnas):
                tablero[i].append(False)
    return tablero

import random
def crear_tablero_aleatorio(filas: int, columnas: int, probabilidad_vida: float) -> list[list[bool]]:
    """
    Crea un tablero con células vivas distribuidas aleatoriamente.

    Parámetros:
        filas (int): Número de filas del tablero.
        columnas (int): Número de columnas del tablero.
        probabilidad_vida (float): Un valor entre 0.0 y 1.0 que representa la
                                   probabilidad de que una célula esté viva.

    Devuelve:
        Una lista de listas que representa el tablero con células vivas (True) y muertas (False).
    """
    tablero = list(list())
    for i in range(filas):
        tablero.append(list())
        for j in range(columnas):
            if random.random() < probabilidad_vida:
                tablero[i].append(False)
            else:
                 tablero[i].append(True)
    return tablero

def insertar_patron(tablero: list[list[bool]], patron: list[list[bool]], pos_fila: int, pos_col: int):
    """
    Inserta un patrón (una pequeña matriz) en el tablero en una posición dada.
    Parámetros:
        tablero (list[list[bool]]): El tablero donde se insertará el patrón.
        patron (list[list[bool]]): El patrón a insertar.
        pos_fila (int): La fila en la que se insertará la esquina superior izquierda del patrón.
        pos_col (int): La columna en la que se insertará la esquina superior izquierda del patrón.
    """
    for i in range(len(patron)):
         for j in range(len(patron[0])):
              if i > len(tablero) or j > len(tablero[0]):
                pass
              else:
                  tablero[pos_fila + i][pos_col + j] = patron[i][j]
    return tablero
              
              
def contar_vecinos(tablero: list[list[bool]], fila: int, col: int) -> int:
    """
    Cuenta el número de vecinos vivos de una célula en la posición (fila, col).
    El tablero es toroidal, lo que significa que los bordes se conectan.
    Parámetros:
        tablero (list[list[bool]]): El tablero actual.
        fila (int): La fila de la célula.
        col (int): La columna de la célula.
    Devuelve:
        El número de vecinos vivos (int).
    """
    vecinos_vivos = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0 :
                pass
            else:
                pos_fila = (fila + i) % len(tablero) 
                pos_col = (col + j) % len(tablero[0])
                if tablero[pos_fila][pos_col]:
                    vecinos_vivos += 1
    return vecinos_vivos


def calcular_siguiente_generacion(tablero):
    """
    Calcula el estado del tablero en el siguiente paso de tiempo basándose en las reglas
    del Juego de la Vida.
    Parámetros:
        tablero (list[list[bool]]): El tablero actual.
    Devuelve:
        Una nueva lista de listas que representa el tablero en la siguiente generación.
    """
    filas_tablero = len(tablero)
    col_tablero = len(tablero[0])
    res = crear_tablero(filas_tablero, col_tablero)

    for i in range(filas_tablero):
        for j in range(col_tablero):
            vecinos_vivos = contar_vecinos(tablero, i, j)
            if (vecinos_vivos == 2 or vecinos_vivos == 3) and tablero[i][j]:
                res[i][j] = True
            elif vecinos_vivos == 3:
                res[i][j] = True
            else:
                res[i][j] = False
    return res
            
