from repository import TestsRepository
from models import *


class Evaluation:

    def __init__(self, repository: TestsRepository):
        self.repository = TestsRepository

    def grade_test(self, choices: dict, test: Test):
        score = 0
        for question in test.questions:
            if question.correct_answer_id == choices[question.question_id]:
                score += 5
        return score
