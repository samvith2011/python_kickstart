'''
1. Create a string with a aparameter for the letter
2. Create a for loop iterating over the loop
3. Ceck if the letter is equal to letter i choose, and if it is, add 1
4. print letter


'''
string = "hello"
character = "l"

def letterf(string,character):
    foundletters = 0
    for letter in string:
        if character == letter:
            foundletters += 1
    print("Frequency of",character,":",foundletters)

letterf(string,character)

