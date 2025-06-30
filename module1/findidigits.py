'''problem statement: Find all digits ij the given word. If it doers nlt hjave digits, print, word does not have digits'''
def digitfinder():
    numberword = "Hello World"

    founddigits = ""
    for char in numberword:
        if char.isdigit():
            founddigits += char
    if len(founddigits)==0:
        print("there is not digit in word")
    print(founddigits)




digitfinder()