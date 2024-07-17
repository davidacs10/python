# Declare your age as integer variable
age = int(27)
print(type(age))

# Declare your height as a float variable
height = float(1.75)

# Declare a variable that store a complex number
complex_number = 4j

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
# b = int(input("Enter base: "))
# h = int(input("Enter height: "))
# a = 0.5 * b * h
# print("The area of the triangle: ", a)

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
# a = int(input("Enter side a: "))
# b = int(input("Enter side b: "))
# c = int(input("Enter side c: "))
# perimeter = a + b + c
# print("The perimeter of the triangle: ", perimeter)

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
# length = int(input("length: "))
# width = int(input("width: "))
# perimeter_rectangle = 2 * (length + width)
# print("The perimeter of the rectangle: ", perimeter_rectangle)

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
# pi = 3.14
# r = int(input("Enter radius: "))
# area = pi * r**2
# circumference = 2 * pi * r
# print("circle area: ", area)
# print("circumference: ", circumference)

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
slope = 2
x_intercept = 2 / 2
y_intercept = -2
print("sople: ", slope)
print("x_intercept: ", x_intercept)
print("y_intercept: ", y_intercept)

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1 = 2
x2 = 6
y1 = 2
y2 = 10
sople_between_points = (y2 - y1) / (x2 - x1)
euclidean_distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("sople between points: ", sople_between_points)
print("euclidean distance: ", euclidean_distance)

# Compare the slopes in tasks 8 and 9.
print("is sople > sople between points: ", slope > sople_between_points)
print("is sople < sople between points: ", slope < sople_between_points)
print("is sople >= sople between points: ", slope >= sople_between_points)
print("is sople <= sople between points: ", slope <= sople_between_points)
print("is sople == sople between points: ", slope == sople_between_points)
print("is sople != sople between points: ", slope != sople_between_points)

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x = -3
y = (x**2) + (6 * x) + 9
print("y =", y)

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
word_1 = "python"
word_2 = "dragon"
print(len(word_1), len(word_2))

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("on" in word_1)
print("on" in word_2)

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = "I hope this course is not full of jargon"
print("jargon" in sentence)

# There is no 'on' in both dragon and python
print("on" not in word_1)
print("on" not in word_2)

# Find the length of the text python and convert the value to float and convert it to string
print(len(word_1))
print(float(len(word_1)))
print(str(len(word_1)))

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = int(input("Enter number: "))
even_number = number % 2
print("is even number = 0?", even_number is 0)

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor_division = 7 // 3
int_value = int(2.7)
print(floor_division == int_value)

# Check if type of '10' is equal to type of 10
print(type(10) == type("10"))

# Check if int('9.8') is equal to 10
print(int(float("9.2")) == 10)
# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = int(input("hours: "))
rate_per_hour = int(input("rate_per_hour: "))
weekly_earning = hours * rate_per_hour
print("Your weekly earning: ", weekly_earning)

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
seconds_per_year = 31536000
years = int(input("Number of year you have lived:"))
print("you have lived for", seconds_per_year * years, "seconds")

# Write a Python script that displays the following table
print(1, 1, 1, 1, 1)
print(2, 1, 2, 4, 8)
print(3, 1, 3, 9, 27)
print(4, 1, 4, 16, 64)
print(5, 1, 5, 25, 125)
