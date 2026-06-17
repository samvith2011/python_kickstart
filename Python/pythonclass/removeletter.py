'''
1. Create string
2. Use .remove to remove it if it matches the letter
3. print the new one





'''



def remove(str1,character):
    str2 = ""
    for letter in str1:
        if letter == character:
            str2 = str1.replace(letter,"")

    print(str2)


str1 = "programming"
character = "g"
remove(str1,character)


