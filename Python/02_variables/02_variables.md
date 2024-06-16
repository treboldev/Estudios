![Banner](/Python/Python_Github_Banner.png)

<div align="center"><h2>Variables</h2></div>

Las variables en Python son elementos fundamentales del lenguaje que permiten almacenar y manipular datos. Son contenedores con nombre que pueden guardar información de diferentes tipos, como números, cadenas de texto, booleanos y listas.

### *¿Cómo se declaran las variables?*

En python, no es necesario declarar explicitamente el tipo de dato de una varibale antes de asignarle un valor. El tipo de dato se infiere automaticamente a partir del valor asignado.

Para declarar una varibale, simplemente se utiliza el operador de asignacion `(=)` seguido del nombre de la variable y el valor que se le quiere asignar:

```py
nombre = "Juan"
edad = 30
pi = 3.14159
esta_lloviendo = True
numeros = [1, 2, 3, 4, 5]
```

En este ejemplo, se han creado variables con los nombres `nombre`, `edad`, `py`, `esta_lloviendo` y `numeros`. Cada una de ellas almacena un tipo de dato diferente: una cadena de texto, un número entero, un número decimal, un valor booleano y una lista de números, respectivamente.

### *¿Como se usan las variables?*

Una vez que se ha declarado una variable, se puede usar su nombre para referirse al valor almacenado en ella. Esto se puede hacer en expresiones, asignaciones a otras variables, funciones, etc.

*Ejemplo:*

```py
# Imprimiendo el valor de la variable "nombre"
print(nombre)

# Calculando la edad en 5 años
edad_en_5_años = edad + 5
print(f"Edad en 5 años: {edad_en_5_años}")

# Comprobando si esta lloviendo
if esta_lloviendo:
    print("¡Lleva un paraguas!")
else:
    print("¡Disfruta del sol!")
```

### *¿Qué tipos de variables existen?*

Python admite una amplia variedad de tipos de variables, cada uno con sus propias caracteristicas y usos:

- ***Numeros:*** Pueden ser enteros `(int)`, decimales `(float)` o complejos `(complex)`.
  
- ***Booleanos:*** Representan valores lógicos de verdad o falsedad (`True` o `False`).
  
- ***Listas:*** Son colecciones ordenadas de elementos de cualquier tipo.
  
- ***Tuplas:*** Son colecciones inmutables (no se pueden modificar) de elementos de cualquier tipo.
  
- ***Diccionarios:*** Son colecciones no ordenadas de pares clave-valor.
  
- ***Conjuntos:*** Son colecciones no ordenadas de elementos únicos.

### *Recomendaciones para usar variables:*

- ***Elegir nombres descriptivos:*** Es importante elegir nombres de variables que sean claros y descriptivos del dato que almacenan. Esto facilita la lectura y comprensión del código.
  
- ***Utilizar convenciones de nomenclatura:*** Existen diferentes convenciones de nomenclatura para nombrar variables en python. es recomendable seguir una convención consistente para mejorar la legibilidad del código.
  
- ***Evitar usar variables globales:*** Las variables globales son accesibles desde cualquier parte del programa. Su uso excesivo puede dificultar la lectura y el mantenimiento del código.
  
- ***Documentar el código:*** Es importante documentar el código para explicar el proposito de las variables y cómo se utilizan.