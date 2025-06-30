'''
Algorithm:

1. Create a list with random numbers
1a. Create an empty variable called max and min with a number
2. Use a for loop to iterate through the list
3. Use if statements to compare the numbers to the max and min
4. Return results
5. Print the results


'''

list = [1,71,45,67,346,992,13,78]

def findminandmax(list):
    #check the edge case 1: if list is empty
    if len(list) == 0:
        print("Thre is nothing")

    else: #chck if list has items
        max = list[0] #assume 0th index is the max number
        min = list[0] #assume 0th index is the min value
        for num in list: #iterate over the list
            if num > max: #comare current element with max
                max = num #update max with current

            if num < min: #compare cureent elemnent with min
                min = num #update min

    print(f"max {max} and min {min}")
    if max == min: #if number are duplicated
        print("All numbers are the same")

list = []
findminandmax(list)
