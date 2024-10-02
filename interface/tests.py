from service.test_service import TestsService
from service.models import Test


class Tests:
    def __init__(self, service: TestsService):
        self.service = service

    def choose_test(self):
        print('Выберите тест:')
        tests = self.service.get_all()
        for i in range(len(tests)):
            print(f'{i + 1}. {tests[i]}')
        choise = input()
        return tests[int(choise) - 1]

    def run_test(self, raw_test: Test):
        test = self.service.collect_test(raw_test)
        print(test.title + "\n")
        user_choises = {}
        for question in test.questions:
            print("== " + str(question) + " ==")
            for i in range(len(question.answers)):
                print(f"{i + 1}. {question.answers[i]}")
            choise = int(input())
            user_choises[question.id] = question.answers[choise - 1].id
        return user_choises
