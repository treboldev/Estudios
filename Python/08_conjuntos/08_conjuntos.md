![Banner](../Python_Github_Banner.png)


<div align="center"><h2>Conjuntos</h2></div>

Los conjuntos `(sets)` en Python son un tipo de dato **mutable** que se utilizan para almacenar colecciones **desordenadas** y **únicas** de elementos. esto significa que los conjuntos no ppermiten elementos duplicados y el orden de los elementos no esta definido. Los conjuntos son útiles para representar conjuntos de datos, como conjuntos de números, conjuntos de palabras o conjuntos de objetos.

### ***¿Cómo se crean los conjuntos?***

Los conjuntos se crean utilizando la funcion `set()` y pasando un iterable (como una lista, tupla o cadena) como argumento. también se pueden crear conjuntos vacíos utilizando la función `set()`.

```py
# Ejemplo de creación de un conjunto a partir de una lista.
numeros = [1, 2, 3, 4, 4, 3, 2, 1]
conjunto_numeros = set(numeros)
print(conjunto_numeros)             # {1, 2, 3, 4}

# Ejemplo de creación de un conjunto vacío. 
conjunto_vacio = set()
print(conjunto_vacio)               # set()
```

### ***¿Cómo se añaden elementos a un conjunto?***

Se pueden añadir elementos a un conjunto utilizando el método `add()`. Si el elemento ya existe en el conjunto, no se añade de nuevo.

```py
conjunto_frutas = {"Manzana", "Platano", "Pera"}
conjunto_frutas.add("Uva")
print(conjunto_frutas)              # {"Manzana", "Platano", "Pera", "Uva"}
```

### ***¿Cómo se eliminan elementos de un conjunto?***

se pueden eliminar elementos de un conjunto utilizando el método `remove()`. si el elemento no existe en el conjunto, se generara una excepción `KeyError`.

```py
conjunto_numeros = {1, 2, 3, 4}
conjunto_numeros.remove(3)
print(conjunto_frutas)              #   {1, 2, 3}
```

### ***¿Cómo se comprueban si existen elementos en un conjunto?***

Se puede comprobar si un elemento existe en un conjunto utilizando el operador de pertenencia `in`.

```py
conjunto_animales = {"perro", "Gato", "Conejo"}
print("Perro" in conjunto_animales)         # True
print("caballo" in conjunto_animales)       # False
```

### ***¿Cuáles son las operaciones que se pueden realizar con conjuntos?***

Los conjuntos en Python soportan diversas operaciones, como:

- ***Unión:*** Combinar dos conjuntos en un nuevo conjunto que contiene todos los elementos únicos de ambos conjuntos.
  
- ***Intersección:*** Encontrar los elementos comunes de dos conjuntos.
  
- ***Diferencia:*** Encontrar los elementos que pertenecen a un conjunto pero no al otro.
  
- ***Subconjunto:*** Comprobar si un conjunto está contenido dentro de otro conjunto.
  
- ***Comparación:*** Comparar dos conjuntos para determinar si son iguales o si uno es subconjunto del otro.

##### ***Ejemplo de operaciones con conjuntos:***

```py
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}

# Union
conjunto_union = conjunto_a | conjunto_b
print(conjunto_union)                               # {1, 2, 3, 4, 5}

# Intersección
conjunto_interseccion = conjunto_a & conjunto_b
print(conjunto_interseccion)                        # {3}

# Diferencia
conjunto_diferencia = conjunto_a - conjunto_b
print(conjunto_diferencia)                          # {1, 2}

# Subconjunto
conjunto_a.issubset(conjunto_b)                     # False
conjunto_b.issubset(conjunto_a)                     # False
conjunto_a.issuperset(conjunto_b)                   # False
conjunto_b.issuperset(conjunto_a)                   # False

# Igualdad
conjunto_a == conjunto_b                            # False
```