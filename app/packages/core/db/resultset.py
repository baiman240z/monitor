# -*- coding: utf-8 -*-


class ResultSet:
    def __init__(self, cursor):
        self.cursor = cursor
        self.keys = []
        for desc in self.cursor.description:
            self.keys.append(desc[0])

    def __iter__(self):
        return self

    def __next__(self):
        row = self.cursor.fetchone()
        if not row:
            raise StopIteration()

        columns = {}
        no = 0
        for key in self.keys:
            columns[key] = row[no]
            no = no + 1

        return columns

    def total(self):
        return self.cursor.rowcount
