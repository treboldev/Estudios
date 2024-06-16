![Banner](/Python/Python_Github_Banner.png)

<div align="center"><h1>Cadenas de texto</h2></div>

Las cadenas de texto (strings en inglés) son uno de los tipos de datos básicos en Python. Se utilizan para representar secuencias de caracteres, como palabras, frases, oraciones o cualquier tipo de texto. En python, las cadenas de texto se definen entre comillas simples `('')` o comillas dobles `("")`.

```py
# Ejemplo de cadenas de texto simples
cadena1 = 'Hola, Mundo!'
cadena2 = "Este es un ejemplo de cadena de texto."
cadena3 = "Se pueden usar comillas simples o dobles."
```

### ***Acceso a caracteres:***
Se puede acceder a caracteres individuales de una cadena de texto utilizando el operador de índice `([])`. El indice comienza en 0, y se puede acceder al último carácter usando la longitud de la cadena menos 1.

```py
cadena = "Hola, mundo!"

# Accediendo al primer caracter.
primer_caracter = cadena[0]             # 'H'

# Accediendo al último carácter. 
ultimo_caracter = cadena[-1]           # '!'

# Accediendo a un rango de caracteres. 
subcadena = cadena[3:6]                 # 'o mu'
```

### ***Operaciones de cadenas de texto***

Python ofrece una amplia gama de operaciones que se pueden realizar con cadenas de texto, incluyendo:

- ***Concatenación:*** Unir dos o más cadenas de texto.
- ***Repetición:*** Repetir una cadena de texto un número específico de veces.
- ***Interpolación:*** Insertar variables o expresiones dentro de una cadena de texto.
- ***Reemplazo:*** Reemplazar un patrón o subcadena dentro de una cadena de texto.
- ***Mayúsculas y minúsculas:*** Convertir una cadena de texto a mayúsculas o minúsculas.
- ***Eliminación de espacios:*** Eliminar espacios en blanco al inicio o final de una cadena de texto.
- ***División***: Dividir una cadena de texto en una lista de subcadenas según un delimitador.

### ***Funciones de cadenas de texto:***

Python proporcionan una biblioteca de funciones integradas para trabajar con cadenas de texto. Algunas de las funciones más comunes son:

- `len(cadena)`: Devuelve la longitud de una cadena de texto.
- `upper(cadena)`: Convierte una cadena de texto en mayúsculas.
- `lower(cadena)`: Convierte una cadena de texto en minúsculas.
- `strip(cadena)`: Elimina espacios en blanco al inicio y final de una cadena de texto.
- `find(cadena1, cadena2)`: Busca la primera aparición de una subcadena dentro de otra cadena de texto.
- `replace(cadena1, cadena2, cadena3)`: Reemplaza todas las apariciones de una subcadena por otra subcadena dentro de una cadena de texto.
- `split(cadena, separador)`: Divide una cadena de texto en una lista de subcadenas según un delimitador.

### ***Secuencia de escape en cadena***

El escape de cadenas en Python es un mecanismo que se utiliza para representar caracteres especiales o secuencias de caracteres que no se interpretan literalmente dentro de una cadena de texto. Esto es útil para evitar confusiones o errores cuando se trabaja con cadenas que contienen caracteres que tienen un significado especial en el lenguaje.

#### ***¿Cuándo se necesita escapar una cadena?***

Se debe escapar una cadena en Python cuando continie alfuno de los siguientes caracteres:

- ***Comillas simples `('')`***: Se utilizan para delimitar cadenas de texto, por lo que si se quieren incluir dentro de una cadena, hay que escaparlas.
- ***Comillas dobles `("")`***: Similar a las comillas simples, se utilizan para delimitar cadenas de texto y necesitan escaparse si se quieren incluir dentro de una cadena.
- ***Barra invertida `(\)`***: Se utilizan para escapar otros caracteres especiales, por lo que si se quiere incluir una barra invertida literal, hay que escaparla.
- ***Barra de carro `(\r)`***: Marca el final de una línea en Windows.
- ***Salto de línea `(\n)`***: Marca el final de una línea en la mayoria de los sistemas operativos.
- ***Tabulador `(\t)`***: Inserta un tabulador.
- ***Campana `(\a)`***: Reproduce un sonido de campana.
- ***Retroceso `(\b)`***: Mueve el cursor un espacio hacia atrás.
- ***Alimentación de formulario `(\f)`***: Inserta un nuevo folio en una impresora.