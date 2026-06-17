'''
1. Create a list of nunbers
2. create a variable to store results and sums
igtetate over the list
4. keep adding results to the variables


'''

numlist = [1,2,3,4,5]
def addlist(numlist):
    numsum = 0
    for num in numlist:
        numsum = numsum + num
    print(numsum)

addlist(numlist)