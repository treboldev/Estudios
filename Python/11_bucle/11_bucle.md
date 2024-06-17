![Banner](../Python_Github_Banner.png)


<div align="center"><h2>Bucles</h2></div>

Los bucles en python son estructuras de control que permiten ejecutar un bloque de código repetidamente hasta que se cumpla una condición específica. Son herramientas esenciales para automatizar tareas repetitivas y procesar colecciones de datos.

### ***Tipos de bucle en Python***

Existen dos tipos principales de bucles en Python:

- ***Bucle `for`***: El bucle `for` se utiliza para iterar sobre una secuencia de elementos, como una lista, tupla o cadena. En cada iteración, la variable de control del bucle toma el valor de un elemento de la secuencia.

```py
# Recorrer una lista de nombres
nombres = ["Juan", "Maria", "Pedro", "Ana"]

for nombre in nombres:
    print(nombre)
``` 

- ***Bucle `while`***: El bucle `while` se utiliza para ejecutar un bloque de código mientras una condición se evalúa como `True`. La condición se evalúa al incio de cada iteración, y si es `False`, el bucle termina.

```py
# imprimir números del 1 al 10
contador = 1
while contador <= 10:
    print(contador)
    contador +=1
```

### ***Sentencias de control dentro de bucles:***

Las sentencias de control, como `break` y `continue`, se pueden utilizar dentro de los bucles para modificar su comportamiento:

- ***`break`***: Termina el bucle inmediatamente y sale de la iteración actual.
- ***`continue`***: Salta a la siguiente iteración del bucle, omitiendo el resto del código en la iteración actual.

```py
# Recorrer una lista de números y detenerse al encontrar un numero impar
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in numeros:
    if numero % 2 != 0:
        print(f"Número impar encontrado: {numero}")
        break
```

### ***Bucles anidados***

Los bucles anidados se pueden anidar, es decir, un bucle puede contener otro bucle dentro de él. Esto permite realizar iteraciones más complejas sobre estructuras de datos miltidimensionales. 

```py
# Imprimir una tabla de multiplicar
for numero in range(1, 11):
    print(f"Tabla del {numero}:")
    for multiplicador in range(1, 11):
        resultado = numero * multiplicador
        print(f"{numero} x {multiplicador} = {resultado}")
```