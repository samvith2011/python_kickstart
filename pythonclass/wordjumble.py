import random

'''def get_random_words():
words = ['python','developer','fumble','learning','project','school','keyboard']
return random.choice(words)'''

def get_random_word():
    word = input("Enter a word to scramble")
    return word
def jumble_word(word):
    return ''.join(random.sample(word, len(word)))

def play_game():
    print("Welcome to the word jumble game")
    score = 0
    play = True

    while play:
        original_word = get_random_word()
        jumbled = jumble_word(original_word)

        print(f"\nJumbled Word: {jumbled}")
        guess = input("Your Guess").lower()

        if guess == original_word:
            print("Correct! Well Done!")
            score += 1
        else:
            print(f"Wrong!  The correct word was {original_word}")
            if score > 0:
                score -= 1

        again = input("Do you want to play again? (yes/no): ").lower()
        if again != "yes":
            play = False
    print(f"\nThanks for playing! Your final score is: {score}")

    if __name__ == "__main__:":
        play.game()



play_game()