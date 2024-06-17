![Banner](../Python_Github_Banner.png)


<div align="center"><h2>Condicionales</h2></div>

Las sentencias condicionales en Python permiten controlar el flujo de un programa en función de la evaluación de una condición. Son una herramienta esencial para tomar decisiones y ejecutar diferentes acciones según se cumplan o no ciertas condiciones.

### ***Tipos de sentencias condicionales:***

Existen tres tipos principales de sentencias condicionales en Python:

- ***Sentencia `if`***: La sentencia `if` es la más básica y se utiliza para verificar una sola condición. Si la condición se evalúa como `True`, se ejecuta un bloque de código. Si la condición se evalúa como `False`, se ejecuta un bloque de código opcional `else`.

```py
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

- ***Sentencia `if-elif-else`***: La sentencia `if-elif-else` permite evaluar varias condiciones anidadas. Se utiliza la palabra clave `elif` para agregar más condiciones a la sentencia `if`. Si ninguna de las condiciones `if` o `elif` se evalúa como `True`, se ejecuta el bloque de código `else` (Si está presente).

```py
calificacion = 70

if calificacion >= 70:
    print("Excelente")
elif calificacion >= 60:
    print("Muy Bien")
elif calificacion >= 50:
    print("Bien")
else:
    print("Debes estudiar mas!")
```

- ***Sentencia `switch`: Sentencia no nativa, aunque Python no tiene una sentencia `switch` nativa, se puede utilizar la libreria `enum` o la función `getattr()` para crear una funcionalidad similar a la de `switch`.

```py
from enum import Enum

class Operacion(Enum):
    SUMA = 1
    RESTA = 2
    MULTIPLICACION = 3
    DIVISION = 4

operacion = Operacion.SUMA
numero1 = 10
numero2 = 5

resultado = None

if operacion == Operacion.SUMA:
    resultado = numero1 + numero2
elif operacion == Operacion.RESTA:
    resultado = numero1 - numero2
elif operacion == Operacion.MULTIPLICACION:
    resultado = numero1 * numero2
elif operacion == Operacion.DIVISION:
    resultado = numero1 / numero2

if resultado is not None:
    print(f"El resultado de la operación {operacion.name} es: {resultado}.")
else:
    print("Operación no válida.")
```

#### ***Operadores lógicos:***

Las sentencias condicionales en Python utilizan operadores lógicos para evaluar las condiciones. Los operadores lógicos más comunes son:

- `and`: Evalúa si ambas condiciones son `True`.
- `or`: Evalúa si al menos una de las condiciones es `True`.
- `not`: Invierte el valor de la condicion.

##### ***Ejemplo de uso de operadores lógicos:

```py
edad = 17
tiene_credencial = True

if edad >= 18 or tiene_credencial:
    print("Puedes entrar al evento.")
else:
    print("No puedes entrar al evento.")
```