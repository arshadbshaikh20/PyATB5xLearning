# Problem to find the max between ( 3,4)
# Logic Building Formula
# 1. user input -> two intergers
# 2. o/p -> int1 which ever is greater max number it will return.
# 31.4 or 41.34 - float

num1 = float(input("Enter the num1"))
num2 = float(input("Enter the num2"))

if num1 > num2:
    print("Max is num1")
else:
    print("Max is num2")

# Edge cases - num1 = num2
# String -> ABC, ten -> try and except - We will learn it in future
# -ve value -> We will learn it in future
