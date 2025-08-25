import pytest
from main import BooksCollector

class TestBooksCollector:

    # def test_add_new_book_add_two_books(self):
    #     collector = BooksCollector()
    #     collector.add_new_book('Гордость и предубеждение и зомби')
    #     collector.add_new_book('Что делать, если ваш кот хочет вас убить')
    #     assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # ''' Негативная проверка: книги с наименованием 0 или длиннее 40 символов - не добавляются'''
    # @pytest.mark.parametrize('invalid_books', 
    #     ['',
    #     'A'*50
    #     ])
    # def test_add_new_book_add_invalid_book_name(self, invalid_books):
    #     collector = BooksCollector()
    #     collector.add_new_book(invalid_books)
    #     assert len(collector.get_books_genre()) == 0

    '''Позитивная проверка: жанр для имеющейся книги можно установить'''
    def test_set_book_genre_getting_the_right_genre(self):
        #collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        assert collector.get_book_genre('Властелин колец') == 'Фантастика'

    # '''Позитивная проверка: получение жанра по названию книги'''
    # def test_get_book_genre_correct_genre_by_book_title(self):
    #     collector = BooksCollector()
    #     collector.add_new_book('Недоросль')
    #     collector.set_book_genre('Недоросль', 'Комедии')
    #     assert collector.get_book_genre('Недоросль') == 'Комедии'

    # '''Позитивная проверка: удаётся получить список книг с определённым жанром'''
    # def test_books_with_specific_genre_find_books_by_genre(self):
    #     collector = BooksCollector()
    #     collector.books_genre = {
    #         'Джуманджи': 'Фантастика',
    #         'Властелин Колец': 'Фантастика', 
    #         'Молчание ягнят': 'Ужасы',
    #         'Пуаро': 'Детективы',
    #     }
    #     assert collector.get_books_with_specific_genre('Фантастика') == ['Джуманджи',  'Властелин Колец']

    # '''Позитивная проверка: удаётся получить словарь books_genre'''
    # def test_get_books_genre(self):
    #     collector = BooksCollector()
    #     collector.books_genre = {
    #         'Властелин Колец': 'Фантастика', 
    #         'Молчание ягнят': 'Ужасы',
    #         }
    #     assert collector.get_books_genre() == {'Властелин Колец': 'Фантастика', 
    #                                             'Молчание ягнят': 'Ужасы'}
    
    # '''Позитивная проверка: удаётся получить книги, подходящие детям'''
    # def test_get_books_for_children_success(self)