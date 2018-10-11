# -*- coding: utf-8 -*-
from core.config import Config
from core.db.mysql import MySQL


class Factory:
    def __init__(self):
        return

    @classmethod
    def create(cls, name="default"):
        config = Config.get(name, "database")
        if config["driver"] == "mysql":
            return MySQL(config)
