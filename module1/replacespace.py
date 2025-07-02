'''
1. Create string with spaces
2. Use replace command to replace spaces with hyphen
3. Print it


'''
str1 = "Python is fun"
def replace(string):
    for char in str1:
        if char == " ":
            str2 = str1.replace(" ","-")

    print(str2)

replace(str1)