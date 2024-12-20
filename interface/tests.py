from service.test_service import TestsService
from service.models import Test
from pprint import pprint


class Tests:
    def __init__(self, service: TestsService):
        self.service = service

    def choose_test(self):
        print("Выберите тест:")
        tests = self.service.get_all()
        for i in range(len(tests)):
            print(f"{i + 1}. {tests[i]}")
        choice = input()
        test = tests[int(choice) - 1]
        return self.service.collect_test(test)

    def run_test(self, raw_test: Test):
        test = self.service.collect_test(raw_test)
        print(test.title + "\n")
        user_choices = {}
        for question in test.questions:
            pprint(str(question))
            for i in range(len(question.answers)):
                print(f"{i + 1}. {question.answers[i]}")
            choice = int(input())
            user_choices[question.question_id] = question.answers[choice - 1].answer_id
        return user_choices
