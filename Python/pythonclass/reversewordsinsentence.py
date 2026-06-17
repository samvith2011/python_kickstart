# Given a string s, reverse the string without reversing the letters
# input " i like this program very much "
# output "much very program this like i"
str1 = " i like this program very much "
def reverse(str1):
    list = str1.split()
    reverselist = list[::-1]
    reversestring = ""
    for item in reverselist:
        reversestring += item +" "
    finalreversestring = reversestring.rstrip()
    print(finalreversestring)

#reverse(str1)




def reverse1(str1):
    list = str1.split()
    print(list)
    result = ""
    i = len(list)-1
    while i >=0:
        result +=list[i]+ " "
        i -= 1
    return result

str1 = "i like this program"
print(reverse1(str1))