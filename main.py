from service.repository import UsersRepository, TestsRepository
from storage.sqlite_storage import SqliteStorage
from service.auth_service import AuthService
from service.test_service import TestsService
from interface.authorisation import Login
from interface.tests import Tests
from service.evaluation_service import EvaluationService


def main():
    storage = SqliteStorage('./storage/data.db')
    userRepository = UsersRepository(storage)
    testsRepository = TestsRepository(storage)

    auth = AuthService(userRepository)
    testsService = TestsService(testsRepository)

    authInterface = Login(auth)
    testsInterface = Tests(testsService)

    evaluationService = EvaluationService(testsRepository)


    while True:
        user = authInterface.user_choice()
        if user is None:
            continue
        user_input = int(input("""Нажмите 1, если вы хотите просмотреть предыдущие результаты.
Нажмите 2, если вы хотите пройти тест.
Нажмите 3, если вы хотите внести изменения (потребуется пароль администратора)
"""))
        if user_input == 1:
            pass
        elif user_input == 2:
            test = testsInterface.choose_test()
            print(test.test_id)
            user_choice = testsInterface.run_test(test)
            user_result = evaluationService.grade_test(user_choice, test)
            print(f"Вы набрали {user_result} баллов")

        elif user_input == 3:
            pass


if __name__ == '__main__':
    main()
