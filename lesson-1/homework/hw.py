#1)Given a side of square. Find its perimeter and area.

side = float(input("Enter the length of the side of the square: "))
perimeter = 4 * side
area = side * side

print(f"Perimeter of the square: {perimeter}")
print(f"Area of the square: {area}")

#2)Given diameter of circle. Find its length.

import math

diameter = float(input("Enter the diameter of the circle: "))
circumference = math.pi * diameter
print(f"The circumference of the circle is: {circumference:.2f}")

#3)Given two numbers a and b. Find their mean.

a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))
mean = (a + b) / 2
print(f"The mean of {a} and {b} is: {mean}")

#4)Given two numbers a and b. Find their sum, product and square of each number.

a = float(input("Birinchi sonni kiriting (a): "))
b = float(input("Ikkinchi sonni kiriting (b): "))

yigindi = a + b
kopaytma = a * b
a_kvadrat = a ** 2
b_kvadrat = b ** 2

print(f"{a} + {b} = {yigindi} (Yig‘indi)")
print(f"{a} * {b} = {kopaytma} (Ko‘paytma)")
print(f"{a} ning kvadrati: {a_kvadrat}")
print(f"{b} ning kvadrati: {b_kvadrat}")
