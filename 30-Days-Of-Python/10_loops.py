# Loops

"""
Python tiene dos comandos de bucles primitivos:
while loops
for loops
"""

# While loops
"""
Con el bucle while podemos ejecutar un conjunto de declaraciones siempre y cuando sea verdadero.

Por ejemplo:
Imprime i siempre y cuando i sea menor que 6.
"""
i = 0
while i < 6:
    print(i)
    i += 1
"""
Nota: recuerda aumentar el valor de i, o sino el bucle seguira por siempre.

El bucle while necesita tener listas las variables para poder ejecutarse, en este ejemplo definimos una variable de indexacion i con el valor de 0
"""

# Declaracion break
"""
Con la declaracion break podemos detener el bucle incluso si la condicion while es verdadera.

Por ejemplo:
Salimos del bucle si i es igual a 3.
"""
i = 0
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# Declaracion continue
"""
Con la declaracion continue podemos detener la iteracion actual y continuar con la siguiente

Por ejemplo:
Continua con la siguiente iteracion si i es igual a 3
"""
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# Declaracion else
"""
Con la declaracion else podemos ejecutar un bloque de codigo una vez la condicion no es verdadera.

Por ejemplo:
Imprime un mensaje una vez la condicion sea falsa
"""
i = 0
while i < 6:
    print(i)
    i += 1
else:
    print("i ya no es menor que 6")

# For loops
"""
El bucle for es usado para iterar a traves de una secuencia (es decir, una lista, tupla, set, diccionario o una cadena de texto)

Esto es lo menos parecido al bucle for en otros lenguajes de programacion, y funciona mas como un metodo de iteracion como en otros lenguajes de programacion orientada a objetos.

Con el bucle for podemos ejecutar un conjunto de declaraciones, una vez por cada item en una lista, tupla, set, etc.

Por ejemplo:
Imprime cada fruta de la lista frutas
"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
"""
El bucle for no necesita que se establezca una variable de indexacion.
"""

# Bucle a traves de una cadena.
"""
Incluso las cadenas son iterables, son una secuencia de caracteres.

Por ejemplo:
Bucle a traves de las letras de la palabra "banana"
"""
for x in "banana":
    print(x)

# Declaracion break en for
"""
Con la declaracion break podemos detener el bucle antes de que haya recorrido todos los elementos.

Por ejemplo:
Detenemos el bucle cuando x sea igual a "banana"
"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
"""
Otro ejemplo:
Detenemos el bucle cuando x sea igual a "banana" pero esta vez detenemos antes de imprimir
"""
for x in fruits:
    if x == "banana":
        break
    print(x)

# Declaracion continue en for
"""
Con la declaracion continue podemos detener la iteracion actual y continuar con la siguiente
"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# range() function
"""
Para recorrer a traves de un bloque de codigo una cantidad especifica de veces, podemos usar la funcion range(). La funcion range() retorna una secuencia de numero que por defecto empieza en 0 e incrementa en 1 y termina en el numero especificado.

Por ejemplo:
Usando la funcion range()
"""
for x in range(6):
    print(x)
"""
El ejemplo anterior no imprime los numeros del 0 al 6, pero si de el 0 al 5.

La funcion range() por defecto empieza desde 0, sin embargo es posible establecer un numero en especifico agregando un parametro: range(2,6) lo que significa que empieza desde 2 y termina en 5

Por ejemplo:
Empieza desde el parametro agregado.
"""
for x in range(2, 6):
    print(x)
"""
La funcion range() por defecto incrementa la secuencia en 1, pero podemos establecer un numero especifico de incremento agregando un tercer parametro: range(2, 30, 3)

Por ejemplo:
Incrementa la secuencia en 3(por defecto es 1).
"""
for x in range(2, 30, 3):
    print(x)

# else en bucle for
"""
La palabra clave else en un bucle for significa que ejecuta un bloque de codigo cuando el bucle haya terminado.

Por ejemplo:
Imprime un numero del 0 al 5 e imprime un mensaje cuando el bucle haya terminado.
"""
for x in range(6):
    print(x)
else:
    ("El bucle ha terminado")
"""
El bucle for no ejecutara un else si se encuentra un break dentro del bucle.

Por ejemplo:
se dentendra el bucle cuando x sea igual a 3, y veras que pasa con el bloque else
"""
for x in range(6):
    if x == 3:
        break
    print(x)
else:
    ("El bucle ha terminado")

# Bucles anidados
"""
Un bucle anidado es un bucle dentro de otro bucle

El bucle interior se ejecutara una vez por cada iteracion del bucle exterior

Por ejemplo:
Imprime cada adjetivo por cada fruta.
"""
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)

# Declaracion pass en for
"""
Los bucles for no puedes estar vacios pero si por alguna razon quieres tener un bucle for sin contenido, pon la declaracion pass para evitar tener errores

Por ejemplo:
"""
for x in [0, 1, 2]:
    pass
