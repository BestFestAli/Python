import math as m
import numpy as np

# 1 answer
x = float(input("Input degree: "))
print("Output radian:", m.radians(x))
print("===================")
# 2 answer
h = float(input("Height: "))
b1 = float(input("Base, first value: "))
b2 = float(input("Base, second value: "))
print("Expected Output:", h*(b1+b2)/2)
print("===================")
# 3 answer
n = int(input("Input number of sides: "))
a = float(input("Input the length of a side: "))
print("The area of the polygon is:", (n*a*a*m.sin((n-2)*m.pi/n/2)*m.sin((n-2)*m.pi/n/2)/(2*m.sin(m.pi*2/n))).__round__(1))
print("===================")
# 4 answer
b = float(input("Length of base: "))
h = float(input("Height of parallelogram: "))
print("Expected Output:", b*h)