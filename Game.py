# Quiz Game 

# A simple interactive quiz game using Python

def quiz_game():
    print("🎯 Welcome to the Python Quiz Game!")
    print("Answer the following questions to test your knowledge.\n")

    # List of questions, options, and correct answers
    questions = [
        {
            "question": "1. Which of the following is used to display output in Python?",
            "options": ["A. cout", "B. print", "C. output", "D. show"],
            "answer": "B"
        },
        {
            "question": "2. What is the correct file extension for Python files?",
            "options": ["A. .pyth", "B. .pt", "C. .py", "D. .p"],
            "answer": "C"
        },
        {
            "question": "3. Which keyword is used to define a function in Python?",
            "options": ["A. func", "B. def", "C. function", "D. define"],
            "answer": "B"
        },
        {
            "question": "4. Which of the following is a mutable data type in Python?",
            "options": ["A. Tuple", "B. List", "C. String", "D. Integer"],
            "answer": "B"
        },
        {
            "question": "5. What does the 'len()' function do in Python?",
            "options": ["A. Returns the number of items", "B. Prints output", "C. Converts to string", "D. Creates a loop"],
            "answer": "A"
        }
    ]

    score = 0

    # Loop through each question
    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)

        answer = input("\nEnter your answer (A/B/C/D): ").upper()

        # Validate input
        while answer not in ["A", "B", "C", "D"]:
            answer = input("Invalid input! Please enter A, B, C, or D: ").upper()

        # Check answer
        if answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}.\n")

    # Final score summary
    print("🎉 Quiz Completed!")
    print(f"Your Final Score: {score} / {len(questions)}")

    if score == len(questions):
        print("🏆 Excellent! Perfect score!")
    elif score >= 3:
        print("👍 Good job! Keep practicing!")
    else:
        print("💡 Keep learning! You’ll do better next time.")

# Run the quiz
if __name__ == "__main__":
    quiz_game()
