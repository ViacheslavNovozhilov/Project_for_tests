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
            test = Test(row[1], row[2])
            tests.append(test)
        return tests
    
    def get_emty_test(self, test_id: int) -> Test:
        """
        Метод для получения теста без доп информации. Только id, категорию и название
        Используется в других методах репозитория
        """
        cursor = self.storage.connection.cursor()
        query = "SELECT * from Tests WHERE TestId=" + str(test_id)
        cursor.execute(query)
        row = cursor.fetchone()
        return Test(row[1], row[2], row[0])



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

    def get_all_test_info(self, test_id: int):
        cursor = self.storage.connection.cursor()
        emty_test = self.get_emty_test(test_id)
        questions_query = """
        select q.*, ca.AnswerId
        from TestsAndQuestions as j
        join Questions as q 
        on j.QuestionId = q.QuestionId
        join CorrectAnswers as ca           # код для примера
        on ca.QuestionId = q.QuestionId     #
        WHERE j.TestId=
        """+str(test_id)
        cursor.execute(questions_query)
        raw_questions = cursor.fetchall()
        for row in raw_questions:
            emty_test.questions.append(Question(row[1], row[0]))

        answers_query = """
        select a.*
        from QuestionsAndAnswers as qa
        join Answers as a
        on qa.AnswerId = a.AnswerId
        WHERE qa.QuestionId=
        """
        for question in emty_test.questions:
            cursor.execute(answers_query+str(question.question_id))
            raw_answers = cursor.fetchall()
            for row in raw_answers:
                question.answers.append(Answer(row[1], row[0]))
        
        return emty_test



class UsersRepository(BaseRepository):
    def get_user(self, users_id):
        cursor = self.storage.connection.cursor()
        query = f"SELECT * FROM Users WHERE UserId = {users_id};"
        cursor.execute(query)
        rows = cursor.fetchone()
        return rows

    def get_username(self, username: str):
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
