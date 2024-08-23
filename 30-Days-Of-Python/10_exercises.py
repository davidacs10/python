# Exercises: Level 1
# Iterate 0 to 10 using for loop, do the same using while loop.
## while loop
n = 0
while n <= 10:
    print(n)
    n += 1

## for loop
for x in range(11):
    print(x)

# Iterate 10 to 0 using for loop, do the same using while loop.
## while loop
n = 10
while n >= 0:
    print(n)
    n -= 1

## for loop
for x in range(10, -1, -1):
    print(x)

# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
string = "# "
for x in range(1, 8):
    print(string * x)

# Use nested loops to create the following:
for x in range(1, 8):
    for y in range(1, 8):
        print("#", end=" ")
    print()
# Print the following pattern:

# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100

for x in range(11):
    print(f"{x} x {x} = {x * x}")

# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
technologies = ["Python", "Numpy", "Pandas", "Django", "Flask"]
for x in technologies:
    print(x)

# Use for loop to iterate from 0 to 100 and print only even numbers
for x in range(101):
    if x % 2 == 0:
        print(x)

# Use for loop to iterate from 0 to 100 and print only odd numbers
for x in range(101):
    if x % 2 == 1:
        print(x)

# Exercises: Level 2
# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# The sum of all numbers is 5050.
sum_all_numbers = 0
for x in range(101):
    sum_all_numbers += x
print(sum_all_numbers)

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
# The sum of all evens is 2550. And the sum of all odds is 2500.
sum_all_evens = 0
sum_all_odds = 0
for x in range(101):
    if x % 2 == 0:
        sum_all_evens += x
    else:
        sum_all_odds += x
print(
    f"The sum of all evens is {sum_all_evens}. And the sum of all odds is {sum_all_odds}"
)

# Exercises: Level 3
# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
from data import countries

country = countries.countries

countries_with_land = []
for x in country:
    if x.endswith("land"):
        countries_with_land.append(x)
print(countries_with_land)

# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ["banana", "orange", "mango", "lemon"]
reverse_fruits = []
for fruit in range(len(fruits) - 1, -1, -1):
    reverse_fruits.append(fruits[fruit])

print(reverse_fruits)

# Go to the data folder and use the countries_data.py file.
from data import countries_data

data = countries_data.countries_data

# What are the total number of languages in the data
total_number_languages = set()
for x in data:
    for languages in x["languages"]:
        total_number_languages.add(languages)
print(f"Total number of languages in the data: {len(total_number_languages)}")

# Find the ten most spoken languages from the data
from collections import Counter

total_languages = []
for x in data:
    for y in x["languages"]:
        total_languages.extend(x["languages"])
most_spoken_languages = Counter(total_languages).most_common(10)
print("The most spoken langugages:")
for k, v in most_spoken_languages:
    print(f"{k}: {v}")

# Find the 10 most populated countries in the world
populated_countries = []
for x in data:
    populated_countries.append((x["name"], x["population"]))
most_populated_countries = Counter(dict(populated_countries))
ten_most_populated_countries = most_populated_countries.most_common(10)
print("Most populated countries in the world:")
for k, v in ten_most_populated_countries:
    print(f"{k}:{v}")
