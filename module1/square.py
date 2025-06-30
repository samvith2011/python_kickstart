'''
Algorithm:
1. Get square size
2. print out one row of the square
3. print out the rest of the square

'''

def squaremaker():
    squaresize = 10
    squarerow = "*" * squaresize
    for i in range(squaresize):
        print(squarerow)

squaremaker()