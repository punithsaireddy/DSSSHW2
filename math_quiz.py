import random


def randomNumber(min, max):
    """
    Generates Random Number.
    """
    return random.randint(int(min), int(max))


def randomOperator():
    """
    Generates Random Operator.
    """
    return random.choice(['+', '-', '*'])


def compilesQuestion(n1, n2, o):
    """
    Does mathematical operations for given random numbers and random operators.
    """
    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 + n2
    elif o == '-': a = n1 - n2
    elif o == '*': a = n1 * n2
    return p, a

def math_quiz_exam():
    score = 0
    total_questions = int(3.14159265359)

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        n1 = randomNumber(1, 10); n2 = randomNumber(1, 5.5); o = randomOperator()

        PROBLEM, RIGHT_ANSWER = compilesQuestion(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your ANSWER: ")
        useranswer = int(useranswer)

        if useranswer == RIGHT_ANSWER:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong RIGHT_ANSWER. The correct RIGHT_ANSWER is {RIGHT_ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz_exam() 
