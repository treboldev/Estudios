<div align="center">
  <h1> Apuntes de Python </h1>
  <sub> Autor:
  <a href="https://www.linkedin.com/in/david-villegas-cl/" target="_blank"> David Villegas</a><br>
  <small> Edición: Mayo, 2024, Chile</small>
</div>

![Banner](Python_Github_Banner.png)
-----

# CADENA DE TEXTO

El texto es un tipo de datos de cadena. Cualquier tipo de datos escrito como texto es una cadena. todos los datos entre comillas simples, dobles o triples son cadenas. Existen diferentes métodos de cadena y funciones integradas para manejar tipos de datos de cadena.


```py
letra = 'P'                       # Una cadena puede ser un solo carácter o un conjunto de texto.
print(letra)                      # P, Imprime el primer caracter de la cadena.
print(len(letra))                 # 1, Cuenta la longitud de la cadena.
saludo = 'Hello, World!'          # La cadena se puede crear usando comillas simples o dobles, 'Hello, World'
print(saludo)                     # Hello, World!
print(len(saludo))                # 13,
```

La cadena multilinea se crea utilizando comillas simples triples `'''` o dobles triples `"""`.
```py
multilinea_srt = '''Este es un string multilinea para validar su funcionalidad, la finalidad de este material es poder simplificar el proceso de aprendizaje de futuros programadores latinos.'''
print(multilinea_srt)

multilinea_string = """Este es un string multilinea para validar su funcionalidad, la finalidad de este material es poder simplificar el proceso de aprendizaje de futuros programadores latinos."""
```
### CONCATENACIÓN DE CADENA

Podemos conectar cadenas entre si. Fusionar o conectar cadenas de llama concatenación.

```py
nombre = 'David'
ap_paterno = 'Villegas'
ap_materno = 'Carreno'
espacio = ' '
nombre_completo = nombre + espacio + ap_paterno + espacio + ap_materno
print(nombre_completo) # David Villegas Carreno
```

### SECUENCIAS DE ESCAPE EN CADENA

En python como en otros lenguajes de programación existen las secuencias de escape.

- `\n:` Nueva linea.
- `\t:` Tabulador significa 8 espacios.
- `\\:` Barra invertida.
- `\':` Una frase.
- `\":` Comillas dobles. 

### INTERPOLACIÓN DE CADENA DE TEXTO

```py
nombre = 'David'
edad = 34
ciudad = 'Santiago'
cadena_formateada = f'Hola, {nombre}. Tienes {edad} años y vives en {ciudad}.'
cadena_final = cadena_formateada
print(cadena_final)

# Imprime Hola, David. Tienes 34 años y vives en Santiago.
```

La interpolación de cadenas en python es un método para insertar valores dentro de cadenas de texto de forma dinámica. esto permite crear cadenas de texto más flexibles y adaptables a diferentes situaciones.

-----

### ACCEDIENDO A CARACTERES EN CADENA POR ÍNDICE

En programación el conteo comienza desde cero. Por lo tanto, la primera letra de una cadena tiene un índice cero y la última letra de una cadena es la longitud de una cadena menos uno.

```py
['P', 'Y', 'T', 'H', 'O', 'N']
# 0    1    2    3    4    5
```

*Ejemplo*

```py
lenguaje = 'Python'
primera_letra = lenguaje[0]
print(primera_letra)                         # Imprime P
segunda_letra = lenguaje[1]
print(segunda_letra)                         # Imprime y
ultimo_indice = len(lenguaje) -1
ultima_letra = lenguaje[ultimo_indice]
print(ultima_letra)                         # Imprime n
```

Si queremos comenzar desde el extremo derecho, podemos usar indexación negativa -1 es el último índice.

```py
lenguaje = 'Python'
ultima_letra = lenguaje[-1]
print(ultima_letra)                       # n
segunda_letra = lenguaje[-2]
print(segunda_letra)                      # o
```

### CORTAR CADENAS

En python podemos dividir cadenas en subcadenas.

```py
lenguaje = 'Python'
cortar_tercera = lenguaje[0:3]    # Extraera los caracter desde el cero hasta el tres.
print(cortar_tercera)             # Imprime Pyt
tres_ultimas = lenguaje[3:6]      # Extrae los caracteres desde el seis hasta el tercero.
print(tres_ultimas)               # Imprime hon
# Inverso
ultimas_tres = lenguaje[-3]
print(ultimas_tres)               # imprime hom         
```

### INVERTIR UNA CADENA

Podemos invertir cadenas facilmente.
```py
saludo = 'Hello, World!'
print(saludo[::-1])               # Imprime !dlroW ,olleH
```

### SALTAR CARACTERES MIENTRAS CORTA

Es posible omitir caractere mientras se corta pasando el argumento del paso al método de corte.

```py
lenguaje = 'Python'
saltos = lenguaje[0:6:2]
print(saltos)                     # Imprime Pto
```
### METODOS DE CADENA

Existen muchos métodos de cadenas que nos permiten formatear cadenas.

#### `capitalize()`:
Convierte el primer caracter de la cadena en mayuscula.

```py
apuntes = 'estos son los apuntes de mi aprendizaje en Python'
print(apuntes.capitalize())         # Estos son los apuntes de mi aprendizaje en Python
```

#### `count()`:
Devuelve la cantidad de caracteres encontrados dentro de la cadena de texto.

```py
desafio = 'este es mi tercer dia aprendiendo Python'
print(desafio.count('e'))         # Imprime 7
print(desafio.count('e', 7, 14))  # Imprime 1
print(desafio.count('er'))        # imprime 2
```

 #### `endswitch()`:
 Comprueba si una cadena termina con un final especifico.

 ```py
 desafio = 'aprendiendo Python'
 print(desafio.endswitch('on'))    # True
 print(desafio.endswitch('tion'))  # False
 ```

 #### `expandtabs()`
 Se utiliza para reemplazar las tabulaciones `\t` por espacios en blanco `( )`. Esta función toma como argumento opcional el tamaño de tabulación. Si no se especifica el tamaño de tabulación, se utiliza el valor predeterminado de 8 espacios.
 ```py
desafio = 'Este\ttexto\ttiene\ttabulaciones.'
print(desafio.expandtabs())        # Este    texto   tiene   tabulaciones.
print(desafio.expandtabs(10))      # Este      texto     tiene     tabulaciones.
 ```


 #### `find()`
 Se utiliza para encontrar la primera aparición de una subcadena (substring) dentro de una cadena original. Este método devuelve la posición del primer carácter de la subcadena dentro de la cadena original. Si la subcadena no se encuentra, el método devuelve -1.

```py
cadena = 'Hola, mundo!'
subcadena = 'mundo'
posicion = cadena.find(subcadena)
if posicion == -1:
  print('No se encontró la subcadena')
else:
  print('La subcadena se encontró en la posición:', posicion)
```

 #### `rfind()`
 Se utiliza para encontrar la última aparición de una subcadena dentro de una cadena. A diferencia del método find(), que busca la primera aparición de la subcadena, rfind() busca desde el final de la cadena hacia la izquierda.

```py
cadena = 'Hola, mundo!'
# Busca la última aparición de la letra 'o'
ultima_o = cadena.rfind('o')
print(ultima_o)                     # Salida: 7

# Busca la última aparición de la subcadena 'mundo'
ultima_palabra = acdena.rfind('mundo')
print(ultima_palabra)               # Salida: 6

# Busca la última aparición de la letra 'o' desde la posición 5
ultima_o_desde_5 = cadena.rfind('o', 5)
print(ultima_o_desde_5)            # Salida: 7

# Busca la última aparición de la subcadena 'mundo' hasta la posición 10
ultima_palabra_hasta_10 = cadena.rfind('mundo', 0, 10)
print(ultima_palabra_hasta_10)    # Salida: -1
```

 #### `format()`
 Se utiliza para formatear cadenas de texto de manera flexible y poderosa. Permite insertar valores, aplicar formato numérico y de cadenas, y crear cadenas con una sintaxis clara y legible.

 ```py
 nombre = 'Juan'
 edad = 30

 # Formateo usando índice numérico
 cadena_formateada = f'Hola, {nombre} tienes {edad} años.'
 print(cadena_formateada)       # Salida: Hola, Juan tienes 30 años.

 # Formateo usando nombre de argumento
 cadena_formateada = f'Hola, {nombre=Juan} tienes {edad=30} años.'
 print(cadena_formateada)       # Salida: Hola, Juan tienes 30 años.
 ```

 #### `index()`
 Es un método de la clase `list` que se utiliza para encontrar el índice (posición) de la primera aparición de un elemento específico dentro de una lista.

 ```py
 # Ejemplo 1: busca el índice del elemento 'manzana' en una lista
 frutas = ['manzana', 'banana', 'naranja', 'manzana']

 indice_manzana1 = frutas.index('manzana')
 print(indice_manzana1)       # Salida: 0

 # Ejemplo 2: Buscar el índice del elemento 'manzana' a partir del índice 2
 indice_manzana2 = frutas.index('manzana', 2)
 print(indice_manzana2)       # Salida: 3

 # Ejemplo 3: Buscar el índice del elemento 'pera' (que no está en la lista)
 try:
  indice_pera = frutas.index('pera')
  except ValueError as e:
    print(e)                  # Salida: ValueError: 'pera' is not in list
 ```

 #### `rindex()`
 El metodo `rindex()` (abreviatura de "right index") de las cadenas en python se utiliza para encontrar la última aparición de una subcadena dentro de una cadena principal. A diferencia del método `find()`, que devuelve el índice de la primera aparación de la subcadena, `rindex()` devuelve el índice de la última aparición.

 ```py
 cadena = 'Hola, mundo! Mundo, hola!'
 # Encontrar la última aparición de 'mundo' en toda la cadena
 ultima_aparicion = cadena.rindex('mundo')
 print(ultima_aparicion)      # Salida: 17

 # Encontrar la última aparición de 'mundo' a partir del índice 10
 ultima_aparicion = cadena.rindex('mundo', 10)
 print(ultima_aparicion)      # Salida: 17

 # Buscar la última aparición de 'mundo' en un rango específico
 ultima_aparicion = cadena.rindix('mundo', 5, 15)
 print(ultima_aparicion)      # Salida: 12

 # Buscar una subcadena que no existe
try:
  ultima_aparicion = cadena.rindex('adios')
  except ValueError:
    print("La subcadena 'adios' no se encuentra en la cadena")
 ```

 #### `isalnum()`
 El método `isalnum` en python se utiliza para verificar si una cadena está compuesta **exclusivamente** para caracteres alfanuméricos. Esto significa que la cadena solo puede contener letras (minúsculas o mayúsculas) y números (del 0 al 9). El método devuelve un valor booleano.

 ```py
 cadena1 = 'Hola123'
 cadena = 'Hola@mundo'

 print(cadena1.isalnum())         # Salida: True
 print(cadena2.isalnum())         # Salida: False
 ```

 #### `isalpha()`
 El método `isalpha()` en Python se utiliza para verificar si una cadena dada está compuesta exclusivamente por caracteres alfabéticos (letras mayúsculas y minúsculas).

 ```py
 # Ejemplos que devuelven True:
 print('Hola'.isalpha())              # True
 print('mI_Nombre'.isalpha())         # True

 # Ejemplos que devuelven False:
 print('123'.isalpha())               # False
 print('¿Qué tal?'.isalpha())         # False
 print(' '.isalpha())                 # False
 ```

 #### `isdecimal()`
 Comprueba si todos los caracteres de una cadena son decimales (0-9)
 
 ```py
 desafio = 'Hola como estas'          # False
 print(desafio.isdecimal())           

 desafio = '123'                      # True
 print(desafio.isdecimal())           

 desafio = '\u00B2'                   # False
 print(desafio.isdecimal())

 desafio = '12 3'                     # False
 print(desafio.isdecimal())
 ```

 #### `isdigit()`
 Comprueba si todos los caracteres de una cadena son números (0-9 y algunos otros caracteres Unicode para numeros).

 ```py
 desafio = 'Cadena de texto'          # False
 print(desafio.isdigit())             

 desafio = '30'                       # True
 print(desafio.isdigit())

 desafio = '\u00B'                    # Flase
 print(desafio.isdigit())             
 ```

 #### `isnumeric()`
 El método se utiliza para verificar si una cadena de texto dada contiene únicamente caracteres numéricos. Este funciona dentro de las cadenas de caracteres y no con números directamente.

 ```py
 cadena1 = '12345'
 cadena2 = 'HolaMundo'
 cadena3 = '-10.5'

 print(cadena1.isnumeric())   # True
 print(cadena2.isnumeric())   # False
 print(cadena3.isnumeric())   # False
 ```

 #### `ididentifier()`
 El metodo `isidentifier()` se utiliza para verificar si una cadena de caracteres es un identificador válido. Un identificador es un nombre que se utilizara para representar variables, funciones, clases y otrolos elementos del lenguaje.

 ```py
 nombre = 'miVariable'
 if nombre.isidentifier():
  print(f'{nombre} es un identificador válido.')
else:
  print(f'{nombre} no es un identificador válido.')
 ```

 #### `islower()`
 Se utiliza para verificar si todos los caracteres alfabéticos (letras) en una cadena de texto están en minúscula.

 ```py
 texto = 'este texto está en minúscula'
 if texto.islower():
  print(f'{texto} está en minuscula.')
else:
  print(f'{texto} no está en minúscula.')
 ```

 #### `isupper()`
 El método `isupper()` en python se utiliza para verificar si todos los caracteres alfabéticos (letras) en una cadena de texto están en mayúscula.

 ```py
 texto = 'ESTE TEXTO ESTÁ EN MAYÚSCULA.'
 if texto.isupper():
  print(f'{texto} está en mayúscula.')
else:
  print(f'{texto} no está en mayúscula.')
 ```

 #### `join()`
 El método `join()` se utiliza para unir elementos de un iterable (una secuencia de valores) en una cadena de texto, utilizando un separador especificado. 

 ```py
 #Unir una lista de palabras con una coma(,) como separador.
 palabras = ['Hola', 'mundo', 'cómo', 'estás']
 cadena_unida = ','.join(palabras)
 print(cadena_unida)                    # Salida: Hola,mundo,cómo,estás

 #Unir una tupla de números con guion (-) como separador.
 numeros = (1, 2, 3, 4, 5)
 cadena_unida = '-'.join(str(numero) for numero in numeros)
 print(cadena_unida)                    # Salida: 1-2-3-4-5

 #Unir un conjunto de caracteres con espacio en blanco como separador.
 caracteres = {'a', 'b', 'c', 'd', 'e'}
 cadena_unida = ' '.join(caracteres)
 print(cadena_unida)                    # Salida: a b c d e
 ```

 #### `strip()`
El método `strip()` en python se utiliza para eliminar los espacios en blanco (incluyendo tabulaciones, saldtos de línea y otros caracteres invisibles) de ambos extremos (inicio y final) de una cadena de texto. También se puede utilizar para eliminar caracteres especificos del inicio y final de la cadena.

```py
# Eliminar espacios en blanco de ambos extremos.
texto_con_espacios = ' Hola Mundo   '
texto_sin_espacios = texto_con_espacios.strip()
print(f'Texto original: {texto_con_espacios}')
print(f'Texto sin espacios: {texto_sin_espacios}')

# Eliminar guiones (-) del inicio y final.
texto_con_guiones = '-Hola-Mundo-'
texto_sin_guiones = texto_con_guiones.strip('-')
print(f'Texto original: {texto_con_guiones}')
print(f'Texto sin guiones: {texto_sin_guiones}')

# Eliminar espacios en blanco y caracteres especificos.
texto_con_caracteres = '*Hola Mundo*'
texto_sin_caracteres = texto_con_caracteres.strip('*')
print(f'Texto original: {texto_con_caracteres}')
print(f'Texto sin caracteres: {texto_sin_caracteres}')
```

 #### `replace()`
 El método `replace()` en python se utiliza para reemplazar todas las ocurrencias de subcadena especifíca por otra subcadena dentro de una cadena de texto. Es una herramienta muy útil para modificar cadenas de texto de manera eficiente.

 ```py
 # Reemplazar todas las ocurrencias de 'hola' por 'mundo'
 texto_original = 'Hola, hola que tal, hola de nuevo'
 texto_modificado texto_original.replace('hola', 'mundo')
 print(f'Texto original: {texto_original}')
 print(f'texto modificado: {texto_modificado}')

 # Reemplazar solo la primera ocurrencia de "hola" por "mundo"
texto_original = "Hola, hola que tal, hola de nuevo"
texto_modificado = texto_original.replace("hola", "mundo", 1)
print(f"Texto original: {texto_original}")
print(f"Texto modificado: {texto_modificado}")

# Reemplazar caracteres especiales por representaciones HTML
texto_con_caracteres = "Este texto tiene &lt;caracteres especiales&gt;"
texto_html = texto_con_caracteres.replace("<", "&lt;").replace(">", "&gt;")
print(f"Texto original: {texto_con_caracteres}")
print(f"Texto HTML: {texto_html}")
 ```

 #### `split()`
 El método `split()` se utiliza para dividir una cadena de texto de una lista de subcadenas, utilizando un seprador especificado. Es una herramienta muy útil para trabajar con cadenas de texto de manera eficiente.

 ```py
 # Dividir una cadena por espacios en blanco
texto = "Hola mundo, cómo estás"
palabras = texto.split()
print(f"Palabras: {palabras}")

# Dividir una cadena por comas
frase = "Los mejores lenguajes de programación, según yo: Python, Java, C++"
lenguajes = frase.split(", ")
print(f"Lenguajes de programación: {lenguajes}")

# Dividir una cadena por un caracter específico
cadena_con_numeros = "A1B2C3D4"
numeros = cadena_con_numeros.split("A")
print(f"Números: {numeros}")

# Limitar el número de divisiones
texto_largo = "Esta es una cadena de texto muy larga que queremos dividir en partes más pequeñas."
partes = texto_largo.split(" ", 3)  # Dividir en máximo 3 partes por espacio
print(f"Partes del texto: {partes}")
 ```

 #### `title()`
El método `title()` se utiliza para convertir la primera letra de cada palabra en una cadena de texto a mayúscula, y el resto de las letras a minúsculas. Es una herramienta util para formatear titulos, nombres propios y otras cadenas de texto para que tengan un aspecto más formal.

```py
# Convertir un título a formato de título
titulo_original = "mi primer programa en python"
titulo_formateado = titulo_original.title()
print(f"Título original: {titulo_original}")
print(f"Título formateado: {titulo_formateado}")

# Convertir nombres propios a formato de título
nombre = "maria pérez gonzález"
nombre_formateado = nombre.title()
print(f"Nombre original: {nombre}")
print(f"Nombre formateado: {nombre_formateado}")

# Convertir una oración a formato de título
oracion = "esta oración no tiene título."
oracion_formateada = oracion.title()
print(f"Oración original: {oracion}")
print(f"Oración formateada: {oracion_formateada}")
```

 #### `swapcase()`

 El método `swapcase()` se utiliza para cambiar el caso de todas las letras en una cadena de texto. Es decir, convierte las letras minúsculas en mayúsculas y las mayúsculas en minúsculas.

 ```py
 # Invertir el caso de una frase
frase_original = "Esta es una frase en mayúscula y minúscula."
frase_invertida = frase_original.swapcase()
print(f"Frase original: {frase_original}")
print(f"Frase con caso invertido: {frase_invertida}")

# Invertir el caso de una palabra
palabra = "Python"
palabra_invertida = palabra.swapcase()
print(f"Palabra original: {palabra}")
print(f"Palabra con caso invertido: {palabra_invertida}")

# Invertir el caso de caracteres especiales
texto_con_especiales = "EjEmpl0 d3 t3Xt0 c0n c4r4ct3r3s 3sp3c1@l3s."
texto_invertido = texto_con_especiales.swapcase()
print(f"Texto original: {texto_con_especiales}")
print(f"Texto con caso invertido: {texto_invertido}")
 ```

 #### `startswith()`
 Este método verifica si una cadena de texto comienza con otra subcadena especifica. Devuelve `True` si la acdena original comienza con la subcadena especificada, y `False` en caso contrario.

 ```py
texto = "Hola, mundo!"
print(texto.startswith("Hola"))  # Salida: True
print(texto.startswith("Mundo"))  # Salida: False
 ```


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