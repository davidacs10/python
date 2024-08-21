# Exercises: Level 1
# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
age = int(input("enter your age:"))
if age > 18:
    print("You are old enough to drive.")
else:
    print(f"You need {18 - age} more to learn to drive.")

# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.
my_age = int(input("Enter your age: "))
your_age = int(input("Enter their age: "))
if my_age > your_age:
    if my_age - your_age == 1:
        print(f"I'm 1 year older than you.")
    if my_age - your_age >= 2:
        print(f"I'm {my_age - your_age} years older than you.")
elif your_age > my_age:
    if your_age - my_age == 1:
        print(f"You are 1 year older than me.")
    if your_age - my_age >= 2:
        print(f"You are {your_age - my_age} years older than me.")
else:
    print("We have the same age")

# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")
# ### Exercises: Level 2
# Write a code which gives grade to students according to theirs scores:

# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F
student_score = float(input("Enter your score: "))
if student_score >= 90:
    print("A")
elif student_score >= 70 <= 89:
    print("B")
elif student_score >= 60 <= 69:
    print("C")
elif student_score >= 50 <= 59:
    print("D")
else:
    print("F")
# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
user_input = input("Enter a valid month: ")
autumn = ["September", "October", "November"]
winter = ["December", "January", "February"]
spring = ["March", "April", "May"]
summer = ["June", "July", "August"]
if user_input.capitalize() in autumn:
    print("Is Autumn")
elif user_input.capitalize() in winter:
    print("Is Winter")
elif user_input.capitalize() in spring:
    print("Is Spring")
elif user_input.capitalize() in summer:
    print("Is Summer")
else:
    print("Please enter a valid month")

# The following list contains some fruits:

fruits = ["banana", "orange", "mango", "lemon"]
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruit_input = input("Enter a valid fruit: ")
if fruit_input.lower() not in fruits:
    fruits.append(fruit_input.lower())
    print(fruits)
else:
    print("That fruit already exist in the list")

# Exercises: Level 3
# Here we have a person dictionary. Feel free to modify it!

person = {
    "first_name": "David",
    "last_name": "Campos",
    "age": 27,
    "country": "Venezuela",
    "is_marred": False,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}
#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if "skills" in person:
    middle_skill = len("skills") // 2
    print(person["skills"][middle_skill])
else:
    print("person dict doesn't have skills key")

#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if "skills" in person:
    if "Python" in person["skills"]:
        print(True)
    else:
        print("skills key doesn't have Python value")
else:
    print("person dict doesn't have skills key")
#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
person = {
    "first_name": "David",
    "last_name": "Campos",
    "age": 27,
    "country": "Venezuela",
    "is_marred": True,
    "skills": ["React", "Node", "MongoDB", "Rust", "Papacode"],
    "address": {"street": "Space street", "zipcode": "02210"},
}
frontend = ["JavaScript", "React"]
backend = ["Node", "Python", "MongoDB"]
fullstack = ["React", "Node", "MongoDB"]

if "skills" in person:
    if frontend == person["skills"]:
        print("He is a frontend developer")
    elif backend == person["skills"]:
        print("He is a backend developer")
    elif fullstack == person["skills"]:
        print("He is a fullstack developer")
    else:
        print("Unknown title")
#  * If the person is married and if he lives in Finland, print the information in the following format:
#     Asabeneh Yetayeh lives in Finland. He is married.
if "is_married" and "country" in person:
    if person["is_marred"] == True:
        print(
            f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married"
        )
    else:
        print(
            f"{person['first_name']} {person['last_name']} lives in {person['country']}. He's not married"
        )
