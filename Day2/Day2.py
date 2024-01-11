# Day 2: Basic Calculator

# Function to add two numbers
def add (x,y):
    return x + y
# Function to subtract two numbers
def subtract(x,y):
    return x - y

# Function to multiply two numbers
def multiply(x,y):
    return x * y

# Function to divide two numbers
def divide(x,y):
    if x!=0:
        return x /y
    else:
         return "INVALID OPERATION"

# Take user input for numbers and operation
num1 = float(input("Enter a Number:"))
num2 = float(input("Enter a Number:"))
operation = input("Choose an option(+,-,*,/:)")

# Perform the operation and display the result
if operation == "+" :
    result = add(num1, num2)
elif operation == "-" :
    result = subtract(num1, num2)
elif operation == "*" :
    result = multiply(num1, num2)
elif operation == "/" :
    result = divide(num1, num2)
else :
    result = ("Invalid Operation")

print(f"Result:{result}")