### Nivel 1
# 1. Declara una variable first name y asígnale un valor
first_name = "David"

# 2. Declara una variable last name y asígnale un valor
last_name = "Campos"

# 3. Declara una variable full name y asígnale un valor
full_name = "David Campos"

# 4. Declara una variable country y asígnale un valor
country = "Venezuela"

# 5. Declara una variable city y asígnale un valor
city = "Caracas"

# 6. Declara una variable age y asígnale un valor
age = 27

# 7. Declara una variable year y asígnale un valor
year = 2024

# 8. Declara una variable is_married y asígnale un valor
is_married = False

# 9. Declara una variable is_true y asígnale un valor
is_true = True

# 10. Declara una variable is_light_on y asígnale un valor
is_light_on = True

# 11. Declara multiples variables en una linea
first_name, last_name, country, city, age = (
    "David",
    "Campos",
    "Venezuela",
    "Caracas",
    27,
)

### Nivel 2
# 1. Comprueba el tipo de dato de todas tus variables usando la funcion integrada type()
print(type(first_name))
print(type(last_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

# 2. Usando la funcion integrada len(), encuentra la longitud de tu first name
print(len(first_name))

# 3. Compara la longitud de tu first name y last name
print(len(first_name) and len(last_name))

# 4. Declara 5 como num_one y 4 como num_two
num_one = 5
num_two = 4

# 	1. Suma num_one y num_two y asigna su valor a una variable total
total = num_one + num_two

# 	2. Resta num_two y num_one y asigna su valor a una variable diff
diff = num_two - num_one

# 	3. Multiply num_two y num_one y asigna su valor a una variable product
product = num_two * num_one

# 	4. Divide num_one y num_two y asigna su valor a una variable division
division = num_one / num_two

# 	5. Utilice la division de módulos para encontrar num_two dividido por num_one y asigne su valor a una variable remainder
remainder = num_two % num_one

# 	6. Calcule num_one elevado a num_two y asigne su valor a una variable exp
exp = num_one**num_two

# 	7. Encuentre la division de piso de num_one entre num_two y asigne su valor a una variable floor_division
floor_division = num_one // num_two

# 5. El radio de un circulo es 30 metros
r = 30

# 	1. Calcula el area de un circulo y asigna su valor a una variable area_of_circle
area_of_circle = 3.14 * r**2

# 	2. Calcule la circunferencia del circulo y asigne el valor a una variable circum_of_circle
circum_of_circle = 2 * 3.14 * r

# 	3. Tome el radio como una entrada de usuario y calcule el area.
r = int(input("radio: "))
area_of_circle = 3.14 * r**2

# 6. Use la funcion integrada input para obtener first name, last name, country y age de un usuario y almacena su valor en sus variables correspondientes
first_name = input("first name: ")
last_name = input("last name: ")
country = input("country: ")
city = input("city: ")
age = input("age: ")

# 7. Ejecuta help("keywords") en la terminal de python para comprobar las palabras reservadas en python o palabras clave (keywords)
help("keywords")
