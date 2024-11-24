# geometry.py
import math

def sphereArea(r):
    return 4 * math.pi * r**2

def sphereVolume(r):
    return 4 * math.pi * r**3 / 3

def sphereMetrics(r):
    return sphereArea(r), sphereVolume(r)

def circleArea(r):
    return math.pi * r**2

def squareArea(x):
    return x**2

# prac8a.py
import geometry

def pointyShapeVolume(x, h, squareBase):
    if squareBase:
        base = geometry.squareArea(x)
    else:
        base = geometry.circleArea(x)
    return h * base / 3.0

# Show the available functions in the geometry module
print(dir(geometry))

# Test the pointyShapeVolume function
print(pointyShapeVolume(4, 2.6, True))    # Volume of square pyramid
print(pointyShapeVolume(4, 2.6, False))   # Volume of circular cone
,
#B Write a program to implement exception handling.
try:
    num=int(input("Enter the number:"))
    re=100/num
except(ValueError,ZeroDivisionError):
    print("Something is Wrong")
else:
    print("Result is:",re)

