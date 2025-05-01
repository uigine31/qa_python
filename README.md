# qa_python
Тесты для BooksCollector


test_add_new_book_add_one_book
Что проверяет: add_new_book.
Что делает: Добавляю одну книгу и проверяю, что она попала в books_genre с пустым жанром.

test_set_book_genre_set_genre_for_book
Что проверяет: set_book_genre.
Что делает: Добавляю книгу "1984", ставлю жанр "Фантастика" и проверяю, что жанр правильно сохранился.

test_get_books_with_specific_genre_get_books_by_genre
Что проверяет: get_books_with_specific_genre.
Что делает: Добавляю "Гарри Поттер" и "Винни Пух", ставлю им жанры "Фантастика" и "Мультфильмы", проверяю, что метод возвращает нужную книгу по жанру.

test_get_books_for_children_get_children_books
Что проверяет: get_books_for_children.
Что делает: Добавляю "Гарри Поттер" (жанр "Мультфильмы") и "Оно" (жанр "Ужасы"), проверяю, что для детей возвращается только "Гарри Поттер".

test_add_book_in_favorites_add_to_favorites
Что проверяет: add_book_in_favorites.
Что делает: Добавляю книгу, ставлю её в избранное и проверяю, что она там появилась.

test_delete_book_from_favorites_remove_from_favorites
Что проверяет: delete_book_from_favorites.
Что делает: Добавляю "Гарри Поттер" в избранное, потом убираю и проверяю, что её больше нет в избранном.

test_add_new_book_invalid_name_not_added
Что проверяет: add_new_book.
Что делает: Пробую добавить книги с длинными названиями (больше 40 символов) и проверяю, что они не добавились.

test_get_book_genre_nonexistent_book_returns_none
Что проверяет: get_book_genre.
Что делает: Проверяю, что для несуществующей книги ("Несуществующая книга") метод возвращает None.

test_get_book_genre_existing_book_returns_genre
Что проверяет: get_book_genre.
Что делает: Добавляю книгу, ставлю жанр и проверяю, что метод возвращает правильный жанр.

test_set_book_genre_nonexistent_book_no_change
Что проверяет: set_book_genre.
Что делает: Пробую поставить жанр "Фантастика" для несуществующей книги и проверяю, что books_genre остался пустым.

test_get_books_genre_returns_correct_dictionary
Что проверяет: get_books_genre.
Что делает: Добавляю две книги, ставлю жанры и проверяю, что метод возвращает правильный словарь.

test_get_list_of_favorites_books_returns_correct_list
Что проверяет: get_list_of_favorites_books.
Что делает: Добавляю две книги в избранное и проверяю, что метод возвращает правильный список.
