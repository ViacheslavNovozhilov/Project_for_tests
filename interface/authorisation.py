from service.auth_service import AuthService
from service.exceptions import UserNotFound, InvalidPassword


class Login:
    def __init__(self, service: AuthService):
        self.service = service

    def login_form(self):
        login = input("Login: ")
        password = input("Password: ")
        user = None

        try:
            user = self.service.login(login, password)
        except UserNotFound as e:
            print("Такого пользователя не существует!")
            return
        except InvalidPassword as e:
            print("неверный пароль!")
            return
        return user
