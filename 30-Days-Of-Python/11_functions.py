# Functions

"""
Una funcion es un bloque de codigo que solo es ejecutada cuando es llamada.

Se puede ingresar datos en una funcion, conocidos como parametros, dentro de una funcion.

Una funcion puede retornar datos como un resultado
"""

# Creando una funcion
"""
En Python una funcion es definida utilizando la palabra clave def

Por ejemplo:
"""


def my_function_1():
    print("Hello from a function")


# Llamando a una funcion
"""
Para llamar a una funcion, se usa el nombre de la funcion seguido de los parentesis

Por ejemplo:
"""


def my_function_2():
    print("Hello from a function")


my_function_2()

# Argumentos
"""
Es la informacion que puede ser pasada a la funcion como argumentos. 

Los argumentos son especificados despues de la definicion de la funcion, dentro de los parentesis. Podemos añadir todos los argumentos que querramos solo necesitamos separarlos con una coma.

En el siguiente ejemplo tenemos una funcion con un argumento (fname). Cuando la funcion es llamada, pasaremos un primer nombre y luego ese primer nombre se usara dentro de la funcion para imprimir el nombre completo.

Por ejemplo:
"""


def my_function_3(fname):
    print(fname + " Refsnes")


my_function_3("David")
my_function_3("Jose")
my_function_3("Juan")

"""
Nota: Los argumentos son abreviados como args en las documentaciones de Python.
"""

# Parametros o Argumentos
"""
Los terminos parametros y argumentos son usados para la misma cosa: pasarle informacion a una funcion.

Desde la perspectiva de una funcion:

Los parametros son las variables listadas dentro de los parentesis de una funcion.

Los argumentos es el valor que es enviado a una funcion cuando es llamada.
"""

# Numeros de argumentos
"""
Por defecto una funcion puede ser llamada por el numero correcto de argumentos. Esto significa que si la funcion espera 2 argumentos, tienes que llamar la funcion con 2 argumentos, ni mas, ni menos.

Por ejemplo:
La funcion espera 2 argumentos y recibe 2 argumentos.
"""


def my_function_4(fname, lname):
    print(fname + " " + lname)


my_function_4("David", "Refsnes")
"""
Si tratas de llamar a la funcion con 1 o 3 argumentos arrojara error.
"""

# Argumentos arbitrarios, *args
"""
Si no sabes cuantos argumentos puedan ser pasado en tu funcion, agrega un * antes del nombre del parametro en la definicion de tu funcion.

De esta manera tu funcion recibira una tupla de argumentos, y podra acceder a ellos acordemente.

Por ejemplo:
Si el numero de argumentos es desconocido, se agrega un * antes del nombre del parametro.
"""


def my_function_5(*kids):
    print("The youngest child is " + kids[2])


my_function_5("David", "Jose", "Juan")
"""
Los argumentos arbitrarios son abreviados como *args en las documentaciones de python
"""

# Argumentos clave valor
"""
Tambien podemos enviar argumentos con la sintaxis de clave = valor.

De esta forma el orden de los argumentos no importan.

Por ejemplo:
"""


def my_function_6(child_3, child_2, child_1):
    print("The youngest child is " + child_3)


my_function_6(child_1="Juan", child_3="David", child_2="Jose")
"""
La frase argumentos de clave valor a menudo son abreviados como kwargs en la documentacion de python
"""

# Argumentos clave valor arbitrarios
"""
Si no sabes cuantos argumentos clave valor seran pasados por tu funcion, agrega 2 asteriscos ** antes de el nombre del parametro en la definicion de la funcion.

De esta manera la funcion puede recibir diccionarios como argumentos, y tener acceso a sus objetos.

Por ejemplo:
Si el numero de argumentos clave valor es desconocido, agrega ** antes del nombre del parametro
"""


def my_function_7(**kid):
    print("His last name is " + kid["lname"])


my_function_7(fname="David", lname="Refsnes")
"""
Los argumentos clave valor arbitrarios son abreviados como **kwargs en la documentacion de python
"""
# Valores de argumentos predeterminados
"""
El siguiente ejemplo demuestra como usar un valor de argumento predeterminado.

Si llamamos a la funcion sin ningun argumento, la funcion usara el valor predeterminado de ese argumento.

Por ejemplo:
"""


def my_function_8(country="Venezuela"):
    print("I am from " + country)


my_function_8(country="England")
my_function_8(country="Spain")
my_function_8()
my_function_8(country="Germany")

# Pasando una lista como argumento
"""
Podemos enviar cualquier tipo de dato como argumento (cadena de texto, numeros, listas, diccionarios). Y sera tratado como el mismo tipo de dato dentro de la funcion.

Por ejemplo:
Si enviamos una lista como argumento, seguira siendo una lista dentro de la funcion.
"""


def my_function_9(food):
    for x in food:
        print(x)


fruits = ["apple", "cherry", "kiwi"]
my_function_9(fruits)


# Retornar valores
"""
Para permitir que una funcion retorne valores, usemos la declaracion: return.

Por ejemplo:
"""


def my_function_10(x):
    return 5 * x


print(my_function_10(3))
print(my_function_10(4))
print(my_function_10(5))

# Declaracion pass
"""
Las funciones no pueden estar vacias, pero si por alguna razon deseas crear una funcion sin contenido, usemos la declaracion pass dentro de la funcion para evitar tener errores.

Por ejemplo:
"""


def my_function_11():
    pass


# Argumentos de solo posicion
"""
Podemos especificar que una funcion tenga solamente argumentos posicionales, o solo una palabra clave como argumento.

Para especificar que una funcion pueda tener un argumento posicional agregamos , / despues de los argumentos.

Por ejemplo:
"""


def my_function_12(x, /):
    print(x)


my_function_12(3)

"""
Sin , / realmente permitiras que la funcion use palabras clave, incluso si la funcion espera argumentos posicionales.

Por ejemplo:
"""


def my_function_13(x):
    print(x)


my_function_13(x=3)
"""
Pero cuando agregamos , / obtendremos un error si tratas de enviar una palabra clave

def my_function(x, /):
  print(x)

my_function(x = 3)
"""

# Argumentos posicionales de solo palabras clave
"""
A diferencia de los argumentos de solo posicion, los argumentos posicionales de solo palabras clave especifica que la funcion solo puede recibir argumentos posicionales palabras clave agregando *, antes de los argumentos.

Por ejemplo:
"""


def my_funcition_14(*, x):
    print(x)


my_funcition_14(x=5)

"""
Sin el *, permitiras que la funcion pueda recibir argumentos posicionales incluso si la funcion espera argumentos palabras clave.
"""


def my_function_15(x):
    print(x)


my_function_15(5)

"""
Pero cuando agregamos un *, y tratamos de enviar un argumento posicional, obtendremos un error.

def my_function(*, x):
  print(x)

my_function(5)
"""

# Combinacion de argumentos solo posicionales y argumentos posicionales de solo palabras claves
"""
Podemos combinar los dos tipos de argumentos posicionales en la misma funcion

Cualquier argumento antes de , /  seran solo posicionales, cualquier argumento despues de * , seran posicionales de solo palabras claves
"""


def my_function_16(a, b, /, *, c, d):
    print(a + b + c + d)


my_function_16(1, 2, c=3, d=4)

# Recursion
"""
Python tambien permite las funciones recursivas, esto significa que una funcion puede llamarse a si misma.

La recursion es un concepto comun en matematicas y programacion, el cual significa que una funcion puede llamarse a si misma, esto tiene la ventaja de que puede recorrer los datos en bucle hasta llegar a un resultado.

Los desarrolladores deben ser muy cuidadosos con la recursion ya que puede ser bastante facil entrar en una funcion que nunca termina, o una funcion que usa un exceso de memoria y de potencia de procesamiento. Sin embargo cuando se escribe correctamente, la recursion puede tener un efoque muy eficiente y matematicamente elegante en la programacion.

En este ejemplo tri_recursion() es una funcion que se llamara a si misma, usaremos la variable k como el tipo de dato que va a decrementar en -1 cada vez que se aplique la recursion. La recursion terminara cuando el resultado no sea mayor a 0 (Cuando el valor sea igual a 0).

Para los nuevos desarrolladores puede tomar algo de tiempo practicando para entender como funciona exactamente, la mejor manera de hacerlo es probandolo y modificandolo.
"""


def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\n Ejemplo del resultado de recursividad:")
tri_recursion(6)
