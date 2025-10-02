'''
1. Create a string
2. create pprameters for string
3. Find a way to extract substring from string


'''
str1 = "Python Programming"
start = 7
end = 18
def extract(str1,start,end):
    substring = str1[start:end]
    print(substring)

extract(str1,start,end)