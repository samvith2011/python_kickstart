'''
1. Create a string wiht wo words
2. create two papramets
3. use logic to print substring


'''

string = "Python Programming"

start = 7
end = 18

def sub(string,start,end):
    return string[start:end]

print(sub(string,start,end))