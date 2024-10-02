from storage.sqlite_storage import SqliteStorage
from service.models import Test, Question, Answer, User


class BaseRepository:
    def __init__(self, storage: SqliteStorage):
        self.storage = storage


class TestsRepository(BaseRepository):
    def get_tests(self):
        cursor = self.storage.connection.cursor()
        query = f"SELECT * FROM Tests;"
        cursor.execute(query)
        rows = cursor.fetchall()
        tests = []
        for row in rows:
            test = Test(row[1], row[2], row[3])
            tests.append(test)
        return tests

    def get_all_question(self):
        cursor = self.storage.connection.cursor()
        query = f"SELECT * FROM Tests;"
        cursor.execute(query)
        rows = cursor.fetchall()
        questions = []
        for row in rows:
            question = Question(row[1], row[2])
            questions.append(question)
        return questions

    def get_all_answer(self, data: list | tuple, question_id: int):
        cursor = self.storage.connection.cursor()
        query = f"SELECT * FROM Answers;"
        cursor.execute(query)
        rows = cursor.fetchall()
        answers = []
        for row in rows:
            answer = Answer(row[1], row[2])
            answers.append(answer)
        return answers

    def get_correct_answer(self, data: list | tuple, correct_answer_id: int):
        pass

    def get_admins(self, data: list | tuple, admin_user_id: int):
        pass

    def get_full_test(self, test_id: int):
        cursor = self.storage.connection.cursor()
        query = f"""
            SELECT * FROM Tests
            JOIN questions ON tests.id = questions.tests_id
            JOIN answers ON answers.question = questions.id
            WHERE tests.id = {test_id}
            order by questions.id;
        """
        cursor.execute(query)
        raw_data = cursor.fetchall()

        test = Test(test_id=raw_data[0][0], title=raw_data[0][1], category=raw_data[0][3])
        test.questions = []
        for row in raw_data:
            question_id = row[4]
            if len(test.questions) == 0 or question_id != test.questions[-1].question_id:
                question = Question(text=row[5])
                question.answers = self.get_all_answer(raw_data, question.question_id)
                test.questions.append(question)

        return test


class UsersRepository(BaseRepository):
    def get_user(self, users_id):
        cursor = self.storage.connection.cursor()
        query = f"SELECT * FROM Users WHERE UserId = {users_id};"
        cursor.execute(query)
        rows = cursor.fetchone()
        return rows

    def get_by_username(self, username: str):
        cursor = self.storage.connection.cursor()
        query = f"SELECT * FROM Users WHERE Username = '{username}';"
        cursor.execute(query)
        rows = cursor.fetchone()
        if rows is None:
            return None
        user = User()
        user.user_id = rows[0]
        user.username = rows[1]
        user.password = rows[2]
        return user
