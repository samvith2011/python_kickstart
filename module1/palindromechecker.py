'''
1. Create astring
2. Make it reverse, if it is the smae, it is a palindrome, if it is not, print not
3. print it



'''
string = "madam"
def palindrome(string):
    reversestring = string[::-1]
    if reversestring == string:
        return True
    if reversestring != string:
        return False

print(palindrome(string))