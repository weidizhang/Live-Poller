import sqlite3

from .poll import Poll

class PollDB:
    def __init__(self, file_name = "polls.db"):
        self._conn = sqlite3.connect(file_name, check_same_thread = False)
        self._cursor = self._conn.cursor()

        self.initialize_tables()

    def initialize_tables(self):
        with open("initial.sql") as sql_file:
            self._cursor.executescript(sql_file.read())

    def get_by_id(self, id):
        self._cursor.execute("SELECT * FROM polls WHERE ID=?", (id,))
        return Poll(self._cursor.fetchone())
