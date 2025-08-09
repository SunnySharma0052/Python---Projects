# Project: CLI Quiz App 
# Goal:
# Make a Command Line Interface (CLI) Quiz App using everything you've learned.


def ask_question(q, a):
    user_input = input(f"{q} ")
    return user_input.strip().lower() == a.lower()


def main():
    score = 0
    questions = [
        {"Question" :"Who was first prime minister in india ?",
        "Answer" : "Jawaharlal Nehru"},
        {"Question" : "Father Of Python ?",
        "Answer" : "Guido van Rossum"},
        {"Question" : "How many population of india ?",
        "Answer" : "1.46 billion"},
    ]

    print("Welcome To The Sunny  Quiz")

    for q in questions:
        if ask_question(q["Question"], q["Answer"]):
            print("Correct Answer!")
            score += 1
        else:
            print(f"❌ Wrong! \n The correct answer is: {q['Answer']}")

    print(f"🎉 You scored {score}/{len(questions)}")

if __name__ == "__main__":
    main()
