# Create an empty dictionary called dog
my_dict = {}
print(type(my_dict))

# Add name, color, breed, legs, age to the dog dictionary
dog = {"name": "Lobo", "breed": "wolf", "legs": "4", "age": 3}
print(dog)

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    "first_name": "David",
    "last_name": "Campos",
    "gender": "Male",
    "age": 27,
    "Marital status": False,
    "skills": ["HTML", "Python", "SQL"],
    "country": "Venezuela",
    "city": "Caracas",
}
print(student)

# Get the length of the student dictionary
print(len(student))

# Get the value of skills and check the data type, it should be a list
print(type(student["skills"]))
print(type(student.get("skills")))

# Modify the skills values by adding one or two skills
student["skills"].append("CSS")
student["skills"].append("JavaScript")
print(student)

# Get the dictionary keys as a list
print(student.keys())

# Get the dictionary values as a list
print(student.values())

# Change the dictionary to a list of tuples using items() method
print(student.items())

# Delete one of the items in the dictionary
del student["Marital status"]
print(student)

# Delete one of the dictionaries
del dog
