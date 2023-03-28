# Name: Dongjong Lee
# SBUID: 112502003

# Remove the ellipses (...) when writing your solutions.

# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear(). 

def fahrenheit2celsius(fahrenheit): 
   return (5/9 * (fahrenheit - 32))

def what_to_wear(celsius):
   if (celsius < -10):
       print("Puffy_jacket")
   if (-10 < celsius < 0):
        print("Scart")
   if 0 < celsius < 10:
       print("Sweater")
   if 10 < celsius < 20:
       print("Light jacket")
   if 20 < celsius:
       print("T-shirt")
# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  

def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):
    area = abs((x1*y2 + x2*y3 + x3*y1) - (x1*y3 + x2*y1 + x3*y2)) /2
    return area
def euclidean_distance(x1, y1, x2, y2):
    eluclidean_distance = ((((x1 - x2)**2) + ((y1 - y2)**2))**(1/2)) 
    return eluclidean_distance
# d =√[(x2 – x1)2 + (y2 – y1)2]
def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):
    triangle_primeter = ((((x2 - x1)**2) + ((y2 - y1)**2))**(1/2)) + ((((x1 - x3)**2) + ((y1 - y3)**2))**(1/2)) +(((((x3 - x2)**2) + ((y3 - y2)**2))**(1/2)))
    return triangle_primeter

# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area 

import math
def deg2rad(deg):
    return (deg * math.pi/180)

def apothem(number_sides, length_side):
   a = (length_side / (2 * math.tan(180/number_sides)))
   return a

def polygon_area(number_sides, length_side):
   A = ((number_sides * length_side * apothem(number_sides, length_side))/2)
   return A

# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.

# Exercise 1 test
fahrenheit = 40
what_to_wear(fahrenheit2celsius(fahrenheit))

# Exercise 2 test
x1, x2, x3, y1, y2, y3 = -4, -5, 3, -4, 5, -3 # declaration of the vertices of the triangle
area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )

# Exercise 3 test
number_sides = 5
length_side = 4
print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))

