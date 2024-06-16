![Banner](/Python/Python_Github_Banner.png)

<div align="center"><h1>Tuplas</h2></div>

Las tuplas en Python son un tipo de dato **inmutable** que se utilizan para almacenar colecciones ordenadas de elementos. A diferencia de las listas, las tuplas no se pueden modificar una vez creadas. Son útiles para representar datos que no cambian con el tiempo, como coordenadas, direcciones o información de configuración.

### ***¿Cómo se crean las tuplas?***

Las tuplas se crean utilizando paréntesis `()` y seprando los elementos por comas. no es necesario especificar el tipo de datos de los elementos, ya que python los infiere automaticamente a partir del valor asignado.

```py
# Ejemplo de creación de una tupla. 
frutas = ("Manzana", "Platano", "Pera", "Naranja")
numeros = (1, 2, 3, 4, 5)
mezcla = (True, "Hola", 10.5, frutas)
```

### ***¿Cómo se accede a los elementos de una tupla?***

Se puede acceder a los elementos de una tupla utilizando su índice. El índice comienza en 0, y se puede acceder al último elementos utilizando la longitud de la tupla menos 1.

```py
# Ejempleo de acceso a elementos por índice
primera_fruta = frutas[0]           # "Manzana"
segundo_numero = numeros[1]         # 2
ultimo_elemento = mexcla[-1]        # ("Manzana", "Platano", "Pera", "Naranja")

# Acceso a un rango de elementos. 
subtupla = frutas[1:3]              # ("Platano", "Pera")
```

### ***¿Cuáles son las operaciones que se pueden realizar con tuplas?***

las tuplas en Python soportan algunas operaciones básicas, como:

- ***Concatenación:*** Unir dos o más tuplas.
- ***Repetición:*** Repetir una tupla un número específico de veces.
- ***Búsqueda:*** Encontrar un elemento específico dentro de una tupla.
- ***Obtención de longitud:*** Obtener el número de elementos de una tupla.
- ***Deswmpaquetado:*** Extraer elementos de una tupla en variables separadas.

##### ***Ejemplo de desempaquetado de tuplas:***

```py
frutas = ("Manzana", "Platano", "Pera")
fruta1, fruta2, fruta3 = frutas     # desempaquetado en tres variables.
print(f"Primera fruta: {fruta1}")   # Manzana
print(f"Segunda fruta: {fruta2}")   # Platano
print(f"Tercera fruta: {fruta3}")   # Pera
```

