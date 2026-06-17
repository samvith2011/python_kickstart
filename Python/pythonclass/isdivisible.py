'''
1. Create a function with 2 variables, num1 and num2, for the two numbers
2. Use the modulus to see if num1 will divide cleanly with num2
3.If it can, print yes
4. If it cant, print no


'''

def isdivisible(num1, num2):
    if num1 % num2 == 0:
        return "Yes"
    elif num1 % num2 != 0:
        return "No"


print(isdivisible(10,3))