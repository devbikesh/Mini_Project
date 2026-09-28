questions = [
    "What is the capital of Nepal?",
    "What is 5 + 5?",
    "What is the largest planet?",
    "How many days are there in a week?",
    "What is the smallest prime number?"
]

correct_answers = [
    "kathmandu",
    "10",
    "jupiter",
    "7",
    "2"
]

score = 0

for question_number in range(len(questions)):
    print(questions[question_number])

    user_answer = input("Enter your answer: ").lower()

    if user_answer == correct_answers[question_number]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    print("Current score:", score)
    print()

print("Final score:", score, "/", len(questions))

