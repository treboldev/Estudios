edad = 34
altura = 170.5
complejo = (1+4j)

base = float(input('Ingrese la base del triángulo: '))
altura = float(input('Ingrese la altura del triángulo: '))
area = (base * altura) / 2
print(f'El área del triangulo es: {area:2f}')

lado_a = float(input('Ingrese el lado a del triángulo: '))
lado_b = float(input('Ingrese el lado b del triángulo: '))
lado_c = float(input('Ingrese el lado c del triángulo: '))

perimetro = lado_a + lado_b + lado_c
print(f'El perímetro del triángulo es: {perimetro:.2f}')

largo = float(input('Ingrese el largo del rectángulo: '))
ancho = float(input('Ingrese el ancho del rectángulo: '))
area = largo * ancho
perimetro = 2 * (largo + ancho)
print(f'El área del rectanguloes: {area:.2f}')
print(f'El perímetro del rectangulo es: {perimetro:.2f}')

esta_presente_en_python = 'on' in 'python'
esta_presente_en_dragon = 'on' in 'dragon'

print(f"'on' está presente en 'python': {esta_presente_en_python}")
print(f"'on' está presente en 'dragon': {esta_presente_en_dragon}")