# Exercises: Level 1
# Declare an empty list
my_list = []

# Declare a list with more than 5 items
my_list = ["mango", "banana", "orange", "cherry", "lemon"]

# Find the length of your list
print(len(my_list))

# Get the first item, the middle item and the last item of the list
print(my_list[0])
print(my_list[int(len(my_list) / 2)])
print(my_list[-1])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["David", 27, 1.75, False, "472 Street"]

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Print the list using print()
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company
print(it_companies[0])
print(it_companies[len(it_companies) // 2])
print(it_companies[-1])

# Print the list after modifying one of the companies
it_companies[4] = "Samsung"
print(it_companies)

# Add an IT company to it_companies
it_companies.append("Sony")
print(it_companies)

# Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies) // 2, "Huawei")
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()
print(it_companies)

# Join the it_companies with a string '#;  '
it_companies = "#;  ".join(it_companies)
print(it_companies)

# Check if a certain company exists in the it_companies list.
exist = "Microsoft" in it_companies
print(exist)

# Sort the list using sort() method
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list
print(it_companies[:3])

# Slice out the last 3 companies from the list
print(it_companies[-3:])

# Slice out the middle IT company or companies from the list
mid_index = len(it_companies) // 2
print(it_companies[mid_index])

# Remove the first IT company from the list
it_companies.remove("Oracle")
print(it_companies)

# Remove the middle IT company or companies from the list
del it_companies[mid_index - 1 : mid_index + 1]
print(it_companies)

# Remove the last IT company from the list
it_companies.pop(-1)
print(it_companies)

# Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# Destroy the IT companies list
del it_companies

# Join the following lists:

# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']
front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", "Express", "MongoDB"]
front_end.extend(back_end)
print(front_end)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = front_end.copy()
full_stack.append("Python")
full_stack.append("SQL")
print(full_stack)

# Exercises: Level 2
# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
ages.sort()
min_age = min(ages)
max_age = max(ages)
print(ages)
print(f"min age is {min_age} and max age is {max_age}")

# Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
print(ages)

# Find the median age (one middle item or two middle items divided by two)
ages.sort()
length = len(ages)
middle = length // 2
median_age = (ages[middle - 1] + ages[middle]) / 2
print(median_age)
# Find the average age (sum of all items divided by their number )
average_age = sum(ages) / length
print(average_age)

# Find the range of the ages (max minus min)
range_age = max_age - min_age
print(range_age)

# Compare the value of (min - average) and (max - average), use abs() method
min_average = abs(min_age - average_age)
max_average = abs(max_age - average_age)
print(min_average)
print(max_average)

# Find the middle country(ies) in the countries list
from data import countries

countries = countries.countries

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
countries_len = len(countries)
middle_countries_list = countries_len // 2
first_half = countries[: middle_countries_list + 1]
second_half = countries[middle_countries_list + 1 :]
print(first_half)
print(len(first_half))
print(second_half)
print(len(second_half))

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
country = ["China", "Russia", "USA", "Finland", "Sweden", "Norway", "Denmark"]
ch, rs, usa, *scandic_countries = country
print(ch)
print(rs)
print(usa)
print(scandic_countries)
