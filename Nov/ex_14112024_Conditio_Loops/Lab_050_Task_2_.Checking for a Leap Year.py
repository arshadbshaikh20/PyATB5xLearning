# Leap day occurs in each year that is a multiple of 4, except for years evenly divisible by 100 but not by 400.
year = int(input("Enter the year\n"))
if year % 4 == 0 and year % 100 != 0 or year % 400 ==0:
    print("It is a Leap year")
else:
    print("It is not a Leap Year")
