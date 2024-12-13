from datetime import datetime

from lims.base import LIMSBase


class User(LIMSBase):
    def __init__(self, full_name, username, password):
        super().__init__()
        self.full_name = full_name
        self.username = username
        self.password = password
        self.active = False

    def login(self, username, password):
        if self.username == username and self.password == password:
            self.active = True
            self.date_updated = datetime.now()
            return True
        return False


