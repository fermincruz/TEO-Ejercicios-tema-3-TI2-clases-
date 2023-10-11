# Ejercicios del tema 3: Instrucciones condicionales y bucles
---

Cree una carpeta ``src``, y dentro de la misma un archivo ``ejercicioX.py`` para cada ejercicio que vaya a resolver, sustituyendo la X por el número del ejercicio. Implemente en cada archivo la función solicitada por el ejercicio correspondiente, asegurándose de que las pruebas de la función se realicen como programa principal.


### Ejercicio 1
Defina una función ``imprime_diccionario`` que imprima cada clave y cada valor del diccionario, con el siguiente formato:
```
clave ===> valor
```

Pruebe la función pasándole este diccionario a la función: 
```python
precios_productos = {
    "manzana": 0.5,
    "plátano": 0.3,
    "naranja": 0.6,
    "uva": 1.2,
    "fresa": 2.5
}
```

### Ejercicio 2
Defina una función ``imprime_pares`` que reciba un entero ``n`` e imprima en la consola los número pares positivos menores o iguales a ``n``. Todos los números se deben imprimir en una sola línea, separados por espacios.

Pruebe la función de manera que se obtenga una salida parecida a esta:

```
Imprimiendo números pares menores o iguales a 5:
2 4 

Imprimiendo números pares menores o iguales a 6:
2 4 6
```


### Ejercicio 3
Implemente una nueva versión de ``imprime_pares`` (llámela ``imprime_pares_inverso``) que funcione igual que la anterior pero imprima los números empezando por el mayor.

Pruebe la función de manera que se obtenga una salida parecida a esta:
```
Imprimiendo números pares menores o iguales a 5:
4 2 

Imprimiendo números pares menores o iguales a 6:
6 4 2
```

### Ejercicio 4
Defina una función ``indica_primera_aparicion`` que recibe un parámetro ``lista`` y un parámetro ``valor``, y devuelve el índice de la primera aparición de ``valor`` en ``lista``. Si no se encuentra ``valor`` en ``lista``, de devolverá ``-1``.

Pruebe la función de manera que se obtenga una salida parecida a esta:
```
Posición de "casa" en la lista ["árbol", "coche", "casa", "peatón"]: 2
Posición de "bicicleta" en la lista ["árbol", "coche", "casa", "peatón"]: -1
```

NOTA: Las listas en Python tienen un método parecido al que aquí estamos implementando (``index``), pero en este ejercicio no haremos uso de él.


### Ejercicio 5
Tenemos un fichero CSV con registros de libros en una librería (se muestra la primera línea del fichero):

```
978-3-16-148410-0, El Gran Gatsby, F. Scott Fitzgerald, 10/04/1925, 12.99, True
```

Las columnas son:

* ISBN (str): Identificador único de cada libro.
* Título (str): Título del libro.
* Autor (str): Nombre del autor del libro.
* Fecha de publicación (date): Fecha en la que fue publicado el libro.
* Precio (float): Precio de venta en euros.
* Disponible (bool): Indica si el libro está en stock.

Se dispone de la namedtuple ``Libro`` para representar esta información (puede ver la definición en el módulo ``ejercicio5.py``).

Implemente las siguientes funciones:

* Función ``autores_disponibles``, que recibe una lista de libros y una cadena ``inicial`` y devuelve una lista ordenada alfabéticamente con los nombres de los autores cuya inicial es la indicada y para los que hay libros en stock en la librería. La lista no puede contener duplicados.

* Función ``titulos_baratos_actuales``, que recibe una lista de libros y devuelve una lista con los títulos de los libros con un precio a 20 euros que hayan sido publicados a partir del año 2001.

* Función ``media_precios``, que recibe una lista de libros y una cadena de texto ``palabra`` y devuelve la media del precio de los libros que contienen en su título la ``palabra`` en cuestión. Si no se encuentra ningún libro con dicha palabra en el título, la función devuelve ``None``. **NOTA**: La búsqueda de los libros con la palabra en el título no debe ser sensible a mayúsculas.

* Función ``libro_mas_reciente``, que recibe una lista de libros y devuelve el libro con la fecha de publicación más reciente.

Al probar las funciones, debe obtener una salida parecida a esta:

```
Autores disponibles que comienzan por 'M': ['Margaret Atwood', 'Margaret Mitchell', 'Mark Twain', 'Miguel de Cervantes']
Titulos baratos actuales: ['La carretera', 'La sombra del viento', 'La chica con el tatuaje de dragón', 'La chica del tren']
Media de precios de libros con la palabra 'El': 25.093571428571426
Libro más reciente: Libro(isbn='978-3-16-392611-0', titulo='La chica del tren', autor='Paula Hawkins', fecha_publicacion=datetime.date(2015, 1, 13), precio=8.34, disponible=False)
```