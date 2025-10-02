#write a program to find the first occurence of the substrng in a string
'''
input :
str1= "Python is amazing"
substr1 = "is"

output = 7
'''


'''def findoccurence(str1, substr1):
    #get the length of str1 and substr1
    str1_len = len(str1)
    substr1_len = len(substr1)
    #iterate over the str1
    for i in range(str1_len+1):
        #slice the string from index where substr1 starts and go till length of substr1
        if str1[i:i+substr1_len] == substr1:
            return i

str1 = "Python is amazing"
substring = "is"

print(findoccurence(str1,substring ))'''

#find substring in string, return true if it exists, else, false
'''
1. Create two parameters, str1, which is the string, and substr1, which is the substring
2. Create a function called findsubsstring to store the code
3. create a for loop to iterae through the entire string, using string length as loop length
4. Create an if stamtemnt, if the index of str1 equals the substrings first letter and the index + 1 of str1 = substrings second letter,print true, else, print false

'''

def findsubstring(str1,substr1):
    for i in range(len(str1)):
        if str1[i] == substr1[0] and str1[i+1] == substr1[1]:
            return True
    else:
        return False

str1 = "Python is amazing"
substr1 = "amazing"
print(findsubstring(str1,substr1))