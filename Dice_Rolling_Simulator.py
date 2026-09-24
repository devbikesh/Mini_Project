import random

while True:

    roll_choice = input("Want to roll a dice (yes/no): ").lower()

    if roll_choice == "yes":
        dice_result = random.randint(1, 6)
        print("You rolled:", dice_result)

    elif roll_choice == "no":
        print("Okay :(")
        break

    else:
        print("Invalid choice")
        continue