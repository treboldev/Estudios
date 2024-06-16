![Banner](/Python/Python_Github_Banner.png)

<div align="center"><h1>Listas</h2></div>

En python, una lista `(list)` es un tipo de dato compuesto que permite almacenar una colección ordenada de elementos. Estos elementos pueden ser de cualquier tipo de dato en Python, incluyendo números, cadenas de texto, booleanos, otras listas e incluso objetos. Las listas son mutables, lo que significa que se pueden modificar despueés de haber sido creadas.

### ***¿Cómo se crean las listas?***

Las listas se crean utilizando corchetes `[]` y separando los elementos por comas. No es necesario especificar el tipo de dato de los elementos, ya que python lo infiere automáticamente a partir del valor asignado.

```py
# Ejemplo de creación de una lista. 
frutas = ["Manzana", "Platano", "Pera", "Naranja"]
numeros = [1, 2, 3, 4, 5]
mezcla = [True, "Hola", 10.5, frutas]
```

### ***¿Cómo se accede a los elementos de una lista?***

Se puede acceder a los elementos de una lista utilizando su índice. El índice comienza en 0, y se puede acceder al último elemento utiliznado la longitud de la lista menos 1.

```py
# Ejemplo de acceso a elementos por índice. 
primer_fruta = frutas[0]                # Manzana
segundo_numero = numeros[1]             # 2. 
ultimo_elemento = mezcla[-1]            # ["Manzana", "Platano", "Pera", "Naranja"]

# Acceso a un rango de elementos. 
sublista = frutas[1:3]                  # ["Platano", "Pera"]
```

### ***¿Cómo se modifican las listas?***

Las listas se pueden modificar de diversas maneras, como:

- ***Agregar elementos:*** Se utiliza el método `append()` para agregar un elemento al final de la lista.
  
- ***Eliminar elementos:*** Se utiliza el operador `del` o el método `remove()` para eliminar un elemento por índice.
  
- ***Modificar elementos:*** Se utiliza el operador de asignación `(=)` para modificar un elemento por índice.
  
- ***insertar elementos:*** se utiliza el método `insert()` para insertar un elemento en una posición especifica de la lista.

```py
# Ejemplo de modificacion de listas. 

frutas.append("Uva")            # Agrega "Uva" al final de la lista. 
numeros.remove(3)               # Elimina el número 3 de la lista. 
mezcla[0] = False               # Cambia el primer elemento de la lista a False. 
frutas.insert(1, "Kiwi")        # Inserta "Kiwi" en la posición 1 de la lista. 
```

### ***¿Cuáles son las operaciones que se pueden realizar con listas?***
Las listas en Python soportan una amplia gama de operaciones, como:

- ***Concatenación:*** Unir dos o más listas.
- ***Repetición:*** Repetir una lista un número especifico de veces.
- ***Búsqueda:*** Encontrar un elemento específico dentro de una lista.
- ***Ordenamiento:*** Ordena los elementos de una lista según un criterio.
- ***Inversión:*** Invertir el orden de los elementos de una lista.
- ***Comprobación de pertenencia:*** Verificar si un elemento pertenece a una lista.
- ***Obtención de longitud:*** Obtener el n´umero de elementos de una lista.