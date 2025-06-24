'''Algorithm:
#1. Seperate the word into letters
#2. Check which letters are a,e,i,o, and u,
#3. Count how many letters were a, e, i, o, and u
#4. Print the # of letters that were a, e, i, o, and u'''
def getvowel():
    word = input("Enter a word \n").lower()
    vowels = ""
    for char in word:
        if char == "a" or char == "e" or char == "i" or char =="o" or char == "u":
            vowels += char
    return vowels



print(getvowel())