# This Mini Calculator is made using Python by Jay Parmar
# It performs 5 operations namely;
# Addition, Subtraction, Multiplication, Division and Modulo

# Taking input from the User
first = input("Enter first number: ")
operator = input("Enter operator (+,-,*,/,%): ")
second = input("Enter second number: ")

# Converting the following variables from String to Integer
first = int(first)
second = int(second)

# Code for performing operations (+,-,*,/,%) respectively
if operator == "+":
    print((first) + (second))
elif operator == "-":
    print((first) - (second))
elif operator == "*":
    print((first) * (second))
elif operator == "/":
    print((first) / (second))
elif operator == "%":
    print((first) % (second))
else:
    print("Invalid Operation")
