import random

def get_choices():
    player_choice = input("Enter a choice (rock,paper,scissors): ")
    options = ["rock","paper","scissors"]
    computer_choice = random.choice(options)
    choices = {"player":player_choice,"computer":computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player},computer chose {computer}")
    if player == computer:
        return "its a tie"
    elif player == "rock" :
        if computer == "scissors":
            return "rock smashed scissors, you win"
        else:
            return "paper covers rock, you lose"
    elif player == "scissors" :
        if computer == "rock":
            return "scissors got smashed by rock, you lose"
        else:
            return "you cut paper, you win"
    elif player == "paper" :
        if computer == "scissors":
            return "scissors cuts you, you lose"
        else:
            return "you cover rock, you win"

choices = get_choices()

result = check_win(choices["player"],choices["computer"])
print(result)









