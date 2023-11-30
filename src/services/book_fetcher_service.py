import requests


class BookFetcherService:
    @staticmethod
    def get_books():
        r = requests.get('http://localhost:1080/books')
        return r.json()
