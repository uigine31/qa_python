import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize("book_name", ["Гарри Поттер", "Властелин колец"])
    def test_add_new_book_add_one_book(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()
        assert collector.get_books_genre()[book_name] == ""

    def test_set_book_genre_set_genre_for_book(self):
        collector = BooksCollector()
        collector.add_new_book("1984")
        collector.set_book_genre("1984", "Фантастика")
        assert collector.get_book_genre("1984") == "Фантастика"

    @pytest.mark.parametrize("genre, expected_book", [
        ("Фантастика", "Гарри Поттер"),
        ("Мультфильмы", "Винни Пух")
    ])
    def test_get_books_with_specific_genre_get_books_by_genre(self, genre, expected_book):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.add_new_book("Винни Пух")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        collector.set_book_genre("Винни Пух", "Мультфильмы")
        books = collector.get_books_with_specific_genre(genre)
        assert expected_book in books

    def test_get_books_for_children_get_children_books(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.add_new_book("Оно")
        collector.set_book_genre("Гарри Поттер", "Мультфильмы")
        collector.set_book_genre("Оно", "Ужасы")
        children_books = collector.get_books_for_children()
        assert "Гарри Поттер" in children_books and "Оно" not in children_books

    @pytest.mark.parametrize("book_name", ["Гарри Поттер", "1984"])
    def test_add_book_in_favorites_add_to_favorites(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        favorites = collector.get_list_of_favorites_books()
        assert book_name in favorites

    def test_delete_book_from_favorites_remove_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        collector.delete_book_from_favorites("Гарри Поттер")
        assert "Гарри Поттер" not in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize("book_name", [
        "Очень длинное название книги, которое превышает сорок символов",
        "Книга с названием ровно в сорок один символ!"
    ])
    def test_add_new_book_invalid_name_not_added(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name not in collector.get_books_genre()

    def test_get_book_genre_nonexistent_book_returns_none(self):
        collector = BooksCollector()
        assert collector.get_book_genre("Несуществующая книга") is None

    def test_set_book_genre_nonexistent_book_no_change(self):
        collector = BooksCollector()
        collector.set_book_genre("Несуществующая книга", "Фантастика")
        assert len(collector.get_books_genre()) == 0
