import sqlite3


class SqliteStorage:

    def __init__(self, database_path=r"D:/PycharmProjects/interim_design/storage/data.db"):
        self.database_path = database_path
        self.connection = sqlite3.connect(database_path)
