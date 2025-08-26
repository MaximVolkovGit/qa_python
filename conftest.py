import pytest
from main import BooksCollector

@pytest.fixture
def collection():
    collection = BooksCollector()
    return collection

@pytest.fixture
def test_library():
    return {
            'Джуманджи': 'Фантастика',
            'Властелин Колец': 'Фантастика', 
            'Молчание ягнят': 'Ужасы',
            'Пуаро': 'Детективы',
            'Сборник анекдотов': 'Комедии'
        }