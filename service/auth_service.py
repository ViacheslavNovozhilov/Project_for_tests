from service.repository import UsersRepository
from service.exceptions import UserNotFound, InvalidPassword
from service.models import User


class AuthService:
    def __init__(self, repository: UsersRepository):
        self.repository = repository

    def login(self, username: str, password: str) -> User:
        user = self.repository.get_by_username(username)
        if not user:
            raise UserNotFound(username)
        if user.password != password:
            raise InvalidPassword(username)
        return user
