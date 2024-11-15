# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.


side1 = float(input("Enter the value of side1\n"))
side2 = float(input("Enter the value of side2\n"))
side3 = float(input("Enter the value of side3\n"))
if side1 == side2 and side2 == side3:
    print("It is an Equilateral Triangle.")
elif side1 == side2 or side1 ==side3 or side2 == side3:
    print("It is an Isosceles Triangle.")
else:
    print("It is an Scalene Triangle.")
