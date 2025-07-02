'''
Algorithm:
1. create a list of numbers
2. use an for loop to iterate over a list
3. Add an if statement to pt even numbers into a new list
4.Print the results



'''

list = [1,2,3,4,5,6]# the list with numbers

def evenlist(list): # defining fucntion
    evenlist = []# epty variable to store the even numbers
    for num in list: #doing the followijg for each number in the list
        if num % 2 ==0: # if the number is even
            evenlist.append(num) # adds it to the list
        elif num % 2 != 0: # if it is not even
            continue # continues the loop
    print(evenlist) # prints list


evenlist(list) # calling function