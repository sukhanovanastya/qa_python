from main import BooksCollector

class TestBooksCollector:

    # Тест для добавления двух книг
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    # Тест для проверки добавления книги с некорректным названием (пустая строка)
    def test_add_new_book_empty_name(self):
        collector = BooksCollector()

        collector.add_new_book('')

        assert len(collector.get_books_genre()) == 0

    # Тест для проверки добавления книги с длинным названием (более 40 символов)
    def test_add_new_book_long_name(self):
        collector = BooksCollector()

        long_name = 'Очень длинное название книги, которое превышает 40 символов и должно быть отброшено'
        collector.add_new_book(long_name)

        assert len(collector.get_books_genre()) == 0

    # Тест для установки жанра книги
    def test_set_book_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')

        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    # Тест для установки жанра книги с несуществующим жанром
    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Несуществующий жанр')

        assert collector.get_book_genre('Гордость и предубеждение и зомби') == ''

    # Тест для получения книг с определенным жанром
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.set_book_genre('Книга 1', 'Фантастика')
        collector.set_book_genre('Книга 2', 'Ужасы')

        assert collector.get_books_with_specific_genre('Фантастика') == ['Книга 1']

    # Тест для получения книг, подходящих для детей
    def test_get_books_for_children(self):
        collector = BooksCollector()

        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.set_book_genre('Книга 1', 'Фантастика')
        collector.set_book_genre('Книга 2', 'Ужасы')

        assert collector.get_books_for_children() == ['Книга 1']

    # Тест для добавления книги в избранное
    def test_add_book_in_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        assert 'Гордость и предубеждение и зомби' in collector.get_list_of_favorites_books()

    # Тест для удаления книги из избранного
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')

        assert 'Гордость и предубеждение и зомби' not in collector.get_list_of_favorites_books()

    # Тест для получения списка избранных книг

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()

        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.add_book_in_favorites('Книга 1')
        collector.add_book_in_favorites('Книга 2')

        assert collector.get_list_of_favorites_books() == ['Книга 1', 'Книга 2']