import random

options = ("Rock", "Paper", "Scissor")

playing = True

while playing:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (Rock, Paper, Scissor): ").capitalize()

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It is a tie!")
    elif player == "Paper" and computer == "Rock":
        print("You Win!")
    elif player == "Scissor" and computer == "Paper":
        print("You Win!")
    elif player == "Rock" and computer == "Scissor":
        print("You Win!")
    else:
        print("You Lose!")

    play_again = input("Play again (y/n): ").lower()

    if play_again != "y":
        playing = False

print("Thanks for playing!")