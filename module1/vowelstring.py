'''
1. create string
2. Ues for loop mto itermate through string
3. if it matches a,e,i,o,ad u, adsd 1 to empty variable
4.Print variable


'''

word = "programming"
def vowel(word):
    vowelcount = 0
    for letter in word:
         if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
             vowelcount += 1
    print(vowelcount)


vowel(word)