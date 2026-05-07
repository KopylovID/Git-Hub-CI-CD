import pytest

from src.data import Data
from src.contact import Contact
from dataclasses import asdict
from test.test_dataset import test_ds


@pytest.fixture(scope="function")
def data_empty() -> Data:
    return Data()

@pytest.fixture(scope="function", params=[test_ds])
def data_filled(request) -> Data:
    data: Data = Data()
    for el in request.param:
        contact = Contact(*el)
        data.insert(asdict(contact))
    return data