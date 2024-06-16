![Banner](../Python_Github_Banner.png)


<div align="center"><h2>Diccionarios</h2></div>

Los diccionarios `dicts()` en python son un tipo de dato **mutable** que se utilizan para almacenar colecciones **desordenadas** de pares **clave-valor**. Esto significa que cada elemento en un diccionario se asocia con una clave única, y el valor puede ser de cualquier tipo de dato en python. Los diccionarios son útiles para representar datos estructurados, como información de contacto, configuraciones de aplicación o datos de bases de datos.

### ***¿Cómo se crean los diccionaros?***

Los diccionarios se crean utilizando llaves `{}` y separando los pares clave-valor por comas. Las claves deben ser únicas e inmutables (como cadenas o tuplas), mientras que los valores pueden ser de cualquier tipo de dato.

```py
# Ejemplo de creación de un diccionario.
persona = {
    "nombre": "Juan",
    "apellido": "Perez",
    "edad": 30,
    "ciudad": "Santiago"
}

# Ejemplo de acceso a valores por clave
print(persona["nombre"])            # Juan
print(persona["ciudad"])            # Santiago

# modificar un valor existente
personal["edad"] = 31
print(personal["edad"])             # 31

# Agregar un valor por clave-valor
personal["telefono"] = "+56912341234"
print(persona)                      # {"nombre": "Juan", "apellido": "Perez", "edad": 31, "ciudad": "Santiago", "Telefono": "+56912341234"}
```

### ***¿Cómo se iteran los diccionarios?***

Se puede iterar sobre las claves o valor de un diccionario utilizando un bucle `for`.

```py
# Iterar sobre las claves del diccionario
for clave in persona:
    print(clave)        # nombre, apellido, edad, ciudad, telefono. 

# Iterar sobre los valores del diccionario
for valor in persona.values():
    print(valor)        # Juan, Perez, 31, Santiago, +56912341234
```

### ***¿Cuáles son las operaciones que se pueden realizar con diccionarios?***

los diccionarios en python soportan diversas operaciones, como:

- ***Obtener el valor de una clave:*** Se utiliza el operador de índice `[]` o el método `get()`.
- ***Comprobar si una clave existe:*** Se utiliza el operador `in`.
- ***Agregar un nuevo par clave-valor:*** Se utiliza el operador de asignacción `=` o el método `update()`.
- ***Modificar un valor existente:*** Se utiliza el operador de asignacion `=` o el método `update()`.
- ***Eliminar un par clave-valor:*** Se utiliza el operador `del` o el método `pop()`.
- ***Copair un diccionario:*** Se utiliza la función `copy()` o el método `dict()`.
- ***Combinarn diccionarios:*** Se utiliza el operador `+` o el método `update()`.
- ***Obtener la longitud de un diccionariop:*** Se utiliza la función `len()`.
- ***Convertir un diccionario en una lista de claves o valores:*** se utilizan los métodos `key()`.`values()` y `items()`.