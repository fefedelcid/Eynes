'''
Hacer una función que genere una lista de diccionarios que contengan id
y edad, donde edad sea un número aleatorio entre 1 y 100 y la longitud
de la lista sea de 10 elementos. Retornar la lista.
'''

from random import randint

def simple():
    lista = []

    for id in range(10):
        lista.append({"id":id, "edad":randint(1, 100)})

    return lista


'''
Hacer otra función que reciba lo generado en la primer función y
ordenarlo de mayor a menor. Printear el id de la persona más joven
y más vieja. Devolver la lista ordenada.
'''

def ordenar(lista = simple()):
    """Ordena una lista enviada, si no se envía ninguna se creará
    una aleatoria"""

    lista_ord = sorted(lista, key = lambda persona: persona['edad'])

    print(f'La persona más joven tiene id = {lista_ord[0]["id"]}')
    print(f'La persona más vieja tiene id = {lista_ord[-1]["id"]}')

    return lista_ord
