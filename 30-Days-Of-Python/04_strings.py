# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
word_1 = "Thirty"
word_2 = "Days"
word_3 = "Of"
word_4 = "Python"
space = " "
print(word_1 + space + word_2 + space + word_3 + space + word_4)

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
word_5 = "Coding"
word_6 = "For"
word_7 = "All"
print(f"{word_5} {word_6} {word_7}")

# Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# Print the variable company using print().
print(company)

# Print the length of the company string using len() method and print().
print(len(company))

# Change all the characters to uppercase letters using upper() method.
print(company.upper())

# Change all the characters to lowercase letters using lower() method.
print(company.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Cut(slice) out the first word of Coding For All string.
print(company[6:])

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index("Coding"))
print(company.find("Coding"))
print(company.rfind("Coding"))

# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("Coding", "Python"))

# Change Python for Everyone to Python for All using the replace method or other methods.
sentence = "Python for Everyone"
print(sentence.replace("for Everyone", "for All"))

# Split the string 'Coding For All' using space as the separator (split()) .
print(company.split(" "))

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
company = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(company.split(","))

# What is the character at index 0 in the string Coding For All.
print("Coding For All"[0])

# What is the last index of the string Coding For All.
print("Coding For All"[-1])

# What character is at index 10 in "Coding For All" string.
print("Coding For All"[10])

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
challenge = "Python For Everyone"
words = challenge.split()
print("".join(word[0] for word in words))

# Create an acronym or an abbreviation for the name 'Coding For All'.
challenge = "Coding For All"
words = challenge.split()
print("".join(word[0] for word in words))

# Use index to determine the position of the first occurrence of C in Coding For All.
print(challenge.index("C"))

# Use index to determine the position of the first occurrence of F in Coding For All.
print(challenge.index("F"))

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
print("Coding For All People".rindex("l"))

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.find("because"))

# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rfind("because"))

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence[31:54])

# Does ''Coding For All' start with a substring Coding?
phrase = "Coding For All"
print(phrase.startswith("Coding"))

# Does 'Coding For All' end with a substring coding?
phrase = "Coding For All"
print(phrase.endswith("Coding"))

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
phrase = "   Coding For All      "
print(phrase.strip())

# Which one of the following variables return True when we use the method isidentifier():
phrase_1 = "30DaysOfPython"
phrase_2 = "thirty_days_of_python"
print(phrase_1.isidentifier())
print(phrase_2.isidentifier())

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
result = "# ".join(libraries)
print(result)

# Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
print("I am enjoying this challenge.\nI just wonder what is next.")

# Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print("Name\tAge\tCountry\t\tCity\nDavid\t27\tVenezuela\tCaracas")

# Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius**2
print(f"The area of a circle with radius {radius} is {int(area)} meters square")

# Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
a = 8
b = 6
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b:.2f}")
print(f"{a} % {b} = {a%b}")
print(f"{a} ** {b} = {a**b}")
print(f"{a} // {b} = {a//b}")
