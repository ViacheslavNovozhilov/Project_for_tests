from storage.sqlite_storage import SqliteStorage
from service.models import Test, Question, Answer, User, Admin


class BaseRepository:
    def __init__(self, storage: SqliteStorage):
        self.storage = storage


class TestsRepository(BaseRepository):
    def get_all_tests(self):
        cursor = self.storage.connection.cursor() # при создании репозитория даем подключения к базе
        query = f"SELECT * FROM Tests;"
        cursor.execute(query)
        rows = cursor.fetchall()
        tests = []
        for row in rows:
            test = Test(row[1], row[2], row[0])
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

    def get_all_answer(self):
        cursor = self.storage.connection.cursor()
        query = f"SELECT * FROM Answers;"
        cursor.execute(query)
        rows = cursor.fetchall()
        answers = []
        for row in rows:
            answer = Answer(row[1], row[2])
            answers.append(answer)
        return answers

    def get_correct_answer(self):
        cursor = self.storage.connection.cursor()
        correct_answer_query = f"""
        SELECT a.AnswerId 
        FROM Answers as a 
        JOIN CorrectAnswers as ca ON a.AnswerId = ca.AnswerId
        JOIN Questions as q ON ca.QuestionId = q.QuestionId
        """
        cursor.execute(correct_answer_query)
        rows = cursor.fetchall()

        correct_answers = [row[0] for row in rows]  # Извлекаем только id правильных ответов
        return correct_answers

    def get_all_test_info(self, test_id: int):
        cursor = self.storage.connection.cursor()
        test_query = f"""
            SELECT * FROM Tests
            WHERE Tests.TestId = {test_id};
        """
        cursor.execute(test_query)
        raw_data = cursor.fetchone()

        test = Test(test_id=raw_data[0], title=raw_data[1], category=raw_data[2])
        test.questions = []

        questions_query = f"""
        select q.QuestionId, q.Text
        from TestsAndQuestions as tq
        join Questions as q on q.QuestionId = tq.QuestionId
        where tq.TestId = {test_id};
        """

        cursor.execute(questions_query)
        questions_data = cursor.fetchall()
        for question in questions_data:
            test.questions.append(Question(question[1], question[0]))

        answers_query = """
        select a.AnswerId, a.Value
        from QuestionsAndAnswers as qa
        join Answers as a on a.AnswerId = qa.AnswerId
        where qa.QuestionId=
        """

        for question in test.questions:
            raw_answers = cursor.execute(answers_query + str(question.question_id)).fetchall()
            question.answers = []
            for answer in raw_answers:
                answer = Answer(answer[1], answer[0])
                question.answers.append(answer)

        correct_answer_query = f"""
        SELECT q.QuestionId, q."Text", t.TestId, t.Title, a.AnswerId, a.Value 
        From Questions as q
        join TestsAndQuestions as taq on q.QuestionId = taq.QuestionId
        join Tests as t on taq.TestId = t.TestId
        join CorrectAnswers as ca ON q.QuestionId = ca.QuestionId
        join Answers as a on ca.AnswerId = a.AnswerId 
        WHERE q.QuestionId =
        """

        for question in test.questions:
            row = cursor.execute(correct_answer_query + str(question.question_id)).fetchone()
            question.correct_answer_id = row[4]

        return test


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

    def get_admins(self):
        cursor = self.storage.connection.cursor()
        query = f"SELECT * FROM Admins JOIN Users ON Users.UserId = Admins.UserId;"
        cursor.execute(query)
        rows = cursor.fetchall()
        admins = []
        for row in rows:
            admin = Admin(row[0], row[1])
            admins.append(admin)
        return admins

