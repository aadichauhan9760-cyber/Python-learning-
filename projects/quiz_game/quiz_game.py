def quiz_game():
    questions = [
        {
            "question": "What is the correct file extension for Python files?",
            "options": ["A. .java", "B. .py", "C. .html", "D. .cpp"],
            "answer": "B"
        },
        {
            "question": "Which function is used to display output in Python?",
            "options": ["A. input()", "B. print()", "C. display()", "D. output()"],
            "answer": "B"
        },
        {
            "question": "Which symbol is used for comments in Python?",
            "options": ["A. //", "B. <!-- -->", "C. #", "D. **"],
            "answer": "C"
        },
        {
            "question": "Which keyword is used to define a function?",
            "options": ["A. function", "B. define", "C. def", "D. fun"],
            "answer": "C"
        },
        {
            "question": "Which data type stores True or False?",
            "options": ["A. String", "B. Integer", "C. Boolean", "D. Float"],
            "answer": "C"
        }
    ]

    score = 0

    print("=" * 45)
    print("          PYTHON QUIZ GAME")
    print("=" * 45)

    for number, quiz in enumerate(questions, start=1):
        print(f"\nQuestion {number}: {quiz['question']}")

        for option in quiz["options"]:
            print(option)

        while True:
            user_answer = input("Your answer (A/B/C/D): ").upper()

            if user_answer in ["A", "B", "C", "D"]:
                break

            print("❌ Please enter only A, B, C, or D.")

        if user_answer == quiz["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {quiz['answer']}")

    total_questions = len(questions)
    percentage = (score / total_questions) * 100

    print("\n" + "=" * 45)
    print("              QUIZ RESULT")
    print("=" * 45)
    print(f"Correct answers : {score}")
    print(f"Wrong answers   : {total_questions - score}")
    print(f"Score           : {score}/{total_questions}")
    print(f"Percentage      : {percentage:.1f}%")

    if percentage >= 80:
        print("🏆 Excellent performance!")
    elif percentage >= 60:
        print("👍 Good job!")
    elif percentage >= 40:
        print("📚 Keep practicing!")
    else:
        print("💪 Don't give up. Keep learning!")

    print("=" * 45)


if __name__ == "__main__":
    quiz_game()
