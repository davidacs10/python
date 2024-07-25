# Exercises: Level 1
# Create an empty tuple
my_tuple = ()
my_tuple_2 = tuple()

print(type(my_tuple))
print(type(my_tuple_2))

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ("David", "Jose")
sisters = ("Ana", "Maria")

# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters

# How many siblings do you have?
print(len(siblings))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = list(siblings)
family_members.append("Arcadio")
family_members.append("Flor")
family_members = tuple(family_members)
print(family_members)

# Exercises: Level 2
# Unpack siblings and parents from family_members
parents = family_members[4:]
siblings = family_members[:4]
print(parents)
print(siblings)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("Mango", "Lemon", "Strawberry")
vegetables = ("Potato", "Onion", "Tomato")
animal = ("Egg", "Meat", "Chicken")
food_stuff_tp = fruits + vegetables + animal
print(food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_items = len(food_stuff_tp) // 2
print(food_stuff_tp[middle_items])

# Slice out the first three items and the last three items from food_staff_lt list
print(food_stuff_lt[:3])
print(food_stuff_lt[-3:])

# Delete the food_staff_tp tuple completely
del food_stuff_tp

# # Check if an item exists in tuple:
# print("Potato" in food_stuff_tp)

# Check if 'Estonia' is a nordic country

# Check if 'Iceland' is a nordic country

nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)
