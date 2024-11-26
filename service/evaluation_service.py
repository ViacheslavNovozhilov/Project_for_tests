from repository import TestsRepository
from models import *


class EvaluationService:

    def __init__(self, repository: TestsRepository):
        self.repository = repository

    def grade_test(self, choices: dict, test: Test):
        score = 0
        for question in test.questions:
            if question.correct_answer_id == choices[question.question_id]:
                score += 1
        print(score)
        return score
