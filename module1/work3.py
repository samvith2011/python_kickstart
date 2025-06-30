'''
Algorithm:
#1. Give dimensions of cube
#2. Square the dimensions
#3. Cube the dimensions
#4. Print the dimenions

'''

def squareandcube():
    userlength = int(input("How long do you want your square?"))
    squarenumber = userlength * userlength
    cubenumber = userlength * userlength * userlength

    print(squarenumber)
    print(cubenumber)


squareandcube()
