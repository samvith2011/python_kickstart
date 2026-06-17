'''
algorithm:
1. Create the function
2. Create the parameters(num1,num2,operation)
3. Use the parameters to make the calculator do calculations by combining them




'''
''''#num1 and num2 are int and operation is string and use str like "add"/"sub"/multi/div
def simplecalculator(num1,num2,operation):
    if operation=="add":
        addition(num1,num2)
    elif operation == "sub":
        subtraction(num1,num2)
    elif operation == "multi":
        multiplication(num1,num2)
    elif operation == "div":
        division(num1,num2)


# Running function
print(simplecalculator(1,2,"add"))'''


def simplecalutorV2(num1, num2, operation):
    if operation == "add":
        return addition(num1, num2)
    if operation == "sub":
        return subtraction(num1, num2)
    if operation == "multi":
        return multiplication(num1, num2)
    if operation == "div":
        return division(num1, num2)


def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 + num2

def division(num1, num2):
    return num1 + num2


print(simplecalutorV2(1,2,"add"))