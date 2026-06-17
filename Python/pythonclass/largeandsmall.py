'''
Algorithm:

1. Make a list with the 2 numbers
2. Check which one is bigger then the other
3. Print the bigger number





'''

numlist = [7,5]

def findbig(numlist):
    max = numlist[0]
    for num in numlist:
        if num > max:
            max = num

findbig(numlist)