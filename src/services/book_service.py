class BookService:
    def __init__(self, book_fetcher_service):
        self.book_fetcher_service = book_fetcher_service

    def list_books_ids(self):
        books = self.book_fetcher_service.get_books()
        return list(map(lambda book: book['id'], books))

    def list_books_authors(self):
        books = self.book_fetcher_service.get_books()
        return list(set(map(lambda book: book['author']['lastname'] + ' ' + book['author']['firstname'], books)))

    # def list_books_with_more_authors(self):
    #     books = self.book_fetcher_service.get_books()
    #     for item in books:
    #         if item['author']['lastname'] and item['author']['firstname']:
    #             list(set(map(lambda book: item['author']['lastname'] + ' ' + item['author']['firstname'], books)))
    #         else:
    #             list(set(map(lambda book: item['authors'][{'lastname'}] + ' ' + item['authors'][{'firstname'}] + ' & ' +
    #                                       item['authors'][{'lastname'}] + ' ' + item['authors'][{'firstname'}], books)))
