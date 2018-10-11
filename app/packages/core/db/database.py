# -*- coding: utf-8 -*-
import sys
from core.db.resultset import ResultSet


class Database:
    def __init__(self, config):
        self.config = config
        self.db = False
        self.cursor = False

    def connect(self):
        print("This is abstract class!")
        sys.exit()

    def execute(self, sql, params=()):
        self.connect()
        if type(params) != list and type(params) != tuple:
            params = (params,)
        self.cursor.execute(sql, params)

    def all(self, sql, params=()):
        self.execute(sql, params)
        keys = []
        for desc in self.cursor.description:
            keys.append(desc[0])

        rows = []
        for row in self.cursor:
            columns = {}
            no = 0
            for key in keys:
                columns[key] = row[no]
                no = no + 1
            rows.append(columns)

        return rows

    def row(self, sql, params=()):
        self.execute(sql, params)
        keys = []
        for desc in self.cursor.description:
            keys.append(desc[0])

        row = self.cursor.fetchone()
        if not row:
            return False

        columns = {}
        no = 0
        for key in keys:
            columns[key] = row[no]
            no = no + 1

        return columns

    def one(self, sql, params=()):
        self.execute(sql, params)

        row = self.cursor.fetchone()
        if not row:
            return False
        else:
            return row[0]

    def close(self):
        self.db.close()

    def count(self):
        if self.cursor:
            return self.cursor.rowcount
        else:
            return 0

    def commit(self):
        self.db.commit()

    def rollback(self):
        self.db.rollback()

    def result(self, sql, params=()):
        self.execute(sql, params)
        return ResultSet(self.cursor)
