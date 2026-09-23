import random

while True:

    choices = ["rock", "paper", "scissor"]

    computer_choice = random.choice(choices)

    user_choice = input("Choose between Rock, Paper, Scissor: ")

    if computer_choice == user_choice:
        print("Draw")
        continue

    elif user_choice == "rock" and computer_choice == "scissor":
        print("You Win")

    elif user_choice == "paper" and computer_choice == "rock":
        print("You Win")

    elif user_choice == "scissor" and computer_choice == "paper":
        print("You Win")

    else:
        print("Computer Wins")

    play_again = input("Do you want to play again? yes/no: ")

    if play_again == "no":
        break

print("Thanks for playing!")