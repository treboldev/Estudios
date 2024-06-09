
# RESOLUCION EJERCICIO 1

nombre = 'David'
apellido = 'Villegas'
nombre_completo = 'David Villegas'
pais = 'Chile'
ciudad = 'Santiago'
edad = 34
año = 1990
es_casado = False

print(nombre, apellido, nombre_completo, pais, ciudad, edad, año, es_casado)
print('Su nombre es ', nombre, 'su apellido es ', apellido, 'Su nombre completo es ', nombre_completo, 'el vive en el pais de ', pais, 'en la ciudad de ', ciudad, 'Tiene una edad de ', edad,'años.' 'y nacio en el año ', año,)

# RESOLUCION EJERCICIO 2

print(type(nombre))
print(type(apellido))
print(type(nombre_completo))
print(type(pais))
print(type(ciudad))
print(type(edad))
print(type(año))
print(type(es_casado))

longitud_nombre = len(nombre_completo)
print(longitud_nombre)

longitud_name = len(nombre)
print(longitud_name)

num_one = 10
num_two = 8

suma = num_one + num_two
resta = num_two - num_one
multiplicar = num_two * num_one
division = num_two // num_one

nombre_usr = input('Ingrese su nombre: ')
apellido_usr = input('Ingrese su apellido: ')
pais_usr = input('Ingrese su país de origen: ')
edad_usr = input('Ingrese su edad: ')
print(f'Hola {nombre_usr} {apellido_usr}, bienvenido seas desde {pais}. ¡Por lo que vemos tienes {edad_usr} años!.')
