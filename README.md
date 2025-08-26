# Финальный проект 4 спринта курса "Автоматизатор тестирования на Python", "Юнит-тестирование"

## Описание проекта

Приложение "BooksCollector" позволяет создавать коллекции книг, установить им жанр, а также добавлять любимые книги в избранное. Также возможно настроить отображение только детской категории.

## Файлы:
- conftest.py - файл с фикстурами
- main.py - класс BooksCollector
- test_main.py - тестовый класс TestBooksCollector

## Набор тестовых методов класса TestBooksCollector:
1. Позитивная проверка: добавляется книга с длинной названия 8 символов
    def test_add_new_book_add_valid_book
2. Позитивная проверка: добавляется книга с длинной названия 1 и 40 символов (граничные значения)
    test_add_new_book_add_border_book_name
3. Негативная проверка: книги с наименованием 0 или длиннее 40 символов - не добавляются
    test_add_new_book_add_invalid_book_name
4. Позитивная проверка: жанр для имеющейся книги можно установить
    test_set_book_genre_getting_the_right_genre
5. Позитивная проверка: получение жанра по названию книги
    test_get_book_genre_correct_genre_by_book_title
6. Позитивная проверка: удаётся получить список книг с определённым жанром
    test_books_with_specific_genre_find_books_by_genre
7. Позитивная проверка: удаётся получить словарь books_genre
    test_get_books_genre_success
8. Позитивная проверка: удаётся получить книги, подходящие детям
    test_get_books_for_children_success
9. Позитивная проверка: книги добавляются в избранное
    test_add_book_in_favorites_success
10. Негативная проверка: добавление книги в избранное НЕ из словаря
    test_add_book_in_favorites_not_in_library
11. Позитивная проверка: книга удаляется из избранного
    test_delete_book_from_favorites_book_is_deleted  
12. Негативная проверка: удаление из избранного не добавленной туда книги
    test_delete_book_from_favorites_deleting_non_existent_book
13. Позитивная проверка: получение списка Избранных книг
    test_get_list_of_favorites_books_success

## Команда для запуска тестов
pytest -v test_main.py

## Команда для оценки покрытия
pytest --cov

## Результат выполнения тестов: 100%

conftest.py        9      0   100%
main.py           38      0   100%
test_main.py      65      0   100%