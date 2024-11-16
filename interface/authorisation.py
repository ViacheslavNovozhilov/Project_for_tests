from service.auth_service import AuthService
from service.exceptions import UserNotFound, InvalidPassword


print(f"Войдите в систему и выберите нужный пункт:")


class Login:
    def __init__(self, service: AuthService):
        self.service = service

    def user_choice(self):
        login = input("Введите логин: ")
        password = input("Введите пароль: ")
        user = None

        try:
            user = self.service.login(login, password)
        except UserNotFound as e:
            print("Такого пользователя не существует!")
            return
        except InvalidPassword as e:
            print("неверный пароль!")
            return

        print(f"""Если вы хотите просмотреть свои результаты, нажмите 1,
Если вы хотите заново пройти тест, нажмите 2,
Если вы хотите изменить данные, то нажмите 3 (потребуется пароль администратора!)
""")
        user_input = int(input("Введите цифру: "))
        if user_input == 1:
            pass
        elif user_input == 2:
            pass
        elif user_input == 3:
            pass

        return user
