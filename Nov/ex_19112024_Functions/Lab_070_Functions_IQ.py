# Create a program to sum of three number from the user input,
# if user doesn't enter any number', use default as 100, 200, 300
from Nov.ex_19112024_Functions.Lab_069_Types_of_Functions import result

num1 = int(input("Enter the num1\n"))
num2 = int(input("Enter the num2\n"))
num3 = int(input("Enter the num3\n"))

def sum_3_numbers(n1 = 100, n2 = 200, n3 = 200):
    return n1 +n2 + n3
resul = sum_3_numbers(num1, num2, num3)
print(resul)

result2 = sum_3_numbers()
print(result2)
result2 = sum_3_numbers(10)
print(result2)
result2 = sum_3_numbers(10, 20,)
print(result2)
result2 = sum_3_numbers(10, 20, 30)
print(result2)
