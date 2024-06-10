<div align="center">
  <h1> Apuntes de Python </h1>
  <sub> Autor:
  <a href="https://www.linkedin.com/in/david-villegas-cl/" target="_blank"> David Villegas</a><br>
  <small> Edición: Mayo, 2024, Chile</small>
</div>

![Banner](../Python_Github_Banner.png)

-----

# Tuplas.

Una tupla es un tipo de dato que permite almacenar una colección ordenada de elementos. A diferencia de las listas, las tuplas son **inmutables**, lo que significa que una vez creadas, no pueden ser modificadas.

Las tuplas se definen utilizando paréntesis() y separando los elementos por comas.

```py
frutas = ('manzana', 'platano', 'naranja')
```

## Caracteristicas de las tuplas.

- Inmutabilidad: No se pueden modificar los elementos de una tupla una vez creada.
- Ordenadas: Los elementos de una tupla mantienen el orden en que se definen.
- Acceso por índice: Se puede acceder a cada elemento de una tupla utilizando su indice, que comience en 0.
- Longitud: Se puede obtener la longitud de una tupla utilizando la función `len()`.
- Operaciones: Se pueden realizar diversas operaciones sobre las tuplas, como la concatenación, la indexación y la verificación de pertenencia.
- Representacion: Las tuplas se representan entre paréntesis, como los elementos separados por comas.

## Casos de uso de las tuplas.

- Almacenar datos que no necesitan ser modificados, como constantes o configuraciones.
- Representa colecciones de datos que no se van a modificar, como coordenadas geográficas o información de contacto.
- Pasar datos como argumentos a funciones.
- Devolver múltiples valores desde una función.

### Tupla vacia

```py
#Syntaxis
tupla_vacia = ()
# Usando constructor de tupla
tupla_vacia = tuple()
```

### Tupla con valores iniciales.
```py
# Syntaxis
tpl = ('item1', 'item2', 'item3')
frutas = ('Platanos', 'Naranjas', 'Mango', 'Limon')
```

### Longitud de una tupla
usaremos el método len() para obtener la longitu de una tupla.

```py
tpl = ('item1', 'item2', 'item3')
len(tpl)
```

### Accediendo a una tupla
 - Indexación positiva de manera similar al tipo de datos de lista, utilizamos indexación positiva o negativa para acceder a elementos de tupla.

```py
# Syntaxis
tpl = ('iem1', 'item2', 'item3')
primer_item = tpl[0]
segundo_item = tpl[1]
```

```py
frutas = ('Platanos', 'Naranjas', 'Mango', 'Limon')
primera_fruta = frutas[0]
segunda_fruta = frutas[1]
ultimo_indice = len(frutas) - 1
ultima_fruta = frutas[las_index]
```

- Indexación negativa. la indexación negativa significa comenzar desde el final, -1 se refiere al último elemento, -2 se refiere al penultimo y el negativo de la longitud de la lista/tupla se refiere al primer elemento.

```py
# Syntaxis
tpl = ('item1', 'item2', 'item3', 'item4')
primer_item = tpl[-4]
segundo_item = tpl[-3]
```
```py
frutas = ('Platano', 'Naranjas', 'Mango', 'Limon')
primera_fruta = frutas[-4]
segunda_fruta = frutas[-3]
ultima_gruta = frutas[-1]
```

### Dividir tuplas.
podemos dividir una subtupla especificando un rango de índice donde comenzar y dónde terminar en la tupla; el valor de retorno será una nueva tupla con los elementos especificados.

- Rango de índice positivo.
```py
# Syntaxis
tpl = ('item1', 'item2', 'item3', 'item4')
all_item = tpl[0:4]
all_item = tpl[0:]
moddle_two_items = tpl[1:3]
```

```py
frutas = ('Platano', 'Naranja', 'Mango' ,'Limon')
all_fruits = frutas[0:4]
all_fruits = frutas[0:]
naranja_mango = frutas[1:3]
naranja_rest = frutas[1:]
```

- Rango de índice negativo.

```py
tpl = ('item1', 'item2', 'item3', 'item4')
all_items = tpl[-4:]
middle_two_items = tpl[-3:-1]
```
```py
fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]    # all items
orange_mango = fruits[-3:-1]  # doesn't include item at index 3
orange_to_the_rest = fruits[-3:]
```

### Cambiar de tuplas a listas.
Existen dos formas para convertir tuplas en listas.

- Utilizando la funcion `list()`: La función `list` crea una nueva lista a partir de un iterable, como una tupla. Es una forma sencilla y rápida de realizar la conversión.

```py
nueva_lista = list(tupla)
``` 

#### Ejemplo:
```py
tupla = ('Elemento1', 'Elemento2', 'Elemento3')
lista_convertida = list(tupla)
print(f'Tupla original: {tupla}')
print(f'Lista convertida: {lista_convertida}')
```

- Usando un bucle `for` se puede utilizar para recorrer la tupla y agregar cada elemento a una nueva lista. Este método es útil si se necesita realizar alguna operación adicional con cada elemento antes de agregarlo a la lista.

  - Diferencia entre los 2 métodos:
    - `list`: Es más rápido y simple para conversiones directas.
    - `bucle`: Ofrece más flexibilidad para realizar operaciones con los elementos antes de agregarlos a la lista.

```py
nueva_lista = []
  for elemento in tupla:
    nueva_lista.append(elemento)
```

#### Ejemplo:

```py
tupla = ('elemento1', 'elemento2', 'elemento3')
lista = convertida = []

for elemento in tupla:
  lista_convertida.append(elemento)

print(f'Tupla original: {tupla}')
print(f'Lista_convertida: {lista_convertida}')
```

### Comprobar un elemento en una tupla.

-----
<div align="center">Code With ❤️ Trebol <div>
<small> Edición: Mayo, 2024</small><br>


<div align="center">
  <a href="https://www.instagram.com/treboldev/" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Instagram&logo=instagram&label=&color=E4405F&logoColor=white&labelColor=&style=for-the-badge" height="25" alt="instagram logo"  />
  </a>
  <a href="https://discord.com/trebol_dev" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Discord&logo=discord&label=&color=7289DA&logoColor=white&labelColor=&style=for-the-badge" height="25" alt="discord logo"  />
  </a>
  <a href="<dpvc.chile@gmail.com>" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Gmail&logo=gmail&label=&color=D14836&logoColor=white&labelColor=&style=for-the-badge" height="25" alt="gmail logo"  />
  </a>
  <a href="https://www.linkedin.com/in/david-villegas-cl/" target="_blank">
    <img src="https://img.shields.io/static/v1?message=LinkedIn&logo=linkedin&label=&color=0077B5&logoColor=white&labelColor=&style=for-the-badge" height="25" alt="linkedin logo"  />
  </a>
  <a href="https://www.facebook.com/VJTrebol.CL" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Facebook&logo=facebook&label=&color=1877F2&logoColor=white&labelColor=&style=for-the-badge" height="25" alt="facebook logo"  />
  </a>
  <a href="https://x.com/treboldev" target="_blank">
    <img src="https://img.shields.io/static/v1?message=Twitter&logo=twitter&label=&color=1DA1F2&logoColor=white&labelColor=&style=for-the-badge" height="25" alt="twitter logo"  />
  </a>
</div>