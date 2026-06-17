'''
Algorithm:
1. Create a function with the parameters, word and letter
2. Create a piece of code that checks if the first letter matches the one printed, maybe using a loop
3. Return yes or no, based on output
4. Print it


'''

def startletter(word, letter):
    first_letter =word[0]
    if first_letter == letter:
        return "yes"
    elif first_letter != letter:
        return "no"



print(startletter("kitten", "k"))