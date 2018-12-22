import json
import time

class Poll:
    def __init__(self, data_tuple):
        self._data = data_tuple

    @staticmethod
    def timestamp():
        return int(time.time())

    def is_empty(self):
        return len(self._data) == 0

    def is_closed(self):
        return Poll.timestamp() >= self.closes()

    def id(self):
        return self._data[0]

    def question(self):
        return self._data[1]

    def created(self):
        return self._data[2]

    def closes(self):
        return self._data[3]

    def choices(self):
        return json.loads(self._data[4])

    def num_choices(self):
        return self._data[5]

    def is_valid_choice(self, choice):
        try:
            choice = int(choice)
            return 1 <= choice <= self.num_choices()
        except:
            pass

        return False