'''
Algorithm:
1. Ask user for number
2. Find numbers between 0 and one
3.Store each number in a separate variable(make sure they are integers)
4. Multiply the variables
5.Print result
6.*Make sure if someone types zero, it outputs one*


'''



def factorial():
    factorial = 1

    factorialnum = int(input("What number do you want: "))
    if factorialnum <=0:
        print("Enter positive number")
    else:
        for i in range(1, factorialnum + 1):
            factorial *= i

    return factorial

#print(factorial())

#ask, give the faction of even number only
def factorial1():
    factorial = 1
    i = 2

    factorialnum = int(input("What number do you want: "))
    if factorialnum <=0:
        print("Enter positive number")
    else:
        for i in range(2, factorialnum + 1):
            if i % 2 == 0:
                factorial *= i
    return factorial
print(factorial1())

