<div align="center">
  <h1> Apuntes de Python </h1>
  <sub> Autor:
  <a href="https://www.linkedin.com/in/david-villegas-cl/" target="_blank"> David Villegas</a><br>
  <small> Edición: Mayo, 2024, Chile</small>
</div>

![Banner](../Python_Github_Banner.png)

# VARIABLES

Las variables son elementos fundamentales en la programación que permite almacenar y manipular datos de un programa. En python, las variables se caracterizan por su simplicidad y flexibilidad.

***CREACION Y ASIGNACIÓN***

- Para crear una variable, se utiliza el operador `(=)` seguido del nombre de la variable y el valor que se le debe asignar.
- La sintaxis básica es: `nombre_variable = valor`
- El nombre de la variable debe seguir las convenciones de nomenclatura de python, utilizando letras minúsculas, números y guiones bajos.
- El valor puede ser de cualquier tipo de datos compatible con python, como números enteros `(int)`, números decimales `(float)`, cadenas de texto `(str)`, valores booleanos `(bool)` o listas `(list)`.

***VALORES NO PERMITIDOS***

- first-name
- first@name
- first$name
- num-1
- 1num

***Ejemplo declaración de variables***

```py
edad = 25 # Variable de tipo entero.
nombre = David # Variable de tipo cadena de texto (string).
esta_lloviendo = True # Variable de tipo booleana.
temperatura = [22, 25, 23] #Variable de tipo lista.
```

*Tambien se pueden declarar múltiples variables en una linea*.

***Ejemplo:***

```py
nombre, apellido_ap, pais, edad, es_casado = 'David', 'Villegas', 'Chile', 34, False.
print(nombre, apellido_ap, edad, es_casado)
```

### EJERCICIOS REALIZADOS CON LA UNIDAD
```
- Declara una variable de nombre y asignale valor
- Declarar variable apellido y asignale valor.
- Declara una variable de nombre completo y asignale valor.
- Declara una variable país y asignale valor.
- Declara una variable ciudad y asignale valor.
- Declara una variable edad y asignale valor.
- Declara una variable año y asignale valor.
- Declara una varibale es_casado y asignale valor.
- Declara multiples variables en una linea y asignale valor.
- Concatena y agrega texto acorde a las variables para formar una oracion con ellas.

# EJERCICIO 2

- Verifique el tipo de datos de sus variables.
- Calcule la longitud de su nombre usando la función len().
- Calcule la longitu de su nombre completo.
- Declare las siguientes variables 10 como num_one y 8 como num_two
    - suma num_one y num_two y asignele valor a una variable total.
    - reste num_two de num_one y asignele el valor a una variable diff.
    - Multiplique el valor num_two y num_one y asignele valor.
    - Divide num_two por num_one y asignele valor a la variable.
- Utilice la funcion input para obtener el nombre, apellido, pais y edad de un usuario y almacenar el valor en sus variables correspondientes.
```


- [Resolución con variables](01_variable_ejercicios.py)

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