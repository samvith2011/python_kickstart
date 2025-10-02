'''
1. Create a function with a parameter for the word
2. Use a for loop to see all the letters
3. Put the last letter in an empty variable
4. Return the variable
5.Print the variable


'''

def lastletter(word):
    reverse_word = word[::-1]
    last_letter = reverse_word[0]
    print(last_letter)






lastletter("hydrophobia")
