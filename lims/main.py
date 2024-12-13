from datetime import date, datetime

from lims.base import LIMSBase
from lims.client import Client
from lims.user import User
from lims.records import MedicalRecord
from lims.sample import Sample

if __name__ == "__main__":
    # Register a client
    client = Client("John", "Doe", "Male", date(1990, 1, 1))
    print(client)

    # Register a sample
    sample = Sample(
        sample_type="Blood",
        client=client,
        test_order="Complete Blood Count",
        collection_date=datetime.now(),
        collection_point="Lab A",
    )
    print(sample)
    # Receive and update sample status
    sample.receive()
    print(sample)

    # Record results
    sample.record_results(Hemoglobin=13.5, WBC=4500)
    print(sample)

    # Submit and verify the sample
    sample.submit()
    print(sample)
    sample.verify()
    print(sample)

    # Create a medical record
    medical_record = MedicalRecord(client, sample, sample.result)
    print(medical_record)

    # Create a user and login
    user = User("Jane Smith", "janesmith", "securepassword")
    print(user.login("janesmith", "securepassword"))
    print(user)