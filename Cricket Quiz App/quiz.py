quiz = {
    "Who is hitman": "Rohit",
    "Best bowler of india ?": "Bumrah",
    "Who is Master Blaster": "Sachin",
    "Who is king": "Kohli",
    "Who is best captain for India": "Dhoni"
}

print("\n::::::::GET READY FOR CRICKET QUIZ::::::::")

score = 0

for question, answer in quiz.items():

    user_answer = input(question + " : ")
    if user_answer.strip().lower() == answer.lower():
        print("Correct ✅")
        score += 1

    else:
        print("Wrong ❌")
        print("Correct Answer:", answer)

print("\nQuiz Finished!")
print("Your Score:", score, "/", len(quiz))