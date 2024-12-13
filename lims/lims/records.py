from lims.base import LIMSBase
from lims.client import Client
from lims.sample import Sample


class MedicalRecord(LIMSBase):
    def __init__(self, sample, client, result):
        super().__init__()
        self.client = client
        self.sample = sample
        self.result = result