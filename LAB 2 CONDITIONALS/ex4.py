# simple calculator

a = float(input("enter value of a: "))
b = float(input("enter value of b: "))

add = (a + b)
subtract = (a - b)
multiply = (a * b)
divide = (a / b)

print("operators are add, subtract, multiply and divide")

operator = str(input("enter operator: "))

if (operator == "add"):
    print(add)
elif (operator == "subtract"):
    print(subtract)
elif (operator == "multiply"):
    print(multiply)
elif (operator == "divide"):
    print(divide)
    

