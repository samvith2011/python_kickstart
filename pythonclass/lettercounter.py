'''
Algorithm:
1. Create function with parameters for word and letter
2. Use for loop to go through the word and find out how many letters match that letter using if statement
3.Print results


'''
found_letters = 0

def count_letter(word, letter):

    found_letters = 0
    for char in word:
        if char == letter:
            found_letters += 1
    return found_letters

print(count_letter("banana", "b"))