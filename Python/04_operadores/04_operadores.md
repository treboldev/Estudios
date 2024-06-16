![Banner](/Python/Python_Github_Banner.png)

<div align="center"><h1>Operadores</h2></div>

En python, los operadores son simbolos que se utilizan para realizar operaciones con valores o variables. Se pueden clasificar en diferentes grupos según el tipo de operación que realizar:

### ***Operadores aritmeticos:***

- Suma `+`.
- Resta `-`.
- Multiplicación `*`.
- División `/`.
- División entera (cociente) `//`.
- Residuo `%`.
- Potencia `**`.

```py
# Operadores aritméticos

resultado = 10 + 5          # Suma
resta = 15 - 4              # Resta
multiplicación = 3 * 2      # Multiplicación
division = 16 / 4           # División
residuo = 10 % 3            # Residuo
```

### ***Operadores de comparación:***

- Igualdad `==`.
- Desigualdad `!=`.
- Menor que `<`.
- Menor o igual que `<=`
- Mayor que `>`.
- Mayor o igual que `>=`

```py
# Operadores de comparación

es_igual = 10 == 10         # Igualdad
es_distinto = 5 != 3        # Desigualdad
es_menor = 2 < 7            # Menor que
es_mayor = 15 > 10          # Mayor que
```

### ***Operadores de lógicos:***

- Y lógico `and`.
- O lógico `or`.
- No lógico `not`.

```py
# Operadores lógicos

esta_lloviendo = True
tiene_hambre = False

si_esta_lloviendo_y_tiene_hambre = esta_lloviendo and tiene_hambre  # Y Lógico.
si_esta_lloviendo_o_tiene_hambre = esta_lloviendo or tiene_hambre # O Lógico.
no_esta_lloviendo = not esta_lloviendo # NO Lógico. 
```

### ***Operadores de pertenencia:***

- Pertenencia a un conjunto `in`.
- No pertenencia a un conjunto `noy in`.

```py
frutas = ["Manzana", "Platano", "Pera"]
esta_en_la_lista = "Manzana" in frutas      # Pertenencia. 
no_esta_en_la_lista = "Uva" not in frutas   # No pertenencia.
```

### ***Operadores de identidad:***

- Identidad (mismo objeto) `is`.
- No identidad (Distintos objetos) `not in`.

```py
objeto1 = [1, 2, 3]
objeto2 = [1, 2, 3]

mismo_objeto = objeto1 is objeto2           # Identidad. 
distinto_objeto = objeto1 is not objeto2    # No identidad. 
```

### ***Operadores de asignación:*** 

- Asignación simple: `=`.
- Asignación aditiva: `+=`.
- Asignación sustractiva: `-=`
- Asignación multiplicativa: `*=`.
- Asignación por división: `/=`.
- Asignación por division entera: `//=`.
- Asignación por residuo: `%=`.
- Asignación exponencial: `**=`.

```py
# Operadores de asignación

numero = 10
numero += 5     # Asignacion aditiva
numero -= 3     # Asignación sustractiva
numero *= 2     # Asignación multiplicativa
numero /= 4     # Asignación por división
```

### ***Operadores especiales:***

- Paréntesis para agrupar expresiones: `()`.
- Corchetes para acceder a elementos de listas o tuplas: `[]`.
- Llaves para diccionarios: `{}`.
- Decoradores: `@`.
- Inicio de comentarios: `#`.