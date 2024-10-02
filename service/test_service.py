from service.repository import TestsRepository
from service.models import Test


class TestsService:
    def __init__(self, repository: TestsRepository):
        self.repository = repository

    def get_all(self):
        return self.repository.get_tests()

    def collect_test(self, test: Test):
        return self.repository.get_full_test(test.id)
