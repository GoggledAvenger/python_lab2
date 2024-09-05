#Lab 2 assignment from https://github.com/THartmanOfTheRedwoods/PyLab002

#Part 1:Variables and Assignments
name = "Christine"
age = 40
height = 5.7
favorite_color = "blue"

print(name)
print(age)
print(height)
print(favorite_color)

print(name, age, height, favorite_color)

print(f"Hello, my name is {name}. I'm {age} years old and {height}. My favorite colors is {favorite_color}.")

print(f"Hello, my name is {name}. I'm {age:d} years old and {height:f}. My favorite colors is {favorite_color}.")

print(f"""
Name: {name}
Age: {age}
Height: {height}
Favorite Color: {favorite_color}
""")

from math import pi

circle_area = (pi * (5**2))
print(f"Area of circle is {circle_area:.1f}")

#Part 2: Statements and Modules
import math
sqrtofage = math.sqrt(age)
print("Square root of age is", sqrtofage)

cosht = (math.cos(height))**2
sinht = (math.sin(height))**2
print("Cosine of my height:", cosht, "Sine of my height:", sinht)

#Part 3: Expressions and Operators
sumplus5 = age + 5
htminus4 = height - 4
agexht = age * height
htdiv2 = height / 2
agediv3 = age // 3
agesqrd = age**2

print(f'''
The sum of my age and 5 is {sumplus5}.
The difference between my height and 4 is {htminus4}.
The product of my age and my height is {agexht}.
The quotient of my height and 2 is {htdiv2}.
The remainder of my age divided by 3 is {agediv3}.
My age squared is {agesqrd}.
''')

#Part 4: Temperature Conversion

degrees = "°"
F = int(input("Enter temperature in Fahrenheit for conversion to Celsius."))
C = (F - 32) * 5 / 9
print(f"{F} {degrees} Fahrenheit is {C:.0f} {degrees} in Celsius.")

