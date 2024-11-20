# User Defined
# 1. They can't return -> non-return
# 2.They can return something
# 3.They have parameters
# 4. They don't parameters / arguments
from Nov.ex_09112024_Litrals_variables.Lab018 import result


# 1. They can't return -> non-return
# No Return Type and No Parameter/Argument
def greet():
    print("Hello")
greet()


# 2. No Return Type and With Argument
def say_Hello(name):
    print("Hello", name)
say_Hello("Arshad")

# 3. No Return Type with Default Argument ( # positional argument)
def say_hello_default_arg(name="Arshad"):
    print("Hii", name)
say_hello_default_arg()
say_hello_default_arg("Shaikh")

def multiple_args(name1="A", name2="Z"):
    print("Multi-->", name1, name2)
multiple_args()
multiple_args("Lucy", "Thor")
multiple_args(name1="IronMan")
multiple_args(name2="Hulk")

# 4. Argument + Return

def sum_of_two(a, b):
    return a+b
Result = sum_of_two(58, 22)
print(Result)

def sum_of_two_default_numbers(num=100, num2=200):
    print("I will sum the 2 numbers")
    return num +num2
Result = sum_of_two_default_numbers()
print(Result)

Result =sum_of_two_default_numbers(21, 54)
print(Result)