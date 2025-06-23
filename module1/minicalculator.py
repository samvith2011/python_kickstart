#Problem statement, create a calculator that can do the four basic functions of math
'''
1.Take two inputs from user
2. Ask user of type of operation
3. Compute and make a decision based on users choice
4. Return the result




'''

def calculator():
    num1 = int(input("Enter first number\n"))
    num2 = int(input("Enter second number\n"))
    operation = input("pick one: multi,div,add,sub")
    if operation == "multi":
        return num1 * num2
    elif operation == "div":
        return num1 / num2
    elif operation == "add":
        return num1 + num2
    elif operation == "sub":
        return num1 - num2


print(calculator())