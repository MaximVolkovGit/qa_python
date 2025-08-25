import pytest
from main import BooksCollector

@pytest.fixture
def collection():
    collector = BooksCollector()
    return collector