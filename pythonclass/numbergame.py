def numbergame():
    secretnumber = int(input("What is your number going to be?: "))
    guessnumber = int(input("What is your guess: "))
    while secretnumber != guessnumber:
        if guessnumber > secretnumber:
            print("The number is lower")
            guessnumber = int(input("What is your guess: "))
        elif guessnumber < secretnumber:
            print("This number is higher")
            guessnumber = int(input("What is your guess: "))
    if guessnumber == secretnumber:
        print("That was the number, good job")
        print("Thanks for playing")



numbergame()