# Write a program that prints numbers from 1 to 100.
# However, for multiples of 3, print "Fizz" instead of the number, and for multiples of 5, print "Buzz."
# For numbers that are multiples of both 3 and 5, print "FizzB

for i in range(1, 101):
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3==0 and 1% 5 ==0:
        print("FizzB")
    else:
        print(i)
