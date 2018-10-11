# -*- coding: utf-8 -*-
import MySQLdb
from core.db.database import Database

class MySQL(Database):
    def connect(self):
        if self.db:
            return

        self.db = MySQLdb.connect(
            host=self.config["host"],
            db=self.config["db"],
            user=self.config["user"],
            passwd=self.config["password"],
            charset=self.config["charset"]
        )
        self.cursor = self.db.cursor()
