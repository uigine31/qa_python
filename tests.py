import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize("book_name", ["Гарри Поттер", "Властелин колец"])
    def test_add_new_book_add_one_book(self, collector, book_name):
        collector.add_new_book(book_name)
        assert collector.get_book_genre(book_name) == ""

    def test_set_book_genre_set_genre_for_book(self, collector):
        collector.add_new_book("1984")
        collector.set_book_genre("1984", "Фантастика")
        assert collector.get_book_genre("1984") == "Фантастика"

    @pytest.mark.parametrize("genre, expected_book", [
        ("Фантастика", "Гарри Поттер"),
        ("Мультфильмы", "Винни Пух")
    ])
    def test_get_books_with_specific_genre_get_books_by_genre(self, collector, genre, expected_book):
        collector.add_new_book("Гарри Поттер")
        collector.add_new_book("Винни Пух")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        collector.set_book_genre("Винни Пух", "Мультфильмы")
        books = collector.get_books_with_specific_genre(genre)
        assert expected_book in books

    def test_get_books_for_children_get_children_books(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.add_new_book("Оно")
        collector.set_book_genre("Гарри Поттер", "Мультфильмы")
        collector.set_book_genre("Оно", "Ужасы")
        children_books = collector.get_books_for_children()
        assert "Гарри Поттер" in children_books and "Оно" not in children_books

    @pytest.mark.parametrize("book_name", ["Гарри Поттер", "1984"])
    def test_add_book_in_favorites_add_to_favorites(self, collector, book_name):
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_remove_from_favorites(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        collector.delete_book_from_favorites("Гарри Поттер")
        assert "Гарри Поттер" not in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize("book_name", [
        "Очень длинное название книги, которое превышает сорок символов",
        "Книга с названием ровно в сорок один символ!"
    ])
    def test_add_new_book_invalid_name_not_added(self, collector, book_name):
        collector.add_new_book(book_name)
        assert collector.get_book_genre(book_name) is None

    def test_get_book_genre_nonexistent_book_returns_none(self, collector):
        assert collector.get_book_genre("Несуществующая книга") is None

    def test_get_book_genre_existing_book_returns_genre(self, collector):
        collector.add_new_book("1984")
        collector.set_book_genre("1984", "Фантастика")
        assert collector.get_book_genre("1984") == "Фантастика"

    def test_set_book_genre_nonexistent_book_no_change(self, collector):
        collector.set_book_genre("Несуществующая книга", "Фантастика")
        assert len(collector.get_books_genre()) == 0

    def test_get_books_genre_returns_correct_dictionary(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.add_new_book("1984")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        collector.set_book_genre("1984", "Ужасы")
        expected = {"Гарри Поттер": "Фантастика", "1984": "Ужасы"}
        assert collector.get_books_genre() == expected

    def test_get_list_of_favorites_books_returns_correct_list(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.add_new_book("1984")
        collector.add_book_in_favorites("Гарри Поттер")
        collector.add_book_in_favorites("1984")
        expected = ["Гарри Поттер", "1984"]
        assert collector.get_list_of_favorites_books() == expected
