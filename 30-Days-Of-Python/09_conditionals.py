# Python conditions

"""
Python soporta los operadores logicos usuales de las matematicas
    # Igualdad: a == b
    # Desigual: a != b
    # Menor que: a < b
    # Menor o igual que: a <= b
    # Mayor que: a > b
    # Mayor o igual que: a >= b

Estas operaciones se pueden usar de muchas maneras, son mas comunes en las declaraciones if y bucles

Podemos usar la declaracion if con la funcion reservada if
"""
a = 33
b = 200
if b > a:
    print("b es mayor que a")

"""
En este ejemplo usamos las variables a y b, las cuales son utilizadas en la declaracion if para probar si b es mayor que a. Como a es 33, y b es 200. Sabemos que 200 es mayor que 33, entonces esta declaracion imprimira "b es mayor que a".
"""

# Indentacion
"""
Python se basa en sangria (Espacio en blanco al inicio de la linea). Para definir un bloque de codigo. En otros lenguajes se usan las llaves "{}" para definir estos bloques de codigo.

Por ejemplo:
Una declaracion if sin sangria dara error.
a = 33
b = 200
if b > a:
print("b is greater than a") # obtendras un error
"""

# elif
"""
La palabra clave elif es una manera de declarar en python si la primera condicion no es verdadera, entonces prueba con esta condicion.
"""
a = 33
b = 33
if b > a:
    print("b es mayor que a")
elif a == b:
    print("a es igual que b")
"""
En este ejemplo a y b son iguales, es decir la primera condicion no es verdadera, entonces el programa ejecutara la segunda condicion que si lo es.
"""

# else
"""
La palabra clave else detecta cualquier cosa que no es considerado por las condiciones previas.
"""
a = 200
b = 33
if b > a:
    print("b es mayor que a")
elif a == b:
    print("a es igual a b")
else:
    print("a es mayor que b")
"""
En este ejemplo a es mayor que b. Entonces la primera condicion no es verdadera, tampoco la segunda condicion es verdadera. Entonces el programa ejecuta el condicional else que imprimira "a es mayor que b".

Tambien puedes crear una condicional sin elif:
"""
a = 200
b = 33
if b > a:
    print("b es mayor que a")
else:
    print("b no es mayor que a")

# Abreviatura if
"""
Si tienes solo una condicion if que ejecutar puedes hacerlo en una misma linea.
"""
# if a > b: print("a es mayor que b")

# Abreviatura if else
a = 2
b = 200
print("A") if a > b else print("B")

"""
Tambien podemos tener varias declaraciones else en una misma linea.
"""
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# And
"""
and es un operador logico. and es usado para combinar declaraciones condicionales y verificar si ambas se cumplen.

Por ejemplo:
Probaremos si a es mayor que b, y si c es mayor que a
"""
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Ambos son correctos")

# Or
"""
Or es un operador logico. or es usado para combinar las declaraciones condicionales y verificar si al menos una de ellas se cumple.

Por ejemplo:
Probaremos si a es mayor que b o si a es mayor que c. Una de estas 2 condiciones debe cumplirse.
"""
a = 200
b = 33
c = 500
if a > b or a > c:
    print("Al menos una condicion se cumple")

# Not
"""
Not es un operador logico. Not es utilizado para revertir el resultado de la declaracion condicional.

Por ejemplo:
probaremos que a no es mayor que b
"""
a = 33
b = 200
if not a > b:
    print("a no es mayor que b")

# Nested if
"""
Podemos tener condicionales if dentro de una condicion if. Esto se llama condiciones if anidadas.
"""
x = 41
if x > 10:
    print("x es mayor que 10")
    if x > 20:
        print("x es mayor que 20")
    else:
        print("pero no es menor que 20")

# Declaracion pass
"""
Las declaraciones if no pueden estar vacias, pero en caso que quieras declarar un if sin contenido, puedes usar pass para evitar tener un error.
"""
a = 33
b = 200
if b > a:
    pass
