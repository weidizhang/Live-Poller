import sqlite3

class PollDB:
    def __init__(self, file_name = "polls.db"):
        self._conn = sqlite3.connect(file_name)
        self._cursor = self._conn.cursor()

        self.initialize_tables()

    def initialize_tables(self):
        with open("initial.sql") as sql_file:
            self._cursor.executescript(sql_file.read())

