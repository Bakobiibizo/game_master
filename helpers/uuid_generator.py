import uuid
import pandas as pd


def generate_uuids(number_of_ids: int)-> str:
    data = pd.DataFrame({"id": [uuid.uuid4() for _ in range(number_of_ids)]})
    print(data)
    return data