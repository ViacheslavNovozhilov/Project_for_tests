from storage.sqlite_storage import SqliteStorage


class Migrator:
    def __init__(self, storage: SqliteStorage):
        self.storage = storage

    def migrate(self):

        self.storage.connection.execute("""
        CREATE TABLE IF NOT EXISTS Answers (
        AnswerId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Value TEXT NOT NULL
        )
        """)

        self.storage.connection.execute("""
        CREATE TABLE IF NOT EXISTS CorrectAnswers (
        CorrectAnswerId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        AnswerId INTEGER NOT NULL UNIQUE,
        FOREIGN KEY (AnswerId) REFERENCES Answers(AnswerId)
        )
        """)

        self.storage.connection.execute("""
        CREATE TABLE IF NOT EXISTS Questions (
        QuestionId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Text TEXT NOT NULL
        )
        """)

        self.storage.connection.execute("""
        CREATE TABLE IF NOT EXISTS TestsAndQuestions (
        TestId INTEGER NOT NULL,
        QuestionId INTEGER NOT NULL,
        FOREIGN KEY (TestId) REFERENCES Tests(TestId),
        FOREIGN KEY (QuestionId) REFERENCES Questions(QuestionId)
        )
        """)

        self.storage.connection.execute("""
        CREATE TABLE IF NOT EXISTS QuestionsAndAnswers (
        QuestionId INTEGER NOT NULL,
        AnswerId INTEGER NOT NULL,
        FOREIGN KEY (QuestionId) REFERENCES Questions(QuestionId),
        FOREIGN KEY (AnswerId) REFERENCES Answers(AnswerId)
        )
        """)

        self.storage.connection.execute("""
        CREATE TABLE IF NOT EXISTS Tests (
        TestId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Title TEXT NOT NULL,
        Category INTEGER
        )
        """)

        self.storage.connection.execute("""
        CREATE TABLE IF NOT EXISTS Users (
        UserId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Username TEXT NOT NULL,
        Password NUMERIC NOT NULL
        )
        """)

        self.storage.connection.execute("""
        CREATE TABLE IF NOT EXISTS Admins (
        AdminUserId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        UserId INTEGER NOT NULL UNIQUE,
        FOREIGN KEY (UserId) REFERENCES Users(UserId)
        )
        """)

        self.storage.connection.execute("""
        CREATE TABLE IF NOT EXISTS Results (
        ResultId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        UserId INTEGER,
        TestId INTEGER,
        Score INTEGER,
        FOREIGN KEY (UserId) REFERENCES Users(UserId),
        FOREIGN KEY (TestId) REFERENCES Tests(TestId)
        )
        """)

        self.storage.connection.commit()
        self.storage.connection.close()


migrator = Migrator(SqliteStorage("data.db"))
migrator.migrate()
