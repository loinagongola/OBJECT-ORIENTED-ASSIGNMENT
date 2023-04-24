# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    return x / y

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (add /subtract /multiply /divide): ").lower()

if operator == 'add':
    result = add(num1, num2)
elif operator == 'subtract':
    result = subtract(num1, num2)
elif operator == 'multiply':
    result = multiply(num1, num2)
elif operator == 'divide':
    result = divide(num1, num2)
else:
    print("Invalid operator")

print(f"Answer equal {result}")
