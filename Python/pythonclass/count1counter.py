'''
Algorithm
0. Create function called counter
1. Create variable called count and set it to 0
2. Make it add one using a variable
3. Create papameter for counter that makes it stop when it equals that number


'''

def counter():
    stop = int(input("What number do you want to stop at, choose a number greater then 1, or it wont work.\n"))
    count = 0
    for i in range(stop):
        count = count + 1
        print(count)


counter()

