import random

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

i = 0
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"].lower()))
    # print(question_bank[i].text + " " + question_bank[i].answer)
    # i += 1

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    answer = quiz.next_question()

print(f"your final score is {quiz.score}!")