from storage.sqlite_storage import SqliteStorage

storage = SqliteStorage(r"D:/PycharmProjects/interim_design/storage/data.db")


def get_correct_answer():
    cursor = storage.connection.cursor()
    correct_answer_query = f"""
    SELECT a.AnswerId 
    FROM Answers as a 
    JOIN CorrectAnswers as ca ON a.AnswerId = ca.AnswerId
    JOIN Questions as q ON ca.QuestionId = q.QuestionId
    """
    cursor.execute(correct_answer_query)
    rows = cursor.fetchall()

    correct_answers = [row[0] for row in rows]  # Извлекаем только id правильных ответов
    print(correct_answers)
    return correct_answers


get_correct_answer()
