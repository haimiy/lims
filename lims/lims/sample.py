from datetime import datetime

from lims.base import LIMSBase
from lims.client import Client


class Sample(LIMSBase):
    def __init__(self,
                 sample_type: str,
                 client: Client,
                 test_order: str,
                 collection_date: datetime,
                 collection_point: str,
                 status="pending",
                 ):
        super().__init__()
        self.sample_type = sample_type
        self.client = client
        self.test_order = test_order
        self.collection_date = collection_date
        self.collection_point = collection_point
        self.status = status
        self.result = {}

    def update_status(self, new_status:str):
        self.status = new_status
        self.date_updated = datetime.now()

    def receive(self):
        self.update_status('received')

    def record_results(self, **kwargs):
        self.result.update(kwargs)

    def submit(self):
        self.update_status('submitted')

    def verify(self):
        if self.status == "submitted":
            self.update_status('verified')
        else:
            print("Can not verified")


