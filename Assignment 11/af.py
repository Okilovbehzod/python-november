
questions = [
    "What color is the sky?",
    "What is 2 + 2?",
    "Which month comes after April?",
    "How many days are there in a week?",
    "What is the capital of the United States?"
]


answers = [
    "blue",
    "4",
    "May",
    "7",
    "Washington D.C."
]

score = 0   # baroi kholhoro hisob kardan 


for i in range(len(questions)):
    print(questions[i])
    user_answer = input("Your answer: ")

    if user_answer.lower() == answers[i].lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")


print("Your final score is:", score)
