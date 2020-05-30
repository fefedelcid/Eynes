'''
Crear una matriz de 5x5 con números enteros, encontrar secuencia
de 4 números consecutivos horizontal o vertical y si se encuentra
mostrar la posición inicial y final.
'''

from random import randint

def matrixGenerator():
    """
    La función crea y retorna una matriz de 5x5 con valores
    aleatorios entre 0 y 9.
    """

    matriz = []

    for n in range(5):
        fila = [randint(0, 9) for n in range(5)]
        matriz.append(fila)

    return matriz


def findSeq(matrix, seq):
    """
    La función recibe una matriz de 5x5 compuesta por números enteros
    entre 0 y 9, y una secuencia de 4 números enteros.
    En caso de encontrar la secuencia en dicha matriz retorna la posición
    de inicio y fin de la misma.
    Caso contrario retorna 0.
    """

    seq = ''.join(str(n) for n in seq)

    # Búsqueda horizontal
    for row in matrix:
        r = ''.join(str(n) for n in row)

        # Como la búsqueda será horizontal, solo se maneja una fila por vez
        y = matrix.index(row) + 1

        # seq[::-1] invierte el orden de la secuencia
        if seq[::-1] in r:
            start = 5 - r[::-1].index(str(seq[0]))
            pos1 = (y, start)
            pos2 = (y, start - 3)
            # (fila, columna) // (y, x)
            return (pos1, pos2)
        elif seq in r:
            start = r.index(seq[0]) + 1
            pos1 = (y, start)
            pos2 = (y, start + 3)
            # (fila, columna) // (y, x)
            return (pos1, pos2)

    # Búsqueda vertical
    for col in range(5):
        c = ''.join(str(e[col]) for e in matrix)

        # seq[::-1] invierte el orden de la secuencia
        if seq[::-1] in c:
            start = 5 - c[::-1].index(str(seq[0]))
            pos1 = (start, col + 1)
            pos2 = (int(start) - 3, col + 1)
            # (fila, columna) // (y, x)
            return (pos1, pos2)
        elif seq in c:
            start = c.index(seq[0]) + 1
            pos1 = (start, col + 1)
            pos2 = (start + 3, col + 1)
            # (fila, columna) // (y, x)
            return (pos1, pos2)

    return 0
