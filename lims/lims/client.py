from datetime import date

from lims.base import LIMSBase


class Client(LIMSBase):
    def __init__(self,
                 first_name: str,
                 last_name: str,
                 gender: str,
                 birth_date: date,
                 medical_records=None or list[dict]
                 ):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.birth_date = birth_date
        self.medical_records = medical_records
