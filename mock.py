from service.repository import UsersRepository, TestsRepository
from storage.sqlite_storage import SqliteStorage

storage = SqliteStorage('./storage/data.db')
testsRepository = TestsRepository(storage)

test = testsRepository.get_all_test_info(1)

print(test)



