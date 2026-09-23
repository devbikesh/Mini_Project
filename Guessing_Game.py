import random

def play_game():

    secret_number = random.randint(1, 50)

    while True:

        user_guess = int(input("Enter the number: "))

        if user_guess == secret_number:
            print("Correct!")
            break

        elif user_guess < secret_number:
            print("Too Low!")

        else:
            print("Too High!")


play_game()

print("Thank You For Playing!")