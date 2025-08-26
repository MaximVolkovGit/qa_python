import pytest
from main import BooksCollector

class TestBooksCollector:

    '''Позитивная проверка: добавляется книга с длинной названия 8 символов'''
    def test_add_new_book_add_valid_book(self, collection):
        collection.add_new_book('Бородино')
        assert collection.get_books_genre() == {'Бородино': ''}
 
    '''Позитивная проверка: добавляется книга с длинной названия 1 и 40 символов (граничные значения)'''
    @pytest.mark.parametrize('valid_books', 
        ['A',
        'A'*40
        ])
    def test_add_new_book_add_border_book_name(self, collection, valid_books):
        collection.add_new_book(valid_books)
        assert valid_books in collection.get_books_genre()
        assert collection.get_books_genre()[valid_books] == ''
    
    '''Негативная проверка: книги с наименованием 0 или длиннее 40 символов - не добавляются'''
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
    def test_get_books_genre_success(self, collection, test_library):
        collection.books_genre = test_library
        assert collection.get_books_genre() == {
            'Джуманджи': 'Фантастика',
            'Властелин Колец': 'Фантастика', 
            'Молчание ягнят': 'Ужасы',
            'Пуаро': 'Детективы',
            'Сборник анекдотов': 'Комедии'
        }
    
    '''Позитивная проверка: удаётся получить книги, подходящие детям'''
    def test_get_books_for_children_success(self,collection, test_library):
        collection.books_genre = test_library
        assert collection.get_books_for_children() == ['Джуманджи', 'Властелин Колец', 'Сборник анекдотов']

    '''Позитивная проверка: книги добавляются в избранное'''
    def test_add_book_in_favorites_success(self, collection, test_library):
        collection.books_genre = test_library
        collection.add_book_in_favorites('Пуаро')
        collection.add_book_in_favorites('Джуманджи')
        assert collection.get_list_of_favorites_books() == ['Пуаро', 'Джуманджи']

    '''Негативная проверка: добавление книги в избранное НЕ из словаря'''
    def test_add_book_in_favorites_not_in_library(self, collection, test_library):
        collection.books_genre = test_library
        collection.add_book_in_favorites('Несуществующая книга')
        assert  collection.get_list_of_favorites_books() == []

    '''Позитивная проверка: книга удаляется из избранного'''
    def test_delete_book_from_favorites_book_is_deleted(self, collection):
        collection.add_new_book('Властелин колец')
        collection.add_book_in_favorites('Властелин колец')
        collection.delete_book_from_favorites('Властелин колец')
        assert collection.get_list_of_favorites_books() == []

    '''Негативная проверка: удаление из избранного не добавленной туда книги'''
    def test_delete_book_from_favorites_deleting_non_existent_book(self, collection):
        collection.add_new_book('Властелин колец')
        collection.add_book_in_favorites('Властелин колец')
        collection.delete_book_from_favorites('Несуществующая книга')
        assert collection.get_list_of_favorites_books() == ['Властелин колец']

    '''Позитивная проверка: получение списка Избранных книг'''
    def test_get_list_of_favorites_books_success(self, collection):
        collection.add_new_book('Каштанка')
        collection.add_book_in_favorites('Каштанка')
        assert collection.get_list_of_favorites_books() == ['Каштанка']