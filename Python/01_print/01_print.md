![Banner](/Python/Python_Github_Banner.png)


<div align="center"><h2>Función Print</h2></div>

La función `print()` es una función básica y versátil que se utiliza para mostrar texto en consola. Es una de las primeras funciones que se aprende al comenzar a programar con Python, y se utiliza en casi todos los programas. 

*Sintaxis básica:*

```py 
print("Hola, Mundo!")
```
Este código imprimirá el texto "Hola, Mundo!" en la consola.

*Argumentos:*

La función `print()` puede tener varios argumentos, que controlan lo que se imprime y cómo se formatea. Los argumentos más comunes son:

-   *Cadenas de texto:* Se imprimen tal cual están escritas.
-   *Variables:* Se imprime el valor de la variable.
-   *Expresiones:* Se evalúa la expresión y se imprime el resultado.
-   *Separadores:* Se utilizan para separar los argumentos. El separador por defecto es un espacio, pero se puede cambiar utilizando el argumento `sep`.
-   *Fin de línea:* Determina lo que se imprime al final de la línea. El valor por defecto es una nueva línea `(\n)`, pero se puede cambiar utiliznado el argumento `end`.

*Ejemplos:*

```py
print("Hola", "Mundo!")             # Imprime "Hola Mundo!".
print(10)                           # Imprime el número 10.
print(10 + 5)                       # Imprime el resultado de la suma (15).
print("El resultado es:", 10 + 5)   # Imprime "El resultado es: 15".
print("Valor:", variable)           # Imprime el valor de la variable "variable".
print("------------------------")   # Imprime una linea de guiones.
```

## Formateo de cadenas

Python proporciona un método flexible para formatear cadenas de texto utiliando la función `f-strings`. Esto permite insertar variables y expresiones directamente en la cadena de texto.

*Ejemplo:*

```py
nombre = "Juan"
edad = 30

print(f"Hola, {nombre}! Tienes {edad} años.") #Imprime "Hola, Juan! Tienes 30 años."
```

*Conclusión:*
La función `print` es una herramienta esencial en Python para mostrar información al usuario y depurar el código. Con su sintasis simple y sus potentes opciones de formateo, es una función que se utiliza en todos los niveles de programación.