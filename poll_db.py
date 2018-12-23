import sqlite3

from .poll import Poll
from . import config

class PollDB:
    def __init__(self):
        self._conn = sqlite3.connect(config.settings["database_file"], check_same_thread = False)
        self._cursor = self._conn.cursor()

        self.initialize_tables()

    def initialize_tables(self):
        with open("initial.sql") as sql_file:
            self._cursor.executescript(sql_file.read())

    def get_by_id(self, id):
        self._cursor.execute("SELECT * FROM polls WHERE ID=?", (id,))
        return Poll(self._cursor.fetchone())

    def get_all(self):
        self._cursor.execute("SELECT * FROM polls")
        return [ Poll(x) for x in self._cursor.fetchall() ]