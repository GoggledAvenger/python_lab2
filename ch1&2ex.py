#Chapter 1 Exercises


#Exercise top of pg 12
x1 = round(42.5)
print(x1)
x2 = round(43.5)
print(x2)

#Exercises 1-3 pg 12
#1.
x3 = 2++2
print(x3)
#2.
# "4 2" gives error "SyntaxError: invalid syntax" on the second number
#3.
# round(42.5 lets you know "SyntaxError: '(' was never closed"

#Exercise bottom of pg 12
print(type(765))
print(type(2.718))
print(type('2 pi'))
print(type(abs(-7)))
print(type(abs(-7.0)))
print(type(abs))
print(type(int))
print(type(type))

#Exercises pg 13
#1. How many seconds are there in 42 minutes 42 seconds?
secinmin = 42 * 60
howmany = secinmin + 42
print(howmany)

#2. How many miles are there in 10 kilometers?
kminmile = 1.61
mlsin10km = 10 * kminmile
print(mlsin10km)

#3 Average seconds per mile in a 10k at 42 min 42 secs.
secpermile = howmany / mlsin10km
print(secpermile)

#4. average page in minute and seconds per mile
minpermile = secpermile / 60
print(minpermile)

#5. average speed in mph
mph = (mlsin10km / (howmany / 3600))
print(mph)


#Chapter 2 Exercises

#Exercises pg 24-25
#1.
# 17 = n gives an error: "SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?"
#2.
x = y = 1
#3.
# "print(x, y);" it doesn't like the semicolon but it seems to ignore it
#4.
# x = 4 + 5 . adding a period to the end of a statement gives the error: "SyntaxError: invalid syntax"
#5.
# you must spell the module's name correctly or it won't load:
# trying maath results in "ModuleNotFoundError: No module named 'maath'"

#Exercises pg 25
from math import pi, cos, sin, e, pow, exp
#Part 1
radius = 5
volume = ((4 / 3) * pi * radius**3)
print('volume =' , volume)
# radius in centimeters, volume in cubic centimeters

#Part 2
x = 42
c = (cos(x))**2
s = (sin(x))**2
print(c + s)

#Part 3
#three ways to square e

w1 = e**2
w2 = pow(e, 2)
w3 = exp(2)
print('natural logarithm', w1, w2, w3)