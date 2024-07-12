import random


class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        answer = input(f"Q{self.question_number + 1}: {self.question_list[self.question_number].text}"
                       f" (True/False): ").lower()
        self.question_number += 1
        self.check_answer(answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, answer_):
        if answer_ == self.question_list[self.question_number - 1].answer:
            self.score += 1

