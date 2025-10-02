'''
Algorithm:
1. Create string
1a.
2. use a for loop to iterate over string and check if the letter equals the string of a number
3. For every time it is a number, add one to numcount
4. If numcount equals length of string, say yes
5. if not, print no


'''
string = "12345"
def letterornum(string):
    numcount = 0
    for char in string:
        if char == "0" or char == "1" or char == "2" or char == "3" or char == "4" or char == "5" or char == "6" or char == "7" or char == "8" or char == "9":
            numcount += 1
    if numcount == len(string):
        print(True)
    elif numcount != len(string):
        print(False)



letterornum(string)