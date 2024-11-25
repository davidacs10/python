# Exercises: Level 1
# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(num1, num2):
    return num1 + num2


print(add_two_numbers(2, 3))


# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    pi = 3.14
    return pi * r**2


print(area_of_circle(4))


# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
    if not all(isinstance(num, (int, float)) for num in nums):
        return "All arguments must be numbers."
    return sum(nums)


print(add_all_nums(1, 2, 3, 4, 5))


# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to_fahrenheit.
def convert_celsius_to_fahrenheit(c):
    f = (c * 9 / 5) + 32
    return f


print(convert_celsius_to_fahrenheit(41))


# Write a function called check_season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(arg):
    autumn = ["September", "October", "November"]
    winter = ["December", "January", "February"]
    spring = ["March", "April", "May"]
    summer = ["June", "July", "August"]

    if arg.capitalize() in autumn:
        return "Autumn"
    elif arg.capitalize() in winter:
        return "Winter"
    elif arg.capitalize() in spring:
        return "Spring"
    elif arg.capitalize() in summer:
        return "Summer"
    else:
        return "Please enter valid month"


print(check_season("August"))


# Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, x2, y1, y2):
    return (y2 - y1) / (x2 - x1)


print(calculate_slope(2, 6, 2, 10))


# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a, b, c):
    if a == 0:
        return "Error: a can't be equal to zero"

    discriminant = b**2 - 4 * a * c

    if discriminant > 0:
        x1 = (-b + discriminant**0.5) / (2 * a)
        x2 = (-b - discriminant**0.5) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2 * a)
        return x
    else:
        return "No real solutions"


print(solve_quadratic_eqn(2, 3, -2))


# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lst):
    for i in lst:
        print(i)


numbers = [1, 2, 3, 4, 5]
print_list(numbers)


# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
# print(reverse_list([1, 2, 3, 4, 5]))
# # [5, 4, 3, 2, 1]
# print(reverse_list1(["A", "B", "C"]))
# # ["C", "B", "A"]


def reverse_list(param):
    reverse_items = []
    for i in range(len(param) - 1, -1, -1):
        reverse_items.append(param[i])
    return reverse_items


numbers = [1, 2, 3, 4, 5]
print(reverse_list(numbers))
print(reverse_list(["A", "B", "C"]))


# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(lst):
    empty_lst = []
    for i in lst:
        empty_lst.append(i.capitalize())
    return empty_lst


food_list = ["potato", "tomato", "mango", "milk"]
print(capitalize_list_items(food_list))


# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
# numbers = [2, 3, 7, 9];
# print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
def add_item(lst, param):
    lst.append(param)
    return lst


food_staff = ["Potato", "Tomato", "Mango", "Milk"]
numbers = [2, 3, 7, 9]
print(add_item(food_staff, "Meat"))
print(add_item(numbers, 20))


# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
# numbers = [2, 3, 7, 9];
# print(remove_item(numbers, 3))  # [2, 7, 9]
def remove_item(lst, param):
    lst.remove(param)
    return lst


print(remove_item(food_staff, "Mango"))
print(remove_item(numbers, 2))


# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
# print(sum_of_numbers(5))  # 15
# print(sum_all_numbers(10)) # 55
# print(sum_all_numbers(100)) # 5050
def sum_of_numbers(param):
    total = 0
    for n in range(param + 1):
        total += n
    return total


print(sum_of_numbers(100))


# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(param):
    total = 0
    for n in range(param + 1):
        if n % 2 == 1:
            total += n
    return total


print(sum_of_odds(100))


# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(param):
    total = 0
    for n in range(param + 1):
        if n % 2 == 0:
            total += n
    return total


print(sum_of_even(100))


# Exercises: Level 2
# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
#     print(evens_and_odds(100))
#     # The number of odds are 50.
#     # The number of evens are 51.
def evens_and_odds(param):
    even_numbers = []
    odds_numbers = []
    if param > 0:
        for n in range(param + 1):
            if n % 2 == 0:
                even_numbers.append(n)
            else:
                odds_numbers.append(n)
    return f"The number of odds are {len(odds_numbers)}\nThe number of evens are {len(even_numbers)}"


print(evens_and_odds(100))


# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(param):
    if param < 0:
        return "Factorial is not defined for negative numbers"
    if param == 0 or param == 1:
        return 1
    total = 1
    for n in range(2, param + 1):
        total *= n
    return total


print(factorial(10))


# Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(param):
    if len(param) >= 1:
        return "Not empty"
    else:
        return "Empty"


print(is_empty(""))
print(is_empty("Hello World"))


# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(data):
    sum_numbers = 0
    for n in data:
        sum_numbers += n
    mean = sum_numbers / len(data)
    return mean


print(calculate_mean([1, 2, 3, 4, 4]))


def calculate_median(data):
    median = data // len(data)
    return median


print(calculate_median([1, 3, 5]))
# Exercises: Level 3
# Write a function called is_prime, which checks if a number is prime.
# Write a functions which checks if all items are unique in the list.
# Write a function which checks if all the items of the list are of the same data type.
# Write a function which check if provided variable is a valid python variable
# Go to the data folder and access the countries-data.py file.
# Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
# 🎉 CONGRATULATIONS ! 🎉
