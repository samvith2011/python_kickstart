'''
1. Create string with word
2. use largeansmall2 code to fidn out whcih is largrst
3. Print it outi



'''
sentence = "Python is amazing"
def large(sentence):
    word = sentence.split()
    max = word[0]
    for item in word:
        if item > max:
            max = item
        if item < max:
            continue
    print(max)


large(sentence)