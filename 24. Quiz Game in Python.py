import time

questions = ("How many elements are there in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in Earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C","D","A","A","B")
guesses = []
# Questions, options and answers will be
# fixed, thus Tuple is used
# Guesses will append, thus List is used
score = 0
question_num = 0
# This variable is to keep track of q.no.

for question in questions:
    print("---------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT...")
        time.sleep(1)
        print(f"{answers[question_num]} is the correct answer.")
    question_num += 1
    time.sleep(1)

# As the commands go in order, "question_num"
# must be placed in indent of "question"
# instead of "option", because if
# "question_num" increments by 1 inside of
# "option", it will keep executing the
# question_num += 1 and eventually will
# reach its limit and show an error, as it
# does not have options for other questions

time.sleep(1)
print("---------------------------")
time.sleep(1)
print("          RESULTS:         ")
time.sleep(1)
print("---------------------------")

time.sleep(2)
print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()
print()

time.sleep(1)
score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")

