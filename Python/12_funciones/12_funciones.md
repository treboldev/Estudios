![Banner](../Python_Github_Banner.png)


<div align="center"><h2>Funciones</h2></div>

Las funciones en python son bloques de código reutilizables que se utilizan para realizar tareas específicas. Permiten modularizar el código, hacerlo más legible y evitar la dupliación de código. Las funciones pueden recibir argumentos (datos de entrada) y devolver valores (datos de salida).

### ***¿Cómo se crean las funciones?***

La sintaxis para crear una función de Python es la siguiente:

```py
def nombre_funcion(parametro1, parametro2):
    """ Documentación de la función (opcional1)
    Cuerpo de la función
    """
    return valor_de_retorno
```

##### ***Ejemplo de creación de una función:***

```py
def saludar(nombre):
    """
    Función que saluda a una persona por su nombre. 

    Parámetros:
        nombre: El nombre de la persona a saludar. 
    
    Ejemplo de uso:
        Saludar("Juan")
    """
    print(f"¡Hola {nombre}!")

# Llamada a la función
saludar("Maria")
```

### ***¿Cómo funcionan los parámetros de las funciones?***

Los parámetros de las funciones se definen entre paréntesis después del nombre de la función. Cada parámetro tiene un nombre y un tipo opcional. Al llamar a la función, se deben proporcionar argumentos que coincidan con los parámetros definidos.

##### ***Ejemplo de uso de parámetros:***

```py
def sumar(numero1, numero2):
    """
    Funcion que suma dos números. 

    Parámetros:
        numero1: El primer número a sumar. 
        numero2: El segundo número a sumar. 

    Ejemplo de uso:
        resultado = sumar(10, 5)
        print(resultado)            # 5
    """
    return numero1 + numero2

resultado = sumar(20, 3)
print(resultado)                    # 23
```

### ***¿Cómo se devuelven valores desde las funciones?***

Las funciones pueden devolver valores utilizando la palabra clave `return`. El valor devuelto puede ser cualquier tipo de dato en Python.

##### ***Ejemplo de uso de la sentencia `return`:***

```py
def calcular_area_cuadrado(lado):
    """
    Función que calcula el área de un cuadrado.

    Parámetros:
        lado: La longitud de un lado del cuadrado.

    Ejemplo de uso:
        area = calcular_area_cuadrado(5)
        print(area)     # 25
    """
    return lado * lado

area = calcular_area_cuadrado(7)
print(area)                     # 49
```

### ***¿Qué son las funciones sin retorno?***

Las funciones sin retorno no devuelven ningún valor explicitamente. Se utilizan principalmente para realizar acciones o modificar variables globales.

##### ***Ejemplo de una función sin retorno:***

```py
def imprimir_mensaje():
    """
    Función que imprime un mensaje en la consola. 
    """
    print("¡Esta es una funcion sin retorno!")

imprimir_mensaje()          # ¡Esta es una función sin retorno!
```