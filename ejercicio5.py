from collections import namedtuple
import csv
from datetime import datetime

Libro = namedtuple(
    "Libro", "isbn,titulo,autor,fecha_publicacion,precio,disponible")


def lee_libros(ruta_csv):
    with open(ruta_csv, encoding="utf-8") as f:
        res = []
        lector = csv.reader(f)
        next(lector)
        for isbn, titulo, autor, fecha_publicacion, precio, disponible in lector:
            fecha_publicacion = datetime.strptime(
                fecha_publicacion, "%d/%m/%Y").date()
            precio = float(precio)
            disponible = disponible == "Sí"
            res.append(
                Libro(isbn, titulo, autor, fecha_publicacion, precio, disponible)
            )
        return res


# TODO: Implemente las funciones solicitadas en el enunciado
def autores_disponibles(libros, inicial):
    # Condición de filtrado: libro.autor[0] == inicial and libro.disponible
    # Tip: también se puede usar el método startswith
    # libros.autor.startswith(inicial)
    autores = set()   # ¡CUIDADO! No se puede poner autores = {}
    for libro in libros:
        if libro.autor[0] == inicial and libro.disponible:
            autores.add(libro.autor)

    # La función sorted recibe cualquier iterable y devuelve una lista ordenada
    return sorted(autores)


def titulos_baratos_actuales(libros):
    titulos = []
    for libro in libros:
        if libro.precio < 20 and libro.fecha_publicacion.year >= 2001:
            titulos.append(libro.titulo)
    return titulos


def media_precios(libros, palabra):
    suma = 0
    num_elementos = 0
    for libro in libros:
        if palabra.lower() in libro.titulo.lower():
            suma += libro.precio
            num_elementos += 1

    if num_elementos == 0:
        return None

    return suma / num_elementos


def media_precios_version2(libros, palabra):
    precios = []
    for libro in libros:
        if palabra.lower() in libro.titulo.lower():
            precios.append(libro.precio)

    if len(precios) == 0:
        return None

    return sum(precios) / len(precios)

    # Hay una forma de usar sum directamente con los elementos
    # "sacados" de la lista libros que me interese:
    # sum(libro.precio for libro in libros if palabra.lower() in libro.titulo.lower())


def libro_mas_reciente(libros):
    # Aquí voy a guardar el libro que sea más reciente hasta el momento
    mas_reciente = None
    for libro in libros:
        # Si hubiera un filtro (por ejemplo, el más reciente de libros que estén en stock),
        # lo meteríamos AQUÍ:
        # if libro.disponible:
        # Este if NO ES un filtro
        if mas_reciente == None or libro.fecha_publicacion > mas_reciente.fecha_publicacion:
            mas_reciente = libro
    return mas_reciente


if __name__ == "__main__":
    libros = lee_libros("data/libreria.csv")
    print(f"Se han leído {len(libros)} libros.")

    print("Autores disponibles:", autores_disponibles(libros, "M"))
    print("Titulos baratos actuales:", titulos_baratos_actuales(libros))
    print(
        "Media de precios de libros con la palabra 'El':", media_precios(
            libros, "El")
    )
    print("Libro más reciente:", libro_mas_reciente(libros))
