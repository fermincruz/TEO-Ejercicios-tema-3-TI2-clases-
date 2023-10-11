def indica_primera_aparicion(lista, valor):
    '''
    Devuelve la posición de valor en lista,
    o -1 si no se encuentra
    '''
    for i, elemento in enumerate(lista):
        if elemento == valor:
            return i
    return -1


if __name__ == '__main__':
    palabras = ["árbol", "coche", "casa", "peatón"]
    print('Posición de "casa" en la lista ["árbol", "coche", "casa", "peatón"]:',
          indica_primera_aparicion(palabras, "casa"))

    print('Posición de "bicicleta" en la lista ["árbol", "coche", "casa", "peatón"]:',
          indica_primera_aparicion(palabras, "bicicleta")
          )
