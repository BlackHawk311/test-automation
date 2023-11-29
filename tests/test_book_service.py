import collections
from src.services.book_fetcher_service import BookFetcherService
from src.services.book_service import BookService


def test_list_book_ids(monkeypatch):
    # we define a function that will replace the existing function
    # instead of calling the mocked server, we use a controlled dataset
    def mock_get_books(*args):
        return [
            {'id': 'aaa-001', 'name': 'Origine', 'author': {'firstname': 'Dan', 'lastname': 'Brown'}},
            {'id': 'aaa-002', 'name': 'Anges & Démons', 'author': {'firstname': 'Dan', 'lastname': 'Brown'}},
        ]

    monkeypatch.setattr(BookFetcherService, 'get_books', mock_get_books)

    book_service = BookService(book_fetcher_service=BookFetcherService())
    ids = book_service.list_books_ids()

    assert ids == ['aaa-001', 'aaa-002']


def test_list_authors(monkeypatch):

    def mock_get_books(*args):
        return [
            {'id': 'aaa-001', 'name': 'Origine', 'author': {'firstname': 'Dan', 'lastname': 'Brown'}},
            {'id': 'aaa-002', 'name': 'Anges & Démons', 'author': {'firstname': 'Dan', 'lastname': 'Brown'}},
            {'id': 'aaa-003', 'name': 'Paradis ou Enfer', 'author': {'firstname': 'Michael', 'lastname': 'Johnson'}},
        ]

    monkeypatch.setattr(BookFetcherService, 'get_books', mock_get_books)

    book_service = BookService(book_fetcher_service=BookFetcherService())
    authors = book_service.list_books_authors()

#    assert authors == ['Brown Dan']
    assert collections.Counter(authors) == collections.Counter(['Brown Dan', 'Johnson Michael'])


def test_list_authors_without_firstname(monkeypatch):

    def mock_get_books(*args):
        return [
            {'id': 'aaa-001', 'name': 'Origine', 'author': {'firstname': 'Dan', 'lastname': 'Brown'}},
            {'id': 'aaa-002', 'name': 'Anges & Démons', 'author': {'firstname': 'Dan', 'lastname': 'Brown'}},
            {'id': 'aaa-003', 'name': 'Paradis ou Enfer', 'author': {'firstname': 'Michael', 'lastname': 'Johnson'}},
            {'id': 'aaa-004', 'name': 'Enfer ou Enfer', 'author': {'firstname': '', 'lastname': 'Johnson'}},
        ]

    monkeypatch.setattr(BookFetcherService, 'get_books', mock_get_books)

    book_service = BookService(book_fetcher_service=BookFetcherService())
    authors = book_service.list_books_authors()

    assert collections.Counter(authors) == collections.Counter(['Brown Dan', 'Johnson Michael', 'Johnson '])


def test_list_without_books(monkeypatch):

    def mock_get_books(*args):
        return []

    monkeypatch.setattr(BookFetcherService, 'get_books', mock_get_books)

    book_service = BookService(book_fetcher_service=BookFetcherService())
    books = book_service.list_books_authors()

#    assert books == []

    assert collections.Counter(books) == collections.Counter([])


def test_list_books_with_multi_authors(monkeypatch):

    def mock_get_books(*args):
        return [
            {'id': 'aaa-001', 'name': 'Origine', 'author': {'firstname': 'Dan', 'lastname': 'Brown'}},
            {'id': 'aaa-002', 'name': 'Anges & Démons', 'author': {'firstname': 'Dan', 'lastname': 'Brown'}},
            {'id': 'aaa-003', 'name': 'Paradis ou Enfer', 'authors': [{'firstname': 'Michael', 'lastname': 'Johnson'},
                                                                      {'firstname': 'Stephen', 'lastname': 'Thomson'}]
             },
        ]

    monkeypatch.setattr(BookFetcherService, 'get_books', mock_get_books)

    book_service = BookService(book_fetcher_service=BookFetcherService())
    authors = book_service.list_books_with_more_authors()

    assert collections.Counter(authors) == collections.Counter(['Brown Dan', 'Johnson Michael & Thomson Stephen'])

