# Write a program to join a ist of words into a single string with spaces
'''
1. Create a  list of words
2. Create vaeriables for each word by linking the variable to each item in the list
3. Printa string with all the variables




'''

def joinlist(list):
    final = ""
    for item in list:
        final += item + " "
    print(final)


list = ["Python","Is","Fun", "fun2","|"]
joinlist(list)
