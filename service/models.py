class Answer:
    def __init__(self, value: str, answer_id: int | None = None):
        self.answer_id = answer_id
        self.value = value

    def __str__(self):
        return self.value


class Question:
    answers = list[Answer]

    def __init__(self, text: str, question_id: int | None = None, correct_answer_id: int | None = None): # подразумевается id правильного ответа
        self.question_id = question_id
        self.answer_id = correct_answer_id
        self.text = text

    def __str__(self):
        return self.text


class Test:
    questions: list[Question]

    def __str__(self):
        return self.title

    def __init__(self, title: str, category: str, test_id: int = None):
        self.title = title
        self.category = category
        self.test_id = test_id


class User:

    user_id: int | None = None
    username: str
    password: str


class Admin:
    def __init__(self, admin_user_id, user_id):
        self.user_id = user_id
        self.admin_user_id = admin_user_id

