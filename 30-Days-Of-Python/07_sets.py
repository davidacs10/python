# sets
it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises: Level 1

# Find the length of the set it_companies
print(len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)

# Insert multiple IT companies at once to the set it_companies
it_companies_2 = {"Samsung", "Sony", "Huawei", "OpenIA"}
it_companies.update(it_companies_2)
print(it_companies)

# Remove one of the companies from the set it_companies
x = it_companies.pop()
print(x)
print(it_companies)


# What is the difference between remove and discard
# Discard no da error si no se encuentra el item especificado, remove dara error si da error si no se encuentra el item

# Exercises: Level 2
# Join A and B
# A.update(B)
# print(A)

# Find A intersection B
my_intersection = A.intersection(B)
print(my_intersection)

# Is A subset of B
my_subset = A.issubset(B)
print(my_subset)

# Are A and B disjoint sets
disjoint_sets = A.isdisjoint(B)
print(disjoint_sets)

# Join A with B and B with A
print(A.union(B))
B.update(A)
print(B)

# What is the symmetric difference between A and B
symmetric_diferrence = A.symmetric_difference(B)
print(symmetric_diferrence)

# Delete the sets completely
del A
del B
del it_companies

# Exercises: Level 3
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
set_age = set(age)
print(len(age))
print(len(set_age))

# Explain the difference between the following data types: string, list, tuple and set
## string: Es una cadena de texto que permite valores alfanumericos. Es inmutable
## list: Es una coleccion que es ordenada y mutable. Permite elementos duplicados
## tuple: Es una coleccion que es ordenada e inmutable. Permite elementos duplicados
## set: Es una coleccion desordenada, mutable y sin indice. No permite elementos duplicados

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people"
unique_words = set(sentence.split())
print(len(unique_words))
