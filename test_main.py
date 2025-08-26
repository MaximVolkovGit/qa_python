import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collection):
        collection.add_new_book('Гордость и предубеждение и зомби')
        collection.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collection.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    ''' Негативная проверка: книги с наименованием 0 или длиннее 40 символов - не добавляются'''
    @pytest.mark.parametrize('invalid_books', 
        ['',
        'A'*50
        ])
    def test_add_new_book_add_invalid_book_name(self, collection, invalid_books):
        collection.add_new_book(invalid_books)
        assert len(collection.get_books_genre()) == 0

    '''Позитивная проверка: жанр для имеющейся книги можно установить'''
    def test_set_book_genre_getting_the_right_genre(self,collection):
        collection.add_new_book('Властелин колец')
        collection.set_book_genre('Властелин колец', 'Фантастика')
        assert collection.get_book_genre('Властелин колец') == 'Фантастика'

    
        '''Позитивная проверка: получение жанра по названию книги'''
    def test_get_book_genre_correct_genre_by_book_title(self, collection):
        collection.add_new_book('Недоросль')
        collection.set_book_genre('Недоросль', 'Комедии')
        assert collection.get_book_genre('Недоросль') == 'Комедии'

    '''Позитивная проверка: удаётся получить список книг с определённым жанром'''
    def test_books_with_specific_genre_find_books_by_genre(self,collection, test_library):
        collection.books_genre = test_library
        assert collection.get_books_with_specific_genre('Фантастика') == ['Джуманджи',  'Властелин Колец']

    '''Позитивная проверка: удаётся получить словарь books_genre'''
    def test_get_books_genre(self, collection, test_library):
        #collection = BooksCollector()
        collection.books_genre = test_library
        assert collection.get_books_genre() == {
            'Джуманджи': 'Фантастика',
            'Властелин Колец': 'Фантастика', 
            'Молчание ягнят': 'Ужасы',
            'Пуаро': 'Детективы',
        }
    
    # '''Позитивная проверка: удаётся получить книги, подходящие детям'''
    # def test_get_books_for_children_success(self):
        