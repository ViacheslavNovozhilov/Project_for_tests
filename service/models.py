class Answer:
    def __init__(self, value: str, answer_id: int | None = None):
        self.answer_id = answer_id
        self.value = value

    def __str__(self):
        return self.value


class Question:

    def __init__(self, text: str, question_id: int | None = None):
        self.question_id = question_id
        self.text = text

    def __str__(self):
        return self.text


class Test:
    id: int | None = None
    title: str
    category: str

    def __str__(self):
        return self.title

    def __init__(self, title: str, category: str, test_id: int = None):
        self.title = title
        self.category = category
        self.id = test_id


class User:
    user_id: int | None = None
    username: str
    password: str


class Admin:
    admin_user_id: int | None = None
    user_id: int


class CorrectAnswer:
    correct_answer_id: int | None = None
    answer_id: int
