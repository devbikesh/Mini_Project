import random

coin_sides = ["Heads", "Tails"]

while True:

    user_choice = input("Flip a coin (yes/no): ").lower()

    if user_choice == "yes":

        coin_result = random.choice(coin_sides)

        print("Result:", coin_result)

    elif user_choice == "no":

        print("Goodbye :(")
        break

    else:

        print("Invalid choice")
         
