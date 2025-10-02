'''
1.create a string
2. use ::-1 to reverse it
3. Print the reverse string


'''
string = "Python"
def stringreverse(string):
    reversestring = string[::-1]
    return reversestring
print(stringreverse(string))