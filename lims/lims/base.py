from datetime import datetime
from uuid import uuid1

class LIMSBase:
    """" LIMS BASE class definition """
    def __init__(self):
        # Automatically generates a UUID for the id attribute using uuid1
        self.id = uuid1()

        # Sets the current DateTime for date_created and date_updated
        self.date_created = datetime.now()
        self.date_updated = datetime.now()


    def __repr__(self):
        return f"<{self.__class__.__name__}: ({self.__dict__})>"