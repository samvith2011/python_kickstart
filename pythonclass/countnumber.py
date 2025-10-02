'''
Algorithm:
1. Create a list of numbers with repeats
2. Create a apaameter with a number
3. Create a for loop to tierate through the list
4. Create an empty variable for the number of numbers
4. careate an if statmennt that if a number is equal to the paorameter, add 1 to an empty variable
5. Print the variable



'''

list = [1,2,2,3,4,5,3,7]# list of numbers
target = 3# what number we want to count

def numbercount(list,target): # defining founction
    numcount = 0 #starting count of number
    for num in list: # for each num in list
        if num == target: # if the number matches the number in the list
            numcount = numcount + 1 # add one to numcount
    print(numcount) # print the numcount


numbercount(list,target)